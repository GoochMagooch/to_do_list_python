import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

tasks = []
def add_task():
    clear_screen()
    task = input("Enter your task: ")
    tasks.append(task)
    clear_screen()
    print("Your task has been added!")

def remove_task():
    print("Your Tasks:")
    task_num = 1
    numbered_tasks = []
    for i in tasks:
        numbered_tasks.append(f"{task_num}. {i}")
        print(numbered_tasks[-1])
        task_num += 1
    # Figure out why int input converted to str passes the input as an index
    task_remove = input("Choose the task to remove by number: ")
    for i in range(len(numbered_tasks)):
        if task_remove == numbered_tasks[i][0]:
            print(f"{tasks[i]} has been removed from your task list!")
            tasks.remove(tasks[i])

def list_tasks():
    print("Your Tasks:")
    task_num = 1
    for i in tasks:
        print(f"{task_num}. {i}")
        task_num += 1

def check_off_task():
    task_num = 1
    numbered_tasks = []
    for i in tasks:
        numbered_tasks.append(f"{task_num}. {i}")
        task_num += 1
        print(numbered_tasks[-1])
    task_checkoff = input("Choose the task to checkoff by number: ")
    for i in range(len(numbered_tasks)):
        if task_checkoff == numbered_tasks[i][0]:
            print(f"Congratulations on completing your {tasks[i]} task!")
            tasks[i] = tasks[i] + " ✅"

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