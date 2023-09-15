class Queue:
    max_capacity=10
    def __init__(self):
        self.data=[None]*Queue.max_capacity
        self.front=0
        self.size=0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self.data)==0
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        ans=self.data[self.front]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size-=1
        return ans
    def enqueue(self,e):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        avi=(self.front+self.size)%len(self.data)
        self.data[avi]=e
        self.size+=1
    def resize(self,cap):
        old=self.data
        self.data=[None]*cap
        walk=self.front
        for i in range(len(old)):
            self.data[i]=old[walk]
            walk=(walk+1)%len(old)
        self.front=0
    def reverse(self):
        f=self.front
        l=self.size-1

        while(f<l and l>f):
            self.data[f],self.data[l]=self.data[l],self.data[f]
            f+=1
            l-=1
    def display(self):
        for i in range(self.front,self.size):
            print(self.data[i])


s=Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)

s.reverse()
s.display()

