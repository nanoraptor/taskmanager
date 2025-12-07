import os
import classes as t


print("Welcome to Task Manager!\n")
print("Please input the location of your *.json file that contains your tasks\n")

fname = ""
while True:
    f = input().strip()
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
    uinput = input().lower()
    if uinput == "exit":
        print("Exited the program successfully!")
        break
    elif uinput == "list":
        ## Implement list
        l = a.list_task()
        print("All the tasks in the given file:")
        for i in l:
            print(f"ID: {i[0]}, Task: {i[1]}\n")
    elif uinput == "add":
        u1 = input()
        a.add_task(u1)
    elif uinput == "update":
        u1 = ""
        while True:
            u1 = input()
            if (not u1.isnumeric()) and (not a.is_id(u1)):
                print("Please give a valid id!\n")
                continue
            else:
                break
        u1 = int(u1)
        u2 = input()
        a.update_task(u1, u2)
    elif uinput == "delete":
        u1 = ""
        while True:
            u1 = input()
            if (not u1.isnumeric()) and (not a.is_id(u1)):
                print("Please give a valid id!\n")
                continue
            else:
                break
        u1 = int(u1)
        a.delete_task(u1)
    elif uinput == "help":
        ## Implement help menu
        print("Help Menu:\n")
        print("type 'list to list all tasks\n")
        print("type 'add' to to add tasks\n")
        print("type 'update' to add tasks\n")
        print("type 'delete' to delete tasks\n")
        print("type 'help' to open this help menu\n")
    else:
        print("Please give a valid user input!\n")
        print("Type 'help' for more info\n")
