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

while True:
    ## Implement help menu
    ## Implement using json module
    f1 = open(fname, "r+")
    print(f"\nSuccessfully opened {fname} file and loaded all tasks\n")
    break
