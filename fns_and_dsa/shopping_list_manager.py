shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Exit")

display_menu()

choice = int(input("Enter your choice: "))


if choice == 1:
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")
elif choice == 2:
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")
elif choice == 3:
    print("Exiting... Goodbye!")

