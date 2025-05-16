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
    pass

def list_tasks():
    task_num = 1
    for i in tasks:
        print(f"{task_num}. {i}")
        task_num += 1

def check_off_task():
    clear_screen()
    task_num = 1
    numbered_tasks = []
    for i in tasks:
        numbered_tasks.append(f"{task_num}. {i}")
        task_num += 1
        print(numbered_tasks[-1])
    task_checkoff = int(input("Choose the task to checkoff by number: "))
    for i in range(len(numbered_tasks)):
        if str(task_checkoff) == numbered_tasks[i][0]:
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
                add_task()
            elif int_choice == 2:
                check_off_task()
            elif int_choice == 4:
                list_tasks()
            else:
                clear_screen()
                print("Choice not found...")
                pass
        except ValueError:
            clear_screen()
            print("Choice not found...")
            pass