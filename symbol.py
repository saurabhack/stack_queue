class StackArray:
    def __init__(self):
        self.data = []

    def push(self, d):
        self.data.append(d)

    def is_empty(self):
        return len(self.data) == 0

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        return self.data.pop()

def macthed(exp):
    left="({["
    right=")}]"
    s=StackArray()
    for c in exp:
        if c in left:
            s.push(c)
        elif c in right:
            if s.is_empty():
                return False
            if right.index(c) != left.index(s.pop()):
                return False # mismatched
    return s.is_empty()
print(macthed("({[]})"))
