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
class Stack2:
    def __init__(self):
        self.data=[]
    def push(self,e):
        self.data.append(e)
    def pop(self):
        self.data.pop()
    def top(self):
        return self.data[-1]
    def display(self):
        print(self.data)
def transferData(data):
    s=Stack1()
    s2=Stack2()
    for i in range(len(data)):
        s.push(data[i])
    for j in range(s.length()):
        s2.push(s.pop())
    return s2.display()
if __name__=="__main__":
    print(transferData("123"))
