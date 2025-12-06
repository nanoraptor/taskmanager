class Task:
    def __init__(self, path):
        self.task = []
        self.path = path
        with open(path, "r") as file:
            self.task = file.readlines()
        self.task = list(map(str.strip, self.task))
        for i in self.task:
            i = i.split(" _ ")
        for i in self.task:
            i[0] = int(i[0])
        temp = []
        for i in self.task:
            temp.append(i[0])
        self.id = max(temp) + 1

    def add_task(self, tak):
        tak = str(tak)
        self.task.append([self.id, tak])
        self.id += 1
        with open(self.path, "w") as file:
            ttk = self.task
            for i in ttk:
                i = str(i[0]) + " _ " + i[1] + "\n"
            file.writelines(ttk)

    def update_task(self, pid, tak):
        for i in range(len(self.task)):
            if self.task[i][0] == pid:
                self.task[i][1] = tak
        with open(self.path, "w") as file:
            ttk = self.task
            for i in ttk:
                i = str(i[0]) + " _ " + i[1] + "\n"
            file.writelines(ttk)

    def delete_task(self, pid):
        for i in range(len(self.task)):
            if self.task[i][0] == pid:
                self.task.pop(i)
        with open(self.path, "w") as file:
            ttk = self.task
            for i in ttk:
                i = str(i[0]) + " _ " + i[1] + "\n"
            file.writelines(ttk)

    def list_task(self):
        return self.task


# ## The transformation I need to apply
# ## First the int has to be converted to string
# ## then add " _ " after that the tak
# for i in self.task:
#     i = str(i[0]) + " _ " + i[1]
# # review usage of the anyonymous function lambda here
# self.task = list(map(lambda x: x.strip(" _ "),self.task))
