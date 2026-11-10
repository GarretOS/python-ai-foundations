"""A small FastAPI service for generating and saving story ideas."""

import asyncio
import json
import logging
import os
import tempfile
from pathlib import Path

from fastapi import Body, FastAPI, HTTPException
from google import genai
from google.genai import types

app = FastAPI(title="Story Spark API")
DATA_FILE = Path(__file__).parent / "data.json"
HISTORY_LOCK = asyncio.Lock()
DEFAULT_MODEL = "gemini-3.5-flash-lite"
STORY_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "A short story title."},
        "premise": {"type": "string", "description": "A short story premise."},
        "plot_twist": {"type": "string", "description": "A surprising plot twist."},
    },
    "required": ["title", "premise", "plot_twist"],
    "additionalProperties": False,
}
logger = logging.getLogger(__name__)


def load_data():
    """Load saved requests, treating only a missing file as empty history."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as history_file:
            history = json.load(history_file)
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError("Could not read the story history file.") from error
    if not isinstance(history, list):
        raise ValueError("The story history file must contain a JSON list.")
    return history


def save_data(history):
    """Replace history atomically so a failed write cannot truncate the old file."""
    temporary_path = None
    try:
        # Keep the temporary file beside data.json so os.replace stays on one filesystem.
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=DATA_FILE.parent,
            prefix="data-", suffix=".tmp", delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            json.dump(history, temporary_file, ensure_ascii=False, indent=2)
            temporary_file.write("\n")
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        os.replace(temporary_path, DATA_FILE)
    except OSError:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise


def build_prompt(genre, setting, character):
    """Build a focused prompt for one original story idea."""
    return (
        "Create one original fictional story idea using the details below. "
        "Keep the premise short and include a surprising plot twist. "
        "Do not write the full story.\n\n"
        f"Genre: {genre}\nSetting: {setting}\nMain character: {character}"
    )


def validate_story(story):
    """Check both the JSON shape and the content of a generated story."""
    required_fields = ("title", "premise", "plot_twist")
    if not isinstance(story, dict):
        raise ValueError("The generated story must be a JSON object.")
    for field in required_fields:
        value = story.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"The generated story has an invalid {field} field.")
    return {field: story[field].strip() for field in required_fields}


async def generate_story(genre, setting, character):
    """Ask Gemini for one story and validate the returned JSON."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")
    model = os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
    async with genai.Client(api_key=api_key).aio as client:
        response = await client.models.generate_content(
            model=model,
            contents=build_prompt(genre, setting, character),
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_json_schema=STORY_RESPONSE_SCHEMA,
            ),
        )
    if not response.text:
        raise ValueError("The model returned an empty response.")
    return validate_story(json.loads(response.text))


@app.post("/generate-stories")
async def generate_stories(
    genre: str = Body(...),
    setting: str = Body(...),
    character: str = Body(...),
    num_stories: int = Body(3),
):
    """Generate 1-3 story ideas and save them as one history entry."""
    genre, setting, character = genre.strip(), setting.strip(), character.strip()
    for field, value in (("genre", genre), ("setting", setting), ("character", character)):
        if not value:
            raise HTTPException(status_code=400, detail=f"{field} must not be blank.")
    if not 1 <= num_stories <= 3:
        raise HTTPException(status_code=400, detail="num_stories must be between 1 and 3.")
    if not os.environ.get("GEMINI_API_KEY"):
        raise HTTPException(status_code=503, detail="Story generation is unavailable: GEMINI_API_KEY is not configured.")

    results = await asyncio.gather(
        *(generate_story(genre, setting, character) for _ in range(num_stories)),
        return_exceptions=True,
    )
    failure = next((result for result in results if isinstance(result, BaseException)), None)
    if failure is not None:
        logger.error("Story generation failed", exc_info=(type(failure), failure, failure.__traceback__))
        raise HTTPException(status_code=502, detail="Story generation failed. Please try again.")

    entry = {
        "genre": genre,
        "setting": setting,
        "character": character,
        "num_stories": num_stories,
        "stories": results,
    }
    try:
        async with HISTORY_LOCK:
            history = load_data()
            history.append(entry)
            save_data(history)
    except (OSError, ValueError) as error:
        logger.exception("Could not save story history")
        raise HTTPException(status_code=500, detail="Stories were generated, but history could not be saved.") from error
    return {"stories": results}


@app.get("/stories")
async def get_stories():
    """Return all saved generation requests."""
    try:
        async with HISTORY_LOCK:
            return load_data()
    except (OSError, ValueError) as error:
        logger.exception("Could not load story history")
        raise HTTPException(status_code=500, detail="Story history could not be read.") from error


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
