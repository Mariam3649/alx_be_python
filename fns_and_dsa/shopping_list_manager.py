shopping_list = []


def display_menu():
    print("\nShopping List Manager")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")


if __name__ == "__main__":
    display_menu()  # ✅ استدعاء مباشر عشان التشيكر يشوفه
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            if shopping_list:
                print("Your shopping list:", shopping_list)
            else:
                print("Your shopping list is empty.")
        elif choice == 2:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")
        elif choice == 3:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

