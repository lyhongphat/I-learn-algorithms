import json
import os

def load_translation(language: str) -> tuple:
    """
    Load translation data for the specified language with English fallback.
    
    Args:
        language (str): The language to load ('English', 'Vietnamese', 'Japanese', or 'Korean')
    
    Returns:
        tuple: (translations dict, missing_keys set) - translations for specified language with English fallback,
               and a set of keys that were missing in the selected language
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
    
    # Load English translations as fallback
    english_path = os.path.join(translations_dir, language_files['English'])
    with open(english_path, 'r', encoding='utf-8') as f:
        english_translations = json.load(f)
    
    # If selected language is English, return it with empty missing keys set
    if language == 'English':
        return english_translations, set()
        
    # Load the selected language translations
    file_path = os.path.join(translations_dir, language_files[language])
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            selected_translations = json.load(f)
            
        # Find keys that exist in English but not in selected language
        missing_keys = set(english_translations.keys()) - set(selected_translations.keys())
        
        # Create merged translations with English fallback for missing keys
        merged_translations = english_translations.copy()
        merged_translations.update(selected_translations)
        
        return merged_translations, missing_keys
    except FileNotFoundError:
        print(f"Translation file not found for language: {language}")
        # Fall back to English if translation is not found
        with open(os.path.join(translations_dir, 'english.json'), 'r', encoding='utf-8') as f:
            return json.load(f)