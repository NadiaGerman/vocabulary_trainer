# vocab_utils.py
# Utility functions for managing vocabulary and tracking practice repetitions, including S3 upload.

import json  # Built-in module to work with JSON files
import os
import unicodedata    # Built-in module to interact with the file system
import boto3 # AWS SDK for uploading files to S3

VOCAB_FILE = "vocab_hebrew.json"         # Local file to store vocabulary data
REPEAT_FILE = "repeat_log.json"          # Local file to store word repetition log

def normalize_text(text: str) -> str:
    """
    Normalize text to Unicode NFC and lowercase it.
    Useful for comparing Hebrew/English input consistently.

    Args:
        text (str): Raw user input

    Returns:
        str: Normalized string
    """
    ## Normalize the input text using Unicode NFC and lowercase
    return unicodedata.normalize("NFC", text.strip().lower())


def get_unit_choice() -> str:
    """
    Show a numbered menu and return the selected unit name as unit_1, unit_2, etc.

    Returns:
        str: Formatted unit name like 'unit_1'
    """
    print("\nChoose a unit:")
    print("1. Unit 1 - Fruits & Vegetables")
    print("2. Unit 2 - School / Study")
    print("3. Unit 3 - Weather / Nature")

    ## Ask user for numeric choice
    choice = input("Enter 1, 2, or 3: ").strip()
    return f"unit_{choice}"


def load_vocab() -> dict:
    """
    Load vocabulary from the local JSON file.

    Returns:
        dict: A dictionary with unit names as keys and lists of word dictionaries as values.
    """
    ## If file doesn't exist, return empty vocab dictionary
    if not os.path.exists(VOCAB_FILE):
        return {}
    ## Open the file and parse JSON into a dictionary
    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_vocab(vocab: dict) -> None:
    """
    Save vocabulary to the local JSON file.

    Args:
        vocab (dict): The full vocabulary dictionary.

    Returns:
        None
    """
    ## Dump dictionary into JSON format with UTF-8 and indenting
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)

def clean_word(word: str) -> str:
    """
    Normalize a word: strip whitespace and convert to lowercase.

    Args:
        word (str): The input word.

    Returns:
        str: Cleaned word.
    """
    ## Ensure word is stripped of extra spaces and is lowercase
    return word.strip().lower()

def find_word_index(unit_list: list, word: str) -> int:
    """
    Search for a word in a unit list.

    Args:
        unit_list (list): List of word dictionaries.
        word (str): Word to search.

    Returns:
        int: Index of the word, or -1 if not found.
    """
    word = clean_word(word)
    for i, item in enumerate(unit_list):
        ## Compare each word after cleaning formatting
        if clean_word(item.get("word", "")) == word:
            return i
    return -1  # Not found

def ensure_unit_exists(vocab: dict, unit: str) -> None:
    """
    Ensure a unit exists in the vocabulary.

    Args:
        vocab (dict): Vocabulary dictionary.
        unit (str): Name of the unit.

    Returns:
        None
    """
    ## If the unit is not present, create an empty list for it
    if unit not in vocab:
        vocab[unit] = []

def search_word_global(vocab: dict, search_term: str) -> list:
    """
    Search for a word across all units.

    Args:
        vocab (dict): Vocabulary dictionary.
        search_term (str): Word to search.

    Returns:
        list: List of tuples (unit, word, meaning).
    """
    matches = []
    search_term = clean_word(search_term)

    ## Loop through each unit and search in every word entry
    for unit, entries in vocab.items():
        for entry in entries:
            if clean_word(entry["word"]) == search_term:
                matches.append((unit, entry["word"], entry["meaning"]))
    return matches

def load_repeat_log() -> dict:
    """
    Load the repeat log from file if it exists.

    Returns:
        dict: Repeat log dictionary.
    """
    ## Return an empty dictionary if the file doesn't exist
    if not os.path.exists(REPEAT_FILE):
        return {}
    ## Load and return the repeat log
    with open(REPEAT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_repeat_log(log: dict) -> None:
    """
    Save the repeat log to file.

    Args:
        log (dict): Repeat log data.

    Returns:
        None
    """
    ## Save repeat tracking dictionary to JSON
    with open(REPEAT_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=4)

def log_word_repeat(log: dict, unit: str, word: str) -> None:
    """
    Increment the repeat counter for a word in a unit.

    Args:
        log (dict): Repeat log dictionary.
        unit (str): Unit name.
        word (str): Practiced word.

    Returns:
        None
    """
    unit = clean_word(unit)
    word = clean_word(word)

    ## Initialize unit dictionary if missing
    if unit not in log:
        log[unit] = {}

    ## Initialize word counter if missing
    if word not in log[unit]:
        log[unit][word] = 0

    ## Increment counter by 1
    log[unit][word] += 1

def upload_log_to_s3(bucket_name: str, file_path: str, s3_key: str) -> bool:
    """
    Upload a local file to an S3 bucket.

    Args:
        bucket_name (str): Name of the S3 bucket.
        file_path (str): Path to the local file.
        s3_key (str): Key name for the file in S3.

    Returns:
        bool: True if upload succeeds, False otherwise.
    """
    try:
        ## Create S3 client and upload the file
        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f" Uploaded {file_path} to S3 bucket {bucket_name} as {s3_key}")
        return True
    except Exception as e:
        ## If upload fails, print the error
        print(f" Failed to upload to S3: {e}")
        return False
