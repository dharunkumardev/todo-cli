import os

def display_menu():
    print("\033[32mTodo App Menu:\033[0m")
    print("\033[32m1. Add a new task\033[0m")
    print("\033[32m2. View all tasks\033[0m")
    print("\033[32m3. Mark a task as complete\033[0m")
    print("\033[32m4. Delete a task\033[0m")
    print("\033[32m5. Exit\033[0m")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    if not os.path.exists("tasks.txt"):
        print("No tasks found!")
        return
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

def mark_complete(task_index):
    if not os.path.exists("tasks.txt"):
        print("No tasks found!")
        return
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if task_index <= len(tasks):
        tasks[task_index - 1] = tasks[task_index - 1].replace(" [ ]", " [x]")
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task index")

def delete_task(task_index):
    if not os.path.exists("tasks.txt"):
        print("No tasks found!")
        return
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if task_index <= len(tasks):
        del tasks[task_index - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task("[ ] " + task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
