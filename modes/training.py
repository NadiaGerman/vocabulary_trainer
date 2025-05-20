# training.py
# This module allows the user to practice vocabulary word-by-word with logging

import time
from vocab_utils import (
    load_vocab,
    find_word_index,
    load_repeat_log,
    save_repeat_log,
    log_word_repeat,
    upload_log_to_s3,
    get_unit_choice, 
    normalize_text 
)

## Function: training_mode
## Purpose: User practices vocabulary, repetition is logged, and log is uploaded to S3
## Returns: None
def training_mode() -> None:
    vocab = load_vocab()  ## Load vocab data from JSON
    unit = get_unit_choice()  ## Show menu to choose a unit

    if unit not in vocab or not vocab[unit]:
        print(" Unit does not exist or is empty.")
        return

    word_list = vocab[unit]  ## Words in the selected unit

    ## Ask user if they want full list or a specific range
    print("\nDo you want to practice the full unit or a word range?")
    mode = input("Type 'full' or 'range': ").strip().lower()

    ## Validate input
    if mode not in ["full", "range"]:
        print(" Invalid input. Please type 'full' or 'range'.")
        return  ## This return must be indented to work correctly

    if mode == "range":
        start_word = normalize_text(input("Enter start word: "))
        end_word = normalize_text(input("Enter end word: "))

        start_index = find_word_index(word_list, start_word)
        end_index = find_word_index(word_list, end_word)

        if start_index == -1 or end_index == -1 or start_index > end_index:
            print(" Invalid range. Make sure both words exist and are in order.")
            return

        word_list = word_list[start_index:end_index + 1]  ## Subset for practice

    repeat_log = load_repeat_log()  ## Load repeat tracking log

    print("\n Training begins! Press Enter to see the meaning...")
    for entry in word_list:
        print(f"\nWord: {entry['word']}")
        input("...")  ## Wait for user input
        print(f"Meaning: {entry['meaning']}")
        time.sleep(1)  ## Pause briefly

        ## Log and save repetition
        log_word_repeat(repeat_log, unit, entry['word'])
        save_repeat_log(repeat_log)
        upload_log_to_s3("your-s3-bucket-name", "repeat_log.json", "repeat_log.json")

    print("\n Training session complete.")
