import os
import classes as t


print("Welcome to Task Manager")
print("Please input the location of your *.json file that contains your tasks")
fname = input().strip().split(" ")
# if os.path.exists(fname):
# else;
#     print("Please enter a valid file path")
#
#
# while True:
#     break

# user input will be given like this ./tmanager.py <options> --optional <string>
# options can be add, update, list(done | todo | in-progress), mark(-in-progress | -done),
a = t.Task("a")
a.add_task("I can live my life!")
b = a.list_task()
for i in b:
    print(f"ID: {i[0]}, Task: {i[1]}")
