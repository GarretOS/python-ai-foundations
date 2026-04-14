# greeting_translator.py
# Generated with the assistance of ChatGPT through iterative prompting.
#
# Install dependency: pip install deep-translator

import random
from deep_translator import GoogleTranslator

# List of possible target languages
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
    "Hindi": "hi"
}

def translate_greeting(greeting):
    # Randomly select 3 unique languages
    selected_languages = random.sample(list(languages.items()), 3)

    print(f"\nOriginal: {greeting}\n")

    for language_name, language_code in selected_languages:
        translated = GoogleTranslator(source='auto', target=language_code).translate(greeting)
        print(f"{language_name}: {translated}")

if __name__ == "__main__":
    user_input = input("Enter a greeting: ")
    translate_greeting(user_input)
