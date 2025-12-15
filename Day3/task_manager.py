while True:
    print("1. Add a new task\n2. View all tasks\n3. View tasks by owner\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        with open("log_file1.txt", "a") as file:
            task_number = input("Enter task number: ")
            task_description = input("Enter task description: ")
            task_owner = input("Enter task owner: ")
            task_status = input("Enter task status: ")
            file.write("\n"+task_number+","+task_description +
                       ","+task_owner+","+task_status)
    elif choice == 2:
        try:
            file = open("log_file1.txt", "r")
            content = file.read()
            print(content)
            file.close()
        except FileNotFoundError:
            print("Log file not found.")

    elif choice == 3:
        owner = input("Enter task owner to filter: ")
        with open("log_file.txt", "r") as file:
            tasks = file.readlines()   # Alice
            flag = False
            for i in range(-1, -len(tasks)-1, -1):
                task = tasks[i].split(",")    # alice
                if task[2].lower() == owner.lower():
                    print("Owner:", task[2], "Status:", task[3])
                    flag = True
                    break
            if not flag:
                print("No tasks found for the owner:", owner)
    elif choice == 4:
        print("Exiting the program.")
        break
