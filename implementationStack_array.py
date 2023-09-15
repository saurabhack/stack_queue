class StackArray:
    def __init__(self):
        self.data=[]
    def push(self,d):
        self.data.append(d)
    def __len__(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    def Top(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.data[-1]
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        return self.data.pop()
    def display(self):
        print(self.data)
if __name__=="__main__":
    da=StackArray()
    da.push(1)
    da.push(2)
    da.push(3)
    da.display()
    da.pop()
    da.display()
    print(da.Top())
    da.pop()
    da.pop()
    da.pop()