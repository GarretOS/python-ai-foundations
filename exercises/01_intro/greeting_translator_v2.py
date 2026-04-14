# greeting_translator_v2.py
# Extended version with English-only input validation.
# Generated with the assistance of ChatGPT through iterative prompting.
#
# Install dependencies: pip install deep-translator langdetect

import random
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

# Dictionary mapping language names to language codes
languages = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Hindi": "hi",
}

def is_valid_english(text: str) -> bool:
    """Check that the input is non-empty and in English."""
    if not text.strip():
        print("Error: Greeting cannot be empty. Please enter an English greeting.")
        return False

    try:
        language = detect(text)
    except LangDetectException:
        print("Error: Unable to detect language. Please enter a valid English greeting.")
        return False

    if language != "en":
        print("Error: Please enter the greeting in English only.")
        return False

    return True

def translate_greeting(greeting: str) -> None:
    """Translate the greeting into 3 randomly selected languages."""
    selected_languages = random.sample(list(languages.items()), 3)

    print(f"\nOriginal: {greeting}\n")

    for language_name, language_code in selected_languages:
        translated = GoogleTranslator(source="auto", target=language_code).translate(greeting)
        print(f"{language_name}: {translated}")

if __name__ == "__main__":
    # Keep prompting until a valid English greeting is entered
    while True:
        user_input = input("Enter an English greeting: ")

        if is_valid_english(user_input):
            translate_greeting(user_input)
            break
