import json
import os

VOCAB_FILE = "vocab_hebrew.json"


def load_vocab():
    """Load the vocabulary from the JSON file."""
    if not os.path.exists(VOCAB_FILE):
        return {}
    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_vocab(vocab):
    """Save the vocabulary to the JSON file."""
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)


def clean_word(word):
    """Clean user input: strip spaces and convert to lowercase."""
    return word.strip().lower()


def find_word_index(unit_list, word):
    """
    Search for a word in a unit (list of dicts).
    Returns index if found, else -1.
    """
    word = clean_word(word)
    for i, item in enumerate(unit_list):
        if clean_word(item.get("word", "")) == word:
            return i
    return -1


def ensure_unit_exists(vocab, unit):
    """Ensure the unit exists; create if it doesn't."""
    if unit not in vocab:
        vocab[unit] = []
