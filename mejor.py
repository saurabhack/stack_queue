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
def matched(expr):
        lefty = "({[ "
        righty = ")}]"
        S = StackArray()
        for c in expr:
            if c in lefty:
                S.push(c) # push left delimiter on stack 9
            elif c in righty:
                if S.isEmpty():
                    return False # nothing to match with
                if righty.index(c) != lefty.index(S.pop()):
                    return False # mismatched
        return S.isEmpty()
matched("({[]})")