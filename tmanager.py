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
    f1 = open(fname, "r+")
    print(f"\nSuccessfully opened {fname} file and loaded all tasks\n")
    break

# user input will be given like this ./tmanager.py <options> --optional <string>
# options can be add, update, list(done | todo | in-progress), mark(-in-progress | -done),
a = t.Task("a")
