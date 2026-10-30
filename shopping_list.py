
# Part B: Shopping List Manager

# Start with an empty list
shopping_list = []

# Repeat the menu until the user chooses done
while True:
    print("\nShopping List Manager")
    print("add / remove / show / done")

    choice = input("What would you like to do? ").lower().strip()

    if choice == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(item, "has been added.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Your shopping list:")

        if shopping_list:
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please try again.")
