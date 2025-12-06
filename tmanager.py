import os
import classes as t


print("Welcome to Task Manager!\n")
print("Please input the location of your *.json file that contains your tasks\n")

fname = ""
while True:
    f = input().strip()
    if not (os.path.exists(f)):
        print("Please enter a valid file path")
    else:
        if f[-5:] != ".json":
            print("Please enter a valid file path")
            continue
        fname = f
        break

a = t.Task(fname)
print(f"\nSuccessfully opened {fname} file and loaded all tasks\n")
print('type "help" for opening help menu')

while True:
    uinput = input().lower()
    if uinput == "exit":
        print("Exited the program successfully!")
        break
    elif uinput == "list":
        ## Implement list
        pass
    elif uinput == "add":
        u1 = input()
        a.add_task(u1)
    elif uinput == "update":
        while True:
            u1 = input()
            if not u1.isnumeric():
                print("Please give a valid id!")
                continue
            else:
                break
        u1 = int(u1)
        u2 = input()
        a.update_task(u1, u2)
    elif uinput == "delete":
        u2 = int(input())
        a.delete_task(u2)
    elif uinput == "help":
        ## Implement help menu
        pass
    else:
        print("Please give a valid user input!")
