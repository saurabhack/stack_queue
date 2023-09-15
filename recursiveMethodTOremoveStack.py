class Stack1:
    def __init__(self):
        self.data=[]
    def push(self,e):
        return self.data.append(e)
    def pop(self):
        return self.data.pop()
    def top(self):
        return self.data[-1]
    def length(self):
        return len(self.data)


