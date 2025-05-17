import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(no_clear):
    menu = ["Press 1 to add task",
            "Press 2 check off task",
            "Press 3 to remove task",
            "Press 4 to list tasks",
            "Type \"Menu\" to display menu",
            "Type \"Exit\" to exit app", ""]
    if no_clear == 1:
        for i in menu:
            print(i)
    else:
        clear_screen()
        for i in menu:
            print(i)

tasks = []
def add_task():
    clear_screen()
    while True:
        task = input("Enter your task or \"back\": ")
        if task.lower() == "back":
            clear_screen()
            break
        elif task in tasks:
            clear_screen()
            print(f"Error: '{task}' is already a task!")
            pass
        else:
            tasks.append(task)
            clear_screen()
            print("Your task has been added!")
            break

def remove_task():
    loop = True
    if len(tasks) < 1:
        print("No tasks to remove! Add some by pressing 1")
    else:
        while loop:
            print("Your Tasks:")
            task_num = 1
            numbered_tasks = []
            for i in tasks:
                numbered_tasks.append(f"{task_num}. {i}")
                print(numbered_tasks[-1])
                task_num += 1
                # Placing the print statement after the remove method removed an item in tasks
                # before the appropriate print statement could be run, resulting in indexing issues
            task_remove = input("Choose the task to remove by number or \"back\": ")
            if task_remove.lower() == "back":
                display_menu(0)
                loop = False
            else:
                for i in range(len(numbered_tasks)):
                    if task_remove == numbered_tasks[i][0]:
                        clear_screen()
                        print(f"'{tasks[i]}' has been removed from your task list!")
                        tasks.remove(tasks[i])
                        loop = False
                    else:
                        clear_screen()
                        print("Invalid choice, choose a task number!")
                        pass
                    
def list_tasks():
    if len(tasks) < 1:
        print("No tasks to list! Add some by pressing 1")
    else:
        print("Your Tasks:")
        task_num = 1
        for i in tasks:
            print(f"{task_num}. {i}")
            task_num += 1

def check_off_task():
    loop = True
    if len(tasks) < 1:
        print("No tasks to check off! Add some by pressing 1")
    else:
        while loop:
            print("Tasks:")
            task_num = 1
            numbered_tasks = []
            for i in tasks:
                numbered_tasks.append(f"{task_num}. {i}")
                print(numbered_tasks[-1])
                task_num += 1
            nums = []
            for i in numbered_tasks:
                nums.append(i[0])
            task_checkoff = input("Choose the task to checkoff by number or \"back\": ")
            if task_checkoff.lower() == "back":
                display_menu(0)
                loop = False
            elif task_checkoff in nums:
                for i in range(len(numbered_tasks)):
                    if task_checkoff == numbered_tasks[i][0]:
                        if "✅" in tasks[i]:
                            clear_screen()
                            print("This task is already checked off, great job!")
                            pass
                        elif not "✅" in tasks[i]:
                            clear_screen()
                            print(f"Congratulations on completing your '{tasks[i]}' task!")
                            tasks[i] = tasks[i] + " ✅"
                            loop = False
                        else:
                            clear_screen()
                            print("Invalid choice, choose a task number!")
                            pass
            else:
                clear_screen()
                print("Invalid choice, choose a task number!")
                pass


print("Welcome To Your Todo List!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
display_menu(1)

while True:
    choice = input("Choose an option (1 - 4), \"Exit\" or \"Menu\": ")
    if choice.lower() == "exit":
        clear_screen()
        print("Are you sure you want to exit?")
        exit_choice = input("Press \"Y\" or \"N\": ")
        if exit_choice.lower() == "y":
            clear_screen()
            print("Exiting program...goodbye")
            exit()
        else:
            clear_screen()
            pass
    elif choice.lower() == "menu":
        display_menu(0)
    else:
        try:
            int_choice = int(choice)
            if int_choice == 1:
                clear_screen()
                add_task()
            elif int_choice == 2:
                clear_screen()
                check_off_task()
            elif int_choice == 3:
                clear_screen()
                remove_task()
            elif int_choice == 4:
                clear_screen()
                list_tasks()
            else:
                clear_screen()
                print("Choice not found...")
                pass
        except ValueError:
            clear_screen()
            print("Choice not found...")
            pass