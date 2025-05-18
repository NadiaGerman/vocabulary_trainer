# main.py
# This is the entry point of the Vocabulary Trainer app.
# It provides a menu for the user to choose between Editing, Training, and Testing modes.

# Import functions for each mode from their respective files
from modes.editing import editing_mode
from modes.training import training_mode
from modes.testing import testing_mode

def main():
    """
    Main function that displays a simple text-based menu.
    The user chooses between Editing, Training, Testing, or Exit.
    """
    while True:
        # Print the menu options
        print("\n Vocabulary Trainer")
        print("-------------------------")
        print("1. Editing Mode")   # Allows adding/updating/deleting words
        print("2. Training Mode")  # Practice words with delayed meaning reveal
        print("3. Testing Mode")   # Take a one-time quiz for a unit
        print("4. Exit")           # Quit the app

        # Get user choice
        choice = input("Choose an option (1–4): ").strip()

        # Run the selected mode
        if choice == "1":
            editing_mode()  # Calls the editing interface
        elif choice == "2":
            training_mode()  # Starts training session
        elif choice == "3":
            testing_mode()  # Starts test session
        elif choice == "4":
            print(" Goodbye!")
            break  # Exit the while loop and end the app
        else:
            print(" Invalid choice. Try again.")  # Invalid input handling

# Start the app by calling the main function
if __name__ == "__main__":
    main()
