def main():
    print("Enter the Number and Press ENTER to perform the task:\n" \
    "1. Add Task\n"
    "2. View Tasks\n"
    "3. Delete Task\n"
    "4. Exit\n")
    choice = int(input("Enter the number: "))
    if choice < 4 and choice > 0:
        print(f"You have selected option {choice}.")
    else:
        print("Invalid option selected. Please try again.")
        main()  # Restart the process for valid input

    # Storing tasks
    tasks = {}
if __name__ == "__main__":
    main()