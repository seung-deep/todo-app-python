# TODO APP made by Deep
import random

items = []


def main():
    while True:
        print("1. Add an Item.")
        print("2. View Items.")
        print("3. Delete an Item.")
        print("4. Exit.")
        choice = input("Enter your choice:")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice.")


def generate_unique_id():
    seq = ['a', 'k', 't', 'j']
    random_seq_list = random.sample(seq, 3)
    random_seq = ""
    for x in random_seq_list:
        random_seq += x
    unique_id = f"{random_seq}{len(items)}"
    return unique_id


def add_item():
    item = input("Enter your list:")
    item_with_id = {
        "id": generate_unique_id(),
        "item": item
    }
    items.append(item_with_id)
    print("List add successful!")
    view_items()


def view_items():
    if len(items) == 0:
        print("No list found.")
        return
    print("ID       ITEM")
    print("-------------")
    for x in items:
        for key, value in x.items():
            if key == "id":
                print(value, ": ", end='')
            elif key == "item":
                print(value)


def delete_item():
    unique_id = input("Enter the list ID:")
    items_count = 0
    for x in items:
        for key, value in x.items():
            if key == "id" and value == unique_id:
                items.pop(items_count)
                print("List deleted successfully")
                return
        items_count += 1
    print("ID not matched.")


if __name__ == "__main__":
    main()

