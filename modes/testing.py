from vocab_utils import load_vocab, clean_word

def testing_mode():
    """
    Start a one-time quiz session for a selected unit.
    Prompts the user for the Hebrew meaning of each English word.
    Tracks and displays the score and shows incorrect answers at the end.
    """
    vocab = load_vocab()
    unit = input("Enter unit name to test (e.g. unit_1): ").strip()

    # Check if the unit exists and has words
    if unit not in vocab or not vocab[unit]:
        print(" Unit does not exist or is empty.")
        return

    words = vocab[unit]
    total = len(words)
    correct = 0  # Count of correct answers
    incorrect_answers = []  # List of wrong answers to review later

    print("\n Starting test... Type the Hebrew meaning for each English word.")

    for entry in words:
        # Ask user to type the meaning
        answer = input(f"{entry['word']}: ").strip().lower()
        correct_meaning = entry['meaning'].strip().lower()

        # Compare user input to correct answer (case-insensitive)
        if answer == correct_meaning:
            print(" Correct!")
            correct += 1
        else:
            print(f" Wrong! The correct meaning is: {entry['meaning']}")
            incorrect_answers.append((entry['word'], entry['meaning']))

    # Test summary
    print("\n Test complete!")
    print(f"Score: {correct} out of {total} ({(correct / total) * 100:.1f}%)")

    # Show incorrect answers
    if incorrect_answers:
        print("\n Words you got wrong:")
        for word, meaning in incorrect_answers:
            print(f"- {word}: {meaning}")
