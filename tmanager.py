import os
import classes as t


print("Welcome to Task Manager!\n")
print("Please input the location of your *.json file that contains your tasks\n")

fname = ""
while True:
    f = input(">> ").strip()
    # f = "test.json"
    if not (os.path.exists(f)):
        print("Please enter a valid file path")
    else:
        if f[-5:] != ".json":
            print("Please enter a valid file path")
            continue
        fname = f
        break

a = t.Task(fname)
print(f"\nSuccessfully opened file: {fname} and loaded all tasks\n")
print('type "help" for opening help menu\n')

while True:
    uinput = input("> ").lower()
    if uinput == "exit":
        print("Exited the program successfully!")
        break
    elif uinput == "list":
        ## Implement list
        l = a.list_task()
        print("\nAll the tasks in the given file:")
        for i in l:
            print(f"ID: {i[0]}, Task: {i[1]}")
        print()
    elif uinput == "add":
        u1 = input(">> ")
        a.add_task(u1)
        print("Task added successfully\n")
    elif uinput == "update":
        u1 = ""
        while True:
            u1 = input(">> ")
            if u1.isnumeric() and a.is_id(int(u1)):
                break
            else:
                print("Please give a valid id\n")
        u1 = int(u1)
        u2 = input(">>> ")
        a.update_task(u1, u2)
        print("Task updated successfully\n")
    elif uinput == "delete":
        u1 = ""
        while True:
            u1 = input(">> (ID) ")
            if u1.isnumeric() and a.is_id(int(u1)):
                break
            else:
                print("Please give a valid id\n")
        u1 = int(u1)
        a.delete_task(u1)
        print("Task deleted successfully\n")
    elif uinput == "help":
        ## Implement help menu
        print("\nHelp Menu:")
        print("type 'list' to list all tasks")
        print("type 'add' to to add tasks")
        print("type 'update' to add tasks")
        print("type 'delete' to delete tasks")
        print("type 'exit' to exit the program")
        print("type 'help' to open this help menu\n")
    else:
        print("Please give a valid user input!\n")
        print("Type 'help' for more info\n")
