class Task:
    def __init__(self, name):
        self.name = name
        self.id = 0
        self.task = []

    def add_task(self, tak):
        self.task.append([self.id, tak])
        self.id += 1

    def update_task(self, id, tak):
        for i in range(len(self.task)):
            if self.task[i][0] == id:
                self.task[i][1] = tak

    def delete_task(self, id):
        for i in range(len(self.task)):
            if self.task[i][0] == id:
                self.task.pop(i)

    def list_task(self):
        return self.task
