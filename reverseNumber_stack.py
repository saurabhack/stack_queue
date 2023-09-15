class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,e):
        self.arr.append(e)
    def isEmpty(self):
        return len(self.arr)==0
    def pop(self):
        if self.isEmpty():
            print("stact is empty")
        return self.arr.pop()
    def length(self):
        return len(self.arr)
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.arr[-1]
    def display(self):
        print(self.arr)
def reverseName(name):
    s=Stack()
    for i in range(len(name)):
        s.push(name[i])
    name=""
    for j in range(s.length()):
        name+=s.pop()
    return name


def reverseNumber(num):
    s=Stack()
    if type(num)==int:
        d=""
        while num!=0:
            re=num%10
            s.push(str(re))
            d+=s.pop()
            num=num//10
        return int(d)
    else:
        for i in range(len(num)):
            s.push(num[i])
        num = " "
        for j in range(s.length()):
            num += s.pop()
        return num
if __name__=="__main__":
    print(reverseName("saurabh"))
    print(reverseNumber(123))



