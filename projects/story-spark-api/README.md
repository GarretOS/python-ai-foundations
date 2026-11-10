# ✨ Story Spark API

Story Spark is a beginner-friendly local API that creates short fictional story ideas with Gemini and saves successful requests to a JSON history file.

## 🎯 Overview and Features

- FastAPI endpoint for requesting one to three story ideas
- One Gemini call per story, run concurrently with `asyncio.gather()`
- Required Gemini JSON response schema plus nonblank validation for title, premise, and plot twist
- JSON file persistence with a history endpoint
- Separate `requests` client for offline API checks and optional live generation

The API generates story premises, not full stories. Valid structure does not guarantee creative quality, originality, or exact tone adherence. In the user-tested example, two stories used cozy science fiction, a floating night market on Europa, and a retired cartographer, but their tone was not perfectly cozy.

## 🐍 Concepts Practiced

- FastAPI routes, decorators, JSON request bodies, and HTTP responses
- `async` / `await` and concurrent coroutines
- Input validation and checking AI-generated output
- Reading and writing JSON data
- Environment variables for API credentials
- A separate Python client that sends HTTP requests

## 📁 File Structure

```text
story-spark-api/
├── .gitignore
├── README.md
├── requirements.txt
├── server.py
├── story_spark.ipynb
└── test.py
```

`server.py` is the primary application. `test.py` is the separate HTTP client, and `story_spark.ipynb` is the educational notebook companion that reuses the server.

`data.json` is created beside `server.py` after the first successful generation request and is ignored by Git. Atomic-write files, copied notebook history, virtual environments, caches, notebook checkpoints, and local environment credential files are also ignored.

## 🚀 Local Setup

Use Python 3.10 or newer. From this project directory, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```text
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Set `GEMINI_API_KEY` to your own key in the terminal where the server will run. Never add the key to source files or commit it.

Optionally set `GEMINI_MODEL` to override the default model, `gemini-3.5-flash-lite`.

macOS / Linux:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
# Optional:
export GEMINI_MODEL="gemini-3.5-flash-lite"
python server.py
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
# Optional:
$env:GEMINI_MODEL = "gemini-3.5-flash-lite"
python server.py
```

Set environment variables before starting the server. `GEMINI_API_KEY` supplies the credential; `GEMINI_MODEL` selects the model. The application does not automatically load a `.env` file. You can omit the key for offline checks.

The server listens only on `127.0.0.1:8000`. History retrieval works without an API key; generation returns HTTP 503 when the key is missing.

## 🪟 Run the Server and Client

Open two terminals in this directory. In terminal one, activate the environment, set `GEMINI_API_KEY` if you intend to generate stories, and run:

```bash
python server.py
```

In terminal two, activate the environment and run the default offline checks:

```bash
python test.py
```

These checks read history and send invalid requests only; they do not call Gemini.

Keep terminal one running while terminal two sends requests. Stop the server with **Ctrl+C** when finished.

For a live demonstration, use:

```bash
python test.py --live
```

The live option sends real requests to Gemini, generates two stories, and uses API quota. It does not clear existing history.

## 📡 Routes and Request Validation

| Method and route | Request | Successful response |
| --- | --- | --- |
| `POST /generate-stories` | JSON body with required `genre`, `setting`, and `character` strings; optional `num_stories` integer (default `3`, range `1–3`) | `200`, `{"stories": [...]}` |
| `GET /stories` | No body | `200`, list of saved requests; `[]` if the file is absent |

Text inputs are stripped and must remain nonblank. FastAPI validates required fields and annotated types; some compatible values can be converted rather than rejected. Each saved request includes its ingredients, count, and story list. No history entry is saved unless all stories succeed, validate, and can be written.

## 💡 API Examples

Generate one story idea (uses Gemini quota):

```bash
curl -X POST http://127.0.0.1:8000/generate-stories \
  -H "Content-Type: application/json" \
  -d '{"genre":"fantasy","setting":"a city inside a mountain","character":"a young clockmaker","num_stories":1}'
```

Example response:

```json
{
  "stories": [
    {
      "title": "The Mountain's Last Hour",
      "premise": "A clockmaker discovers that the city's clocks keep a sleeping giant's heartbeat in rhythm. When the clocks begin to drift, she must repair the oldest mechanism before the city wakes what lies beneath it.",
      "plot_twist": "The clockmaker's own workshop is the giant's missing heart chamber."
    }
  ]
}
```

Read the complete saved history:

```bash
curl http://127.0.0.1:8000/stories
```

The history response is a JSON list. It is `[]` before any successful generation request.

## 🌐 Notebook / Google Colab Companion

<a href="https://colab.research.google.com/github/GarretOS/python-ai-foundations/blob/main/projects/story-spark-api/story_spark.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Open the notebook using the badge above, or upload a local copy to Colab:

1. Open [Google Colab](https://colab.research.google.com/) and choose **File → Upload notebook** to upload local `story_spark.ipynb`.
2. In the Colab **Files** sidebar, upload local `server.py` and `requirements.txt` directly into `/content`. Do not upload credentials or `data.json`. The notebook reuses these uploaded source files rather than downloading application code from GitHub.
3. Keep `RUN_LIVE = False` and run the cells from top to bottom. No key is needed. Setup installs the project dependencies; the demonstrations retrieve history and check invalid input using real HTTP requests.
4. Optionally add `GEMINI_API_KEY` in Colab **Secrets** and enable notebook access. Change `RUN_LIVE = True`, optionally change `MODEL_NAME` (which sets `GEMINI_MODEL`), then rerun from the configuration cell through the remaining cells. This generates two real stories and verifies their saved history. Outside Colab, the notebook uses the environment key or hidden `getpass()` input.
5. Run the cleanup cell to stop the server. Download the separate history file from the printed location if you want to retain live results. Colab runtime storage is temporary.

The notebook starts Uvicorn in a separate Python process bound to `127.0.0.1` on an available port. It waits for readiness with a bounded timeout and uses `requests` for actual HTTP calls. This avoids notebook event-loop conflicts without `asyncio.run()` in cells. Rerunning startup stops the old notebook process, and cleanup stops the current one. It imports the existing server and overrides only its history path inside the child process, leaving the project's `data.json` untouched. No public URL is created.

For local Jupyter, use a Python 3.10+ kernel and open the notebook beside the source files or start Jupyter from the repository root. Install Jupyter separately if needed; it is not an application dependency. The notebook's temporary history directory is reused within a kernel and changes in a fresh kernel.

## ⚠️ Error Behavior and Limitations

- Blank text fields and `num_stories` outside 1–3 return HTTP 400 with a helpful detail.
- Missing fields and invalid JSON field types use FastAPI's normal validation response, typically HTTP 422.
- A missing `GEMINI_API_KEY` returns HTTP 503 for generation.
- A generation or story-output validation failure returns HTTP 502. The request is all-or-nothing: nothing is saved unless every story succeeds and validates.
- Gemini receives a JSON schema requiring `title`, `premise`, and `plot_twist` as strings. The server still checks that each value is nonblank because a schema does not enforce nonblank content.
- A malformed or incorrectly shaped existing history file returns HTTP 500 and is preserved.
- History storage uses small synchronous JSON file operations while holding an `asyncio.Lock`. This is suitable for a small local demonstration with one server process; it is not a multi-process database.
- Concurrent Gemini calls may still consume quota even when another call causes the overall request to fail.
- Provider diagnostics are written to server logs; provider details and credentials are not returned to clients.
- History validation checks JSON readability and the top-level list, not the shape of every historical entry. Storage has no size limit, pagination, backup, or coordination between multiple server processes.
- Model access, pricing, and quota depend on the user's Google account and can change. The configured default is `gemini-3.5-flash-lite`; use `GEMINI_MODEL` to override it.
- The required JSON schema fixed an observed live failure involving an invalid `plot_twist`. Do not remove the schema or weaken the nonblank field checks.
- The user verified local live generation of two valid stories, history retrieval, persistence across a server restart, and the expected HTTP 400/422 input errors. No live Gemini calls were made for this documentation task.
- The non-live notebook flow was executed in a fresh local Jupyter kernel, including startup, reruns, and cleanup. Actual Google Colab testing is pending.

## 📚 Notes

This project practices connecting a Python API to an asynchronous model client, validating the model's JSON content, saving successful results, and exercising the service from a separate client. The JSON file is intentionally simple and is appropriate only for a small local demonstration.
