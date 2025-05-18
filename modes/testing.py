from vocab_utils import load_vocab, clean_word

def testing_mode():
    vocab = load_vocab()
    unit = input("Enter unit name to test (e.g. unit_1): ").strip()

    if unit not in vocab or not vocab[unit]:
        print("⚠️ Unit does not exist or is empty.")
        return

    words = vocab[unit]
    total = len(words)
    correct = 0
    incorrect_answers = []

    print("\n🧪 Starting test... Type the Hebrew meaning for each English word.")

    for entry in words:
        answer = input(f"{entry['word']}: ").strip().lower()
        correct_meaning = entry['meaning'].strip().lower()

        if answer == correct_meaning:
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong! The correct meaning is: {entry['meaning']}")
            incorrect_answers.append((entry['word'], entry['meaning']))

    print("\n📊 Test complete!")
    print(f"Score: {correct} out of {total} ({(correct / total) * 100:.1f}%)")

    if incorrect_answers:
        print("\n❗ Words you got wrong:")
        for word, meaning in incorrect_answers:
            print(f"- {word}: {meaning}")
