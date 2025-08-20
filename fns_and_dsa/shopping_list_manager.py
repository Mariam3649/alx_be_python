shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

def view_list():
    print("Shopping List:", shopping_list)

if __name__ == "__main__":
    add_item("Apples")
    add_item("Milk")
    view_list()
    remove_item("Apples")
    view_list()
