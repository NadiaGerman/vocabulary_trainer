import time
from vocab_utils import load_vocab, clean_word, find_word_index

def training_mode():
    """
    Allow the user to practice vocabulary words by unit.
    Options include practicing the entire unit or a range of words.
    Each word is shown with a delay before revealing its meaning.
    """
    vocab = load_vocab()
    unit = input("Enter unit name to practice (e.g. unit_1): ").strip()

    # Check if unit exists and is not empty
    if unit not in vocab or not vocab[unit]:
        print(" Unit does not exist or is empty.")
        return

    word_list = vocab[unit]

    # Ask user how they want to practice
    print("\nDo you want to practice the full unit or a word range?")
    mode = input("Type 'full' or 'range': ").strip().lower()

    # If "range", ask for start and end words
    if mode == "range":
        start_word = clean_word(input("Enter start word: "))
        end_word = clean_word(input("Enter end word: "))

        # Find indexes for range slicing
        start_index = find_word_index(word_list, start_word)
        end_index = find_word_index(word_list, end_word)

        if start_index == -1 or end_index == -1 or start_index > end_index:
            print(" Invalid range. Make sure both words exist and are in order.")
            return

        # Slice list to selected range
        word_list = word_list[start_index:end_index + 1]

    # Begin training session
    print("\n Training begins! Press Enter to see the meaning...")

    for entry in word_list:
        print(f"\nWord: {entry['word']}")
        input("...")  # Wait for user confirmation
        print(f"Meaning: {entry['meaning']}")  # Reveal meaning
        time.sleep(1)  # Small delay before next word

    print("\n Training session complete.")
