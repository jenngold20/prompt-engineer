# create a tool in python to organize pending task list

def add_task(task):
    with open("tasks.txt", "a") as task_file:
        task_file.write(f"{task}\n")    
        print("Task added successfully!")
        task_file.close()

def view_tasks():
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
        if len(tasks) == 0:
            print("No pending tasks.")

def remove_task(task):
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
        task_file.close()
    with open("tasks.txt", "w") as task_file:
        for t in tasks:
            if t.strip("\n") != task:
                task_file.write(t)
        task_file.close()
        print("Task removed successfully!")

def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
           






