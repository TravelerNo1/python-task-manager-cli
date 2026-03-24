from task import Task
from storage import load_tasks, save_tasks


def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append(Task(title))
    print("Task added successfully!")


def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "Completed" if task.done else "Uncompleted"
        print(f"{i + 1}. [{status}] {task.title}")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark as Completed")
        print("4. Delete Task")
        print("5. Edit Task")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index].done = True
                print("Task marked as completed.")
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == "4":
            show_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task deleted: {removed.title}")
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == "5":
            show_tasks(tasks)
            index = int(input("Enter task number to edit: ")) - 1
            if 0 <= index < len(tasks):
                new_title = input("Enter new task title: ")
                tasks[index].title = new_title
                print("Task updated successfully.")
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == "0":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()