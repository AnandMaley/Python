import json
import os

def save_tasks(tasks):
    # with open("D:\Projects\Python\\tasks.txt","w") as file:
    #     file.write(str(tasks))
    path = os.path.join("D:", "Projects", "Python", "tasks.json")
    with open(path, "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    path = os.path.join("D:", "Projects", "Python", "tasks.json")
    if not os.path.exists(path):
        return {}
    if os.path.getsize(path) == 0:
        return {}
    with open(path, "r") as file:
        return json.load(file)

def list_tasks(tasks):
    print("tasks_id|tasks|status")
    for tasks_id,(ts,status) in tasks.items():
        print(f"{tasks_id}|{ts}|{status}")

def add_tasks(tasks):
    task_add = input("Enter the Task: ")
    id = int(max(tasks.keys())) + 1 if tasks else 1
    tasks.update({id:[task_add,"Not Done"]})
    save_tasks(tasks)

def delete_task(tasks):
    id = int(input("Enter the Id of the Task you want to DELETE: "))
    if id in tasks:
        tasks.pop(id)
        save_tasks(tasks)
    else:
        print("Task Id not found.")
    
def update_task(tasks):
    list_tasks(tasks)
    id = int(input("Enter the Id of the Task you want to UPDATE: "))
    if id not in tasks:
        print("Task Id not found.")
        return
    upts = tasks.get(id)
    col = int(input("Enter 1 for Updating Task or 2 for Updating Status :"))
    if col < 1 or col > 2:
        print("Invalid column choice.")
        return
    if col == 1:
        upts[col-1] = input("Enter the Task :")
    if col == 2:
        upts[col-1] = input("Enter the Status :")
    tasks.update({id:[upts[0],upts[1]]})
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    tasks = {int(k): v for k, v in tasks.items()}
    while True:
        print("Enter the Number and Press ENTER to perform the task:\n" \
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Delete Task\n"
        "4. Update Task\n"
        "5. Exit\n")
        choice = input("Enter the number: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        choice = int(choice)
        if choice >=1 and choice <= 5:
            print(f"You have selected option {choice}.")
            if choice == 1:
                add_tasks(tasks)
            elif choice == 2:
                list_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                update_task(tasks)
            else:
                save_tasks(tasks)
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()