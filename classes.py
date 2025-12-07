class Task:
    def __init__(self, path):
        self.task = []
        self.path = path
        with open(path, "r") as file:
            self.task = file.readlines()
        self.task = list(map(str.strip, self.task))
        for i in range(len(self.task)):
            self.task[i] = self.task[i].strip().split(" _ ")
        for i in range(len(self.task)):
            self.task[i][0] = int(self.task[i][0])
        self.idl = []
        for i in self.task:
            self.idl.append(i[0])
        try:
            self.id = max(self.idl) + 1
        except ValueError:
            pass

    def add_task(self, tak):
        ## figure out a way to handle empty tasks
        tak = str(tak)
        self.task.append([self.id, tak])
        self.idl.append(self.id)
        self.id += 1
        with open(self.path, "w") as file:
            ttk = self.task[:]
            for i in range(len(ttk)):
                ttk[i] = str(ttk[i][0]) + " _ " + ttk[i][1] + "\n"
            file.writelines(ttk)

    def update_task(self, pid, tak):
        for i in range(len(self.task)):
            if self.task[i][0] == pid:
                self.task[i][1] = str(tak)
        with open(self.path, "w") as file:
            ttk = self.task[:]
            for i in range(len(ttk)):
                ttk[i] = str(ttk[i][0]) + " _ " + ttk[i][1] + "\n"
            file.writelines(ttk)

    def delete_task(self, pid):
        for i in range(len(self.task)):
            if self.task[i][0] == pid:
                self.task.pop(i)
                break
        self.idl.remove(self.id)
        with open(self.path, "w") as file:
            ttk = self.task[:]
            for i in range(len(ttk)):
                ttk[i] = str(ttk[i][0]) + " _ " + ttk[i][1] + "\n"
            file.writelines(ttk)

    def is_id(self, pid):
        if pid in self.idl:
            return True
        else:
            return False

    def list_task(self):
        return self.task


# ## The transformation I need to apply
# ## First the int has to be converted to string
# ## then add " _ " after that the tak
# for i in self.task:
#     i = str(i[0]) + " _ " + i[1]
# # review usage of the anyonymous function lambda here
# self.task = list(map(lambda x: x.strip(" _ "),self.task))
