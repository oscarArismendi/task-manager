class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"name : {self.name}\nstatus: {self.status}\n"