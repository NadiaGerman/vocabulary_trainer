# testing.py
# This module allows the user to take a quiz for a selected unit

from vocab_utils import load_vocab, normalize_text, get_unit_choice

## Function: testing_mode
## Purpose: User is tested on vocabulary from a selected unit
## Returns: None
def testing_mode() -> None:
    vocab = load_vocab()  ## Load vocabulary from file
    unit = get_unit_choice()  ## Prompt for unit selection

    if unit not in vocab or not vocab[unit]:
        print(" Unit does not exist or is empty.")
        return

    words = vocab[unit]  ## Retrieve words from selected unit
    total = len(words)  ## Total number of questions
    correct = 0  ## Counter for correct answers
    incorrect_answers = []  ## Track incorrect answers

    print("\n Starting test... Type the Hebrew meaning for each English word.")

    for entry in words:
        answer = input(f"{entry['word']}: ").strip()
        ## Normalize both expected and user input
        if normalize_text(answer) == normalize_text(entry['meaning']):
            print(" Correct!")
            correct += 1
        else:
            print(f" Wrong! The correct meaning is: {entry['meaning']}")
            incorrect_answers.append((entry['word'], entry['meaning']))

    print("\n Test complete!")
    print(f"Score: {correct} out of {total} ({(correct / total) * 100:.1f}%)")

    if incorrect_answers:
        print("\n Words you got wrong:")
        for word, meaning in incorrect_answers:
            print(f"- {word}: {meaning}")
