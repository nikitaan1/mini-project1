

def app_menu():


    while True:
        print("\nWelcome to the To-Do List App!")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("Enter a number from the menu: (1-5) ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            competed_task()
        elif choice == '4':
            competed_task()
        elif choice == '5':
            break

tasks = []

def add_task():
    
    while True:
        new_task = input("Add a new task: ")
        tasks.append(tasks)
        print("Task added successfully!")

        more_tasks = input("Would you like to add another task? (yes/no)")
        if more_tasks.lower() != 'yes':
            break
        


def view_task():

        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")


def competed_task():
    pass

def delete_task():
    
    while True:

        remove_task = input("Type the name of the task that you want to remove: ")
        tasks.remove(remove_task)

        another_removal = input("Is there any other task that you want to remove? (yes/no): ")
        if another_removal != 'yes':
            break

app_menu()
    