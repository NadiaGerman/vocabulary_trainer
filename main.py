# main.py
# Entry point for the Vocabulary Trainer project
# Provides a menu to select different modes: Editing, Training, Testing

from modes.editing import editing_mode
from modes.training import training_mode
from modes.testing import testing_mode

## Function: main
## Purpose: Display main menu and route user input to appropriate modules
## Returns: None
def main() -> None:
    while True:
        ## Display the main menu options to the user
        print("\n Vocabulary Trainer")
        print("-------------------------")
        print("1. Editing Mode")
        print("2. Training Mode")
        print("3. Testing Mode")
        print("4. Exit")

        ## Take user input and route accordingly
        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            editing_mode()  ## Call editing mode
        elif choice == "2":
            training_mode()  ## Call training mode
        elif choice == "3":
            testing_mode()  ## Call testing mode
        elif choice == "4":
            print(" Goodbye!")  ## Exit message
            break
        else:
            print(" Invalid choice. Try again.")  ## Handle invalid input

## Entry point check
if __name__ == "__main__":
    main()
