from vocab_utils import load_vocab, save_vocab, clean_word, find_word_index, ensure_unit_exists

def editing_mode():
    while True:
        print("\n📘 Editing Mode")
        print("1. Add word")
        print("2. Delete word")
        print("3. Update word")
        print("4. List words")
        print("5. Back to main menu")

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
            break
        else:
            print("Invalid choice. Try again.")

def add_word():
    vocab = load_vocab()
    unit = input("Enter unit name (e.g. unit_1): ").strip()
    ensure_unit_exists(vocab, unit)

    word = clean_word(input("Enter English word: "))
    meaning = input("Enter Hebrew meaning: ").strip()

    if find_word_index(vocab[unit], word) != -1:
        print("⚠️ Word already exists in this unit.")
        return

    vocab[unit].append({"word": word, "meaning": meaning})
    save_vocab(vocab)
    print(f"✅ '{word}' added to {unit}.")

def delete_word():
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab:
        print("⚠️ Unit does not exist.")
        return

    word = clean_word(input("Enter English word to delete: "))
    index = find_word_index(vocab[unit], word)

    if index == -1:
        print("⚠️ Word not found.")
        return

    confirm = input(f"Are you sure you want to delete '{word}'? (y/n): ").strip().lower()
    if confirm == "y":
        del vocab[unit][index]
        save_vocab(vocab)
        print(f"🗑️ '{word}' deleted from {unit}.")
    else:
        print("Deletion canceled.")

def update_word():
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab:
        print("⚠️ Unit does not exist.")
        return

    old_word = clean_word(input("Enter word to update: "))
    index = find_word_index(vocab[unit], old_word)

    if index == -1:
        print("⚠️ Word not found.")
        return

    new_word = clean_word(input("Enter new word: "))
    new_meaning = input("Enter new meaning: ").strip()

    vocab[unit][index] = {"word": new_word, "meaning": new_meaning}
    save_vocab(vocab)
    print(f"🔁 '{old_word}' updated to '{new_word}' with meaning '{new_meaning}'.")

def list_words():
    vocab = load_vocab()
    unit = input("Enter unit name: ").strip()

    if unit not in vocab or not vocab[unit]:
        print("⚠️ Unit is empty or does not exist.")
        return

    print(f"\n📋 Words in {unit}:")
    for entry in vocab[unit]:
        print(f" - {entry['word']} : {entry['meaning']}")
