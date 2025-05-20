# editing.py
# This module allows the user to add, delete, update, list, or search vocabulary

from vocab_utils import (
    load_vocab,
    save_vocab,
    normalize_text,
    find_word_index,
    ensure_unit_exists,
    search_word_global,
    get_unit_choice
)

## Function: editing_mode
## Purpose: Main menu for editing vocabulary
## Returns: None
def editing_mode() -> None:
    while True:
        ## Display menu options
        print("\n Editing Mode")
        print("1. Add word")
        print("2. Delete word")
        print("3. Update word")
        print("4. List words")
        print("5. Search word across units")
        print("6. Back to main menu")

        choice = input("Choose an option: ").strip()

        ## Route user to appropriate action
        if choice == "1":
            add_word()
        elif choice == "2":
            delete_word()
        elif choice == "3":
            update_word()
        elif choice == "4":
            list_words()
        elif choice == "5":
            search_word()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

## Function: add_word
## Purpose: Add a new English-Hebrew pair to the chosen unit
def add_word() -> None:
    vocab = load_vocab()
    unit = get_unit_choice()
    ensure_unit_exists(vocab, unit)

    word = normalize_text(input("Enter English word: "))
    meaning = input("Enter Hebrew meaning: ").strip()

    if find_word_index(vocab[unit], word) != -1:
        print(" Word already exists in this unit.")
        return

    vocab[unit].append({"word": word, "meaning": meaning})
    save_vocab(vocab)
    print(f" '{word}' added to {unit}.")

## Function: delete_word
## Purpose: Delete an English word from a unit
def delete_word() -> None:
    vocab = load_vocab()
    unit = get_unit_choice()

    if unit not in vocab:
        print(" Unit does not exist.")
        return

    word = normalize_text(input("Enter English word to delete: "))
    index = find_word_index(vocab[unit], word)

    if index == -1:
        print(" Word not found.")
        return

    confirm = input(f"Are you sure you want to delete '{word}'? (y/n): ").strip().lower()
    if confirm == "y":
        del vocab[unit][index]
        save_vocab(vocab)
        print(f" '{word}' deleted from {unit}.")
    else:
        print("Deletion canceled.")

## Function: update_word
## Purpose: Update an existing word or its meaning
def update_word() -> None:
    vocab = load_vocab()
    unit = get_unit_choice()

    if unit not in vocab:
        print(" Unit does not exist.")
        return

    old_word = normalize_text(input("Enter word to update: "))
    index = find_word_index(vocab[unit], old_word)

    if index == -1:
        print(" Word not found.")
        return

    new_word = normalize_text(input("Enter new word: "))
    new_meaning = input("Enter new meaning: ").strip()

    vocab[unit][index] = {"word": new_word, "meaning": new_meaning}
    save_vocab(vocab)
    print(f" '{old_word}' updated to '{new_word}' with meaning '{new_meaning}'.")

## Function: list_words
## Purpose: Display all words in a selected unit
def list_words() -> None:
    vocab = load_vocab()
    unit = get_unit_choice()

    if unit not in vocab or not vocab[unit]:
        print(" Unit is empty or does not exist.")
        return

    print(f"\n Words in {unit}:")
    for entry in vocab[unit]:
        print(f" - {entry['word']} : {entry['meaning']}")

## Function: search_word
## Purpose: Search for a word across all units
def search_word() -> None:
    vocab = load_vocab()
    search_term = input("Enter word to search: ").strip()
    results = search_word_global(vocab, search_term)

    if results:
        print(f"\n Found '{search_term}' in the following units:")
        for unit, word, meaning in results:
            print(f" - {unit}: {word} → {meaning}")
    else:
        print(" Word not found in any unit.")
