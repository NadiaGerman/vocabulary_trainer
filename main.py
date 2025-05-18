from modes.editing import editing_mode
from modes.training import training_mode
from modes.testing import testing_mode

def main():
    while True:
        print("\n🌟 Vocabulary Trainer")
        print("-------------------------")
        print("1. Editing Mode")
        print("2. Training Mode")
        print("3. Testing Mode")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            editing_mode()
        elif choice == "2":
            training_mode()
        elif choice == "3":
            testing_mode()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
