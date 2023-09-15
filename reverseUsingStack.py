import os
class StackArray:
    def __init__(self):
        self.arr=[]
    def push(self,s):
        self.arr.append(s)
    def isEmpty(self):
        return len(self.arr)==0
    def top(self):
        if self.isEmpty():
            print("stack is empty")
        return self.arr[-1]
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        return self.arr.pop()
def reverse(file):
    s=StackArray()
    original=open(file)
    for line in original:
        s.push(line.strip("\n"))
    original.close()
    output=open(file, 'W')
    while not s.isEmpty():
        output.write(s.pop()+"\n")
    output.close()
if __name__=="__main__":

    reverse()
