def save_tasks(tasks):
    with open("D:\Projects\Python\\tasks.txt","w") as file:
        file.write(str(tasks))

def load_tasks():
    # Storing tasks
    with open("D:\Projects\Python\\tasks.txt","r") as file:
        tasks = file.read()
        return dict(tasks)

def list_tasks(tasks):
    print("tasks_id|tasks|status")
    for tasks_id,(ts,status) in tasks.items():
        print(f"{tasks_id}|{ts}|{status}")

def add_tasks(tasks):
    task_add = input("Enter the Task: ")
    tasks.update({len(tasks):[task_add,"Not Done"]})

def delete_task(tasks):
    id = int(input("Enter the Id of the Task you want to DELETE: "))
    tasks.pop(id)

def update_task(tasks):
    list_tasks(tasks)
    id = int(input("Enter the Id of the Task you want to UPDATE: "))
    upts = tasks.get(id)
    col = int(input("Enter 1 for Updating Task or 2 for Updating Status :"))
    if col == 1:
        upts[col-1] = input("Enter the Task :")
    if col == 2:
        upts[col-1] = input("Enter the Status :")
    tasks.update({id:[upts[0],upts[1]]})
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("Enter the Number and Press ENTER to perform the task:\n" \
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Delete Task\n"
        "4. Update Task\n"
        "5. Exit\n")
        choice = int(input("Enter the number: "))
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
            print("Invalid option selected. Please try again.")
            main()  # Restart the process for valid input

if __name__ == "__main__":
    main()