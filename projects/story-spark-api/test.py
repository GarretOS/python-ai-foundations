"""A small requests-based client for exercising the Story Spark API."""

import argparse
import sys

import requests

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT_SECONDS = 5
STORY_FIELDS = ("title", "premise", "plot_twist")


def request(method, path, **kwargs):
    """Send one request and report local connection problems clearly."""
    try:
        return requests.request(method, f"{BASE_URL}{path}", timeout=TIMEOUT_SECONDS, **kwargs)
    except requests.exceptions.Timeout as error:
        raise RuntimeError("The API request timed out. Check that the server is running.") from error
    except requests.exceptions.ConnectionError as error:
        raise RuntimeError("Could not connect to the API. Start the server in another terminal.") from error


def assert_valid_stories(payload, expected_count):
    """Assert the successful generation response contains complete stories."""
    assert isinstance(payload, dict), "The response must be a JSON object."
    stories = payload.get("stories")
    assert isinstance(stories, list), "The response must contain a stories list."
    assert len(stories) == expected_count, f"Expected {expected_count} stories, got {len(stories)}."
    for index, story in enumerate(stories, start=1):
        assert isinstance(story, dict), f"Story {index} must be an object."
        for field in STORY_FIELDS:
            assert isinstance(story.get(field), str) and story[field].strip(), (
                f"Story {index} must have a nonblank {field}."
            )
    return stories


def check_status(response, expected_status):
    """Check an HTTP status before reading successful response data."""
    assert response.status_code == expected_status, (
        f"Expected HTTP {expected_status}, received {response.status_code}: {response.text}"
    )


def run_offline_checks():
    """Exercise history retrieval and validation without calling Gemini."""
    response = request("GET", "/stories")
    check_status(response, 200)
    history = response.json()
    assert isinstance(history, list), "History must be a JSON list."
    print(f"History retrieval passed ({len(history)} existing entries).")
    cases = (
        ({"genre": " ", "setting": "A lighthouse", "character": "Mira", "num_stories": 1}, 400, "blank genre"),
        ({"genre": "Fantasy", "setting": "A lighthouse", "character": "Mira", "num_stories": 4}, 400, "out-of-range count"),
        ({"setting": "A lighthouse", "character": "Mira", "num_stories": 1}, 422, "missing required field"),
    )
    for payload, expected_status, label in cases:
        response = request("POST", "/generate-stories", json=payload)
        check_status(response, expected_status)
        print(f"{label} check passed (HTTP {expected_status}).")


def run_live_demo():
    """Generate two real stories and confirm the request appears in history."""
    payload = {
        "genre": "cozy science fiction",
        "setting": "a floating night market on Europa",
        "character": "a retired cartographer",
        "num_stories": 2,
    }
    response = request("POST", "/generate-stories", json=payload)
    check_status(response, 200)
    stories = assert_valid_stories(response.json(), 2)
    history_response = request("GET", "/stories")
    check_status(history_response, 200)
    history = history_response.json()
    assert isinstance(history, list), "History must be a JSON list."
    assert any(
        entry.get("genre") == payload["genre"]
        and entry.get("setting") == payload["setting"]
        and entry.get("character") == payload["character"]
        and entry.get("num_stories") == 2
        and entry.get("stories") == stories
        for entry in history
    ), "The completed request was not found in history."
    print("Live generation passed: received two valid stories and found the request in history.")


def main():
    parser = argparse.ArgumentParser(description="Check the local Story Spark API.")
    parser.add_argument("--live", action="store_true", help="Generate two stories using Gemini (uses API quota).")
    arguments = parser.parse_args()
    try:
        if arguments.live:
            run_live_demo()
        else:
            run_offline_checks()
    except (AssertionError, RuntimeError, requests.exceptions.RequestException, ValueError) as error:
        print(f"Check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
