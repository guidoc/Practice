"""
3 1 Describe how you could use a single array to implement three stacks
"""

# how to implement a stack using lists
class stack(object):
    def __init__(self):
        self.vals = []

    def push(self, value):
        self.vals.append(value)

    def pop(self):
        return self.vals.pop()

    def peek(self):
        return self.vals[-1]

# how to implement a stack using nodes
class node(object):
    def __init__(self, value):
        self.value = value
        self.prevNode = None

class stack2(object):
    def __init__(self, value):
        self.currNode = node(value)

    def push(self, value):
        newNode = node(value)
        newNode.prevNode = self.currNode
        self.currNode = newNode

    def pop(self):
        currNodeVal = self.currNode.value
        currNode = self.currNode
        del(currNode)
        print self.currNode.value
        self.currNode = self.currNode.prevNode
        return currNodeVal

    def peek(self):
        return self.currNode.value


### SOME TESTS ###
s = stack2(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print s.peek()
print s.pop()
print s.pop()
print s.pop()
print s.pop()








