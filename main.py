import os

# ---------------- GLOBAL VARIABLES ----------------
tasks = []

# main.py ke folder ka path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Data file ka path
FILE_PATH = os.path.join(BASE_DIR, "history.txt")


# ---------------- LOAD TASKS ----------------
def load_task():
    try:
        with open(FILE_PATH, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


# ---------------- SAVE TASKS ----------------
def save_task():
    with open(FILE_PATH, "w") as file:
        print("saving to",FILE_PATH)
        for task in tasks:
            file.write(task + "\n")


# ---------------- ADD TASK ----------------
def add_task(task):
    tasks.append(task)
    save_task()
    print(f'"{task}" added successfully.')


# ---------------- SHOW TASKS ----------------
def show_task():
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# ---------------- DELETE TASK ----------------
def delete_task():
    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    show_task()

    try:
        task_no = int(input("\nEnter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            save_task()
            print(f'"{deleted}" deleted successfully.')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter numbers only.")


# ---------------- MARK COMPLETE ----------------
def mark_complete():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    show_task()

    try:
        task_no = int(input("\nEnter task number to mark complete: "))

        if 1 <= task_no <= len(tasks):

            if tasks[task_no - 1].startswith("✅"):
                print("Task is already completed.")
            else:
                tasks[task_no - 1] = "✅ " + tasks[task_no - 1]
                save_task()
                print("Task marked as completed.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter numbers only.")


# ---------------- LOAD SAVED TASKS ----------------
load_task()


# ---------------- MAIN MENU ----------------
while True:

    print("\n========== TO-DO APP ==========")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Complete")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        delete_task()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        show_task()

    elif choice == "5":
        save_task()
        print("Thank you for using To-Do App.")
        break

    else:
        print("Invalid choice. Please try again.")