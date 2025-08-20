shopping_list = []


def display_menu():
    print("\nShopping List Manager")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")


if __name__ == "__main__":
    display_menu()
    choice = int(input("Enter your choice (1-4): "))

