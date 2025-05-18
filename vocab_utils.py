import json
import os

VOCAB_FILE = "vocab_hebrew.json"

def load_vocab():
    """
    Load vocabulary from the JSON file.

    Returns:
        dict: Dictionary with units and their word lists.
    """
    if not os.path.exists(VOCAB_FILE):
        return {}  # If the file doesn't exist, return an empty dictionary
    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)  # Parse and return JSON content

def save_vocab(vocab):
    """
    Save the vocabulary to the JSON file.

    Args:
        vocab (dict): The full vocabulary dictionary.
    """
    # Save the vocab dictionary as JSON with Hebrew-friendly encoding
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)

def clean_word(word):
    """
    Normalize input by removing extra spaces and converting to lowercase.

    Args:
        word (str): The word to clean.

    Returns:
        str: Cleaned word.
    """
    return word.strip().lower()  # Remove whitespace and lower the case

def find_word_index(unit_list, word):
    """
    Search for a word in a unit's list of word dictionaries.

    Args:
        unit_list (list): A list of {"word", "meaning"} dictionaries.
        word (str): The word to search for.

    Returns:
        int: Index of the word if found, -1 otherwise.
    """
    word = clean_word(word)
    for i, item in enumerate(unit_list):
        # Compare cleaned word values
        if clean_word(item.get("word", "")) == word:
            return i
    return -1  # Word not found

def ensure_unit_exists(vocab, unit):
    """
    Ensure the given unit exists in the vocabulary.

    Args:
        vocab (dict): The vocabulary dictionary.
        unit (str): The unit name (e.g. "unit_1").
    """
    # If the unit is not in the dictionary, initialize it as an empty list
    if unit not in vocab:
        vocab[unit] = []

def search_word_global(vocab, search_term):
    """
    Search for a word across all units.

    Args:
        vocab (dict): The vocabulary dictionary.
        search_term (str): The word to search for.

    Returns:
        list: A list of tuples (unit, word, meaning) for each match found.
    """
    matches = []
    search_term = clean_word(search_term)

    for unit, entries in vocab.items():
        for entry in entries:
            # Compare each word to the search term
            if clean_word(entry["word"]) == search_term:
                matches.append((unit, entry["word"], entry["meaning"]))

    return matches
