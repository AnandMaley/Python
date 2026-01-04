 # Storing tasks
tasks = {}

def load_tasks():
    global tasks
    print("tasks_id|tasks|status")
    for tasks_id,(tn,status) in tasks.items():
        print(f"{tasks_id}|{tn}|{status}")

def add_tasks():
    task_add = input("Enter the Task: ")
    tasks.update({len(tasks):[task_add,"Not Done"]})

def delete_task():
    load_tasks()
    id = int(input("Enter the Id of the Task you want to DELETE: "))
    tasks.pop(id) 

def update_task():
    load_tasks()
    id = int(input("Enter the Id of the Task you want to UPDATE: "))
    upts = tasks.get(id)
    col = int(input("Enter 1 for Updating Task or 2 for Updating Status :"))
    if col == 1:
        upts[col-1] = input("Enter the Task :")
    if col == 2:
        upts[col-1] = input("Enter the Status :")
    tasks.update({id:[upts[0],upts[1]]})

def main():
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
                add_tasks()
            elif choice == 2:
                load_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                update_task()
            else:
                break
        else:
            print("Invalid option selected. Please try again.")
            main()  # Restart the process for valid input

if __name__ == "__main__":
    main()