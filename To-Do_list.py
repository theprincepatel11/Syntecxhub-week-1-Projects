# To-Do List Applicationcle

tasks = []

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 2:
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")