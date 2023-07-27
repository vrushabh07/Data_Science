# 232. Implement Queue using Stacks
''' To, Implement Queue using stacks we gonna need two stacks. 
-   I am declaring them as instack and outstack. instack contains value which will be pushed by user. 
-   outstack contains value of instack but in reverse order. So, the top value in instack will be boottom   value of outstack. 
-   After that in push operaton we will add value in instack. in pop operation we will get top value of out stack (which is bottom value of instack). 
-   In peek we wiil check return top value of outstack and if outstack is empty than the value of instack.
-   Empty function will return true or false that the stack are empty or not. '''

class MyQueue(object):

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        self.peek()
        return self.outStack.pop()
        

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[len(self.outStack)-1]

        

    def empty(self):
        return  not self.inStack and  not self.outStack
        


#obj = MyQueue()
#obj.push(x)
# param_2 = obj.pop()
#obj.peek()
# param_4 = obj.empty()
