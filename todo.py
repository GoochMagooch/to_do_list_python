import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task():
    pass

def check_off_task():
    pass

def remove_task():
    pass

def list_tasks():
    pass

def display_menu():
    menu = ["Press 1 to add task",
            "Press 2 check off task",
            "Press 3 to remove task",
            "Press 4 to list tasks",
            "Type \"Menu\" to display menu",
            "Type \"Exit\" to exit app", ""]
    for i in menu:
        print(i)

print("Welcome To Your Todo List!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
display_menu()

while True:
    choice = input("Choose an option (1 - 4), \"Exit\" or \"Menu\": ")
    if choice.lower() == "exit":
        clear_screen()
        print("Are you sure you want to exit?")
        exit_choice = input("Press \"Y\" or \"N\": ")
        if exit_choice.lower() == "y":
            exit()
        else:
            clear_screen()
            pass
    elif choice.lower() == "menu":
        clear_screen()
        display_menu()