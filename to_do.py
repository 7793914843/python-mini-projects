
tasks = []


# Add Task
def add_task():
    task = input("Enter task: ")

    tasks.append(task)

    print("Task added successfully!")


# View Tasks
def view_tasks():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nYour Tasks:")

    for i in range(len(tasks)):
        print(i + 1, ".", tasks[i])


# Delete Task
def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    number = int(input("Enter task number to delete: "))

    if number >= 1 and number <= len(tasks):

        deleted_task = tasks.pop(number - 1)

        print("Task deleted:", deleted_task)

    else:
        print("Invalid task number.")


# Main Menu
while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
