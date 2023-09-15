class ArrayQueue:
    deafault_capacity=10
    def __init__(self):
        self.data=[None]*ArrayQueue.deafault_capacity
        self.front=0
        self.size=0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        if self.is_empty():
            print("this queue is empty")
        return self.data[self.front]
    def dequeue(self):
        if self.is_empty():
            print("this Queue is empty")
        ans=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return ans
    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avia=(self.front+self.size)%10
        self.data[avia]=e
        self.size+=1
    def resize(self,cap):
        old=self.data
        self.data=[None]*cap
        walk=self.front
        for i in range(len(old)):
            self.data[i]=old[walk]
            walk=(walk+1)%len(old)
        self.front=0
    def display(self):
        for i in range(self.front,self.size+1):
            print(self.data[i])

s=ArrayQueue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.dequeue()
s.display()