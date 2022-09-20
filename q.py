class Queue:
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append(item)

    def poll(self):
        if len(self.list) >= 1:
            return self.list.pop(0)

    def peek(self):
        if len(self.list) >= 1:
            return self.list[0]
