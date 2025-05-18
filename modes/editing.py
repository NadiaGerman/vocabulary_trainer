from vocab_utils import (
    load_vocab,
    save_vocab,
    clean_word,
    find_word_index,
    ensure_unit_exists,
    search_word_global
)

def editing_mode():
    """
    Menu for editing vocabulary:
    Allows user to add, delete, update, list, or search for words.
    Loops until the user chooses to return to the main menu.
    """
    while True:
        # Display menu options
        print("\n Editing Mode")
        print("1. Add word")
        print("2. Delete word")
        print("3. Update word")
        print("4. List words")
        print("5. Search word across units")
        print("6. Back to main menu")

        choice = input("Choose an option: ").strip()

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

def add_word():
    """
    Adds a new word to a given unit if it doesn't already exist.
    """
    vocab = load_vocab()
    unit = input("Enter unit name (e.g. unit_1): ").strip()

    # Make sure the unit exists in the vocabulary
    ensure_unit_exists(vocab, unit)

    # Get word and meaning from user
    word = clean_word(input("Enter English word: "))
    meaning = input("Enter Hebrew meaning: ").strip()

    # Check for duplicates
    if find_word_index(vocab[unit], word) != -1:
        print(" Word already exists in this unit.")
        return

    # Add word to the unit list
    vocab[unit].append({"word": word, "meaning": meaning})
    save_vocab(vocab)
    print(f" '{word}' added to {unit}.")

def delete_word():
    """
    Deletes a word from a given unit after user confirmation.
    """
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab:
        print(" Unit does not exist.")
        return

    word = clean_word(input("Enter English word to delete: "))
    index = find_word_index(vocab[unit], word)

    if index == -1:
        print(" Word not found.")
        return

    # Confirm before deleting
    confirm = input(f"Are you sure you want to delete '{word}'? (y/n): ").strip().lower()
    if confirm == "y":
        del vocab[unit][index]  # Remove word from list
        save_vocab(vocab)
        print(f" '{word}' deleted from {unit}.")
    else:
        print("Deletion canceled.")

def update_word():
    """
    Updates an existing word and/or its meaning.
    """
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab:
        print(" Unit does not exist.")
        return

    old_word = clean_word(input("Enter word to update: "))
    index = find_word_index(vocab[unit], old_word)

    if index == -1:
        print(" Word not found.")
        return

    # Ask user for new values
    new_word = clean_word(input("Enter new word: "))
    new_meaning = input("Enter new meaning: ").strip()

    # Replace the old word entry with new data
    vocab[unit][index] = {"word": new_word, "meaning": new_meaning}
    save_vocab(vocab)
    print(f" '{old_word}' updated to '{new_word}' with meaning '{new_meaning}'.")

def list_words():
    """
    Lists all words and meanings in the selected unit.
    """
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab or not vocab[unit]:
        print(" Unit is empty or does not exist.")
        return

    print(f"\n Words in {unit}:")
    for entry in vocab[unit]:
        print(f" - {entry['word']} : {entry['meaning']}")

def search_word():
    """
    Search for a word across all units and display matches.
    """
    vocab = load_vocab()
    search_term = input("Enter word to search: ").strip()
    results = search_word_global(vocab, search_term)

    if results:
        print(f"\n Found '{search_term}' in the following units:")
        for unit, word, meaning in results:
            print(f" - {unit}: {word} → {meaning}")
    else:
        print(" Word not found in any unit.")
