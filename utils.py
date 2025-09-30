import json
import os

def load_translation(language: str) -> dict:
    """
    Load translation data for the specified language.
    
    Args:
        language (str): The language to load ('English', 'Vietnamese', 'Japanese', or 'Korean')
    
    Returns:
        dict: Translation data for the specified language
    """
    # Map full language names to file names
    language_files = {
        'English': 'english.json',
        'Vietnamese': 'vietnamese.json',
        'Japanese': 'japanese.json',
        'Korean': 'korean.json'
    }
    
    # Get the current file's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    translations_dir = os.path.join(current_dir, 'translations')
    
    # Load the translation file
    file_path = os.path.join(translations_dir, language_files[language])
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Translation file not found for language: {language}")
        # Fall back to English if translation is not found
        with open(os.path.join(translations_dir, 'english.json'), 'r', encoding='utf-8') as f:
            return json.load(f)