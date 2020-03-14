class MainStack:
    def __init__(self):
        self.items1=[]
    def push(self,num):
        self.items1.append(num)
    def pop(self):
        if self.items1!=[]:
            return self.items1.pop()  
    def peek(self):
        if self.items1!=[]:
            return self.items1[-1]              
class MaxStack:
    def __init__(self):
        self.items2=[]
    def push(self,num):
        self.items2.append(num)
    def pop(self):
        if self.items2!=[]:
            self.items2.pop()  
    def peek(self):
        if self.items2!=[]:
            return self.items2[-1]
mainstack=MainStack()
maxstack=MaxStack()            
N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))
maxstack.push(float("-inf")) 
for i in l:
    if i[0]==1:
        mainstack.push(num=i[1])
        if mainstack.peek()>=maxstack.peek():
            maxstack.push(mainstack.peek())
    if i[0]==2:
      if mainstack.pop()==maxstack.items2[-1]:
        maxstack.pop()
    if i[0]==3:
        print(maxstack.peek())