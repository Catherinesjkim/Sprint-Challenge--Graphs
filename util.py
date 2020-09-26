"""
Stack is an abstract data type. When we give an abstract data type a physical implementation, we refer to the implementation as a data structure. 

In any object-oriented programming language, the implementation of choice for an abstract data type such as a stack is the creation of a new class. The stack operations are implemented as methods. Further, to implement a stack, which is a collection of elements, it makes sense to utilize the power and simplicity of the primitive collections provided by Ptython. 

We will use a list. List class in Python provides an ordered collection mechanism and a set of methods. i.e. if we have the list [2,5,3,6,7,4], we need only to decide which end of the list will be considered the top of the stack and which will be the base. 

Once that decision is made, the operations can be implemented using the list methods such as append and pop. The stack implementation assumes that the end of the list will hold the top element of the stack. As the stack grows (as push operations occur), new items will be added on the end of the list. pop operations will manipulate that same end. 
"""
class Stack():
    
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
        
    def size(self):
        return len(self.stack)
    
    def tail(self):
        return self.stack[-1]
        