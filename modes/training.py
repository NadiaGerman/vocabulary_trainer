import time
from vocab_utils import load_vocab, clean_word, find_word_index

def training_mode():
    vocab = load_vocab()
    unit = input("Enter unit name to practice (e.g. unit_1): ").strip()

    if unit not in vocab or not vocab[unit]:
        print("⚠️ Unit does not exist or is empty.")
        return

    word_list = vocab[unit]

    print("\nDo you want to practice the full unit or a word range?")
    mode = input("Type 'full' or 'range': ").strip().lower()

    if mode == "range":
        start_word = clean_word(input("Enter start word: "))
        end_word = clean_word(input("Enter end word: "))

        start_index = find_word_index(word_list, start_word)
        end_index = find_word_index(word_list, end_word)

        if start_index == -1 or end_index == -1 or start_index > end_index:
            print("⚠️ Invalid range. Check that both words exist and are in order.")
            return

        word_list = word_list[start_index:end_index + 1]

    print("\n📖 Training begins! Press Enter to see the meaning...")
    for entry in word_list:
        print(f"\nWord: {entry['word']}")
        input("...")  # Wait for user
        print(f"Meaning: {entry['meaning']}")
        time.sleep(1)

    print("\n✅ Training session complete.")
