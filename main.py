# TODO APP made by Deep
import random
import json

items = []


def main():
    while True:
        print("1. Add an Item.")
        print("2. View Items.")
        print("3. Delete an Item.")
        print("4. Save to a file.")
        print("5. Read from a file.")
        print("6. Clear all lists.")
        print("7. Exit.")
        choice = input("Enter your choice:")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            save_file()
        elif choice == "5":
            read_file()
        elif choice == "6":
            clear_items()
        elif choice == "7":
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


def save_file():
    filename = input("Enter file name:")
    try:
        file = open(filename+".json", "w")
        file.write(str(json.dumps(items)))
        file.close()
        print("Saved successful.")
    except Exception as error:
        print(error)
    finally:
        return


def clear_items():
    items.clear()


def read_file():
    filename = input("Enter file name:")
    try:
        file = open(filename+".json", "r")
        file_content = file.read()
        clear_items()
        global items
        items = eval(file_content)
        print("File loaded successful.")
    except Exception as error:
        print(error)
    finally:
        return


if __name__ == "__main__":
    main()

