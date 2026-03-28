
# To-Do CLI App

import json
import os


# -------load tasks------
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json" , "r") as f:
            return json.load(f)
    
    return []


# -------save tasks-------
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent = 4)


#-----------add task--------
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Tasks Added!!")


#------view tasks---------
def view_tasks(tasks):
    if not tasks:
        print("Tasks not found!!")
        return
    
    print("\n Your Tasks: ")
    for i, t in enumerate(tasks, start = 1):
        status = "✔" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")


#----------mark test done----------
def mark_done(tasks):
    if not tasks:
        print("No task to mark!!")
        return
    
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to mark done: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(" Tasks marked as done!")
        
        else:
            print("Invalid Task number")

    except ValueError:
        print("Invalid Input!!")

#-----delete tasks-----
def delete_tasks(tasks):
    if not tasks:
        print("No tasks to delete!!")
        return
    
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        
        else:
            print("Invalid Task number!!")

    except ValueError:
        print("Invalid Input!!")

#-----main program---------
def main():
    tasks = load_tasks()

    while True:
        print("##----TO-DO App------")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Done Task")
        print("4. Delete Task")
        print("5. Exit ")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2": 
            view_tasks(tasks) 
        elif choice == "3": 
            mark_done(tasks) 
        elif choice == "4": 
            delete_tasks(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks Saved. GoodBye!!")
            break
        else:
            print("Invalid choice. Please try again!!")

if __name__ == "__main__":
    main()

