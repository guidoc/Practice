"""
Sum 2 integers stored into linked lists
Ex:
n1 = 8562 -->> l1 = 2 -> 6 -> 5 -> 8
n2 = 7493 -->> l2 = 3 -> 9 -> 4 -> 7

Expected rlt:
n3 = 16055 -->> l3 = 5 -> 5 -> 0 -> 6 -> 1
"""


### LINKED LIST IMPLEMENTATION
class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList(object):
    def __init__(self, root):
        self.root = root
        self.lastNode = root

    def push(self, value):
        newNode = node(value)
        self.lastNode.next = newNode


# create linked list for node1
n0 = reversed([8,5,6,2])
n1 = reversed([7,4,9,3])
for listId, listVals in enumerate([n0,n1]):
    for valId, val in enumerate(listVals):
        # create the nodes
        strToExec1 = 'node' + str(listId) + '_' + str(valId) + ' = node(' + str(val) + ')'
        print strToExec1
        exec strToExec1

        # link previous node to the current
        if valId > 0:
            strToExec2 = 'node' + str(listId) + '_' + str(valId-1) + '.next = node' + str(listId) + '_' + str(valId)
            print strToExec2
            exec strToExec2


def sumLinkedListRecursive(node0, node1, carryover):
    # base case
    if (node0 == None and node1 == None):
        if carryover == 0:
            return None
        else:
            return node(carryover)

    elif node0 == None:
        val0 = 0
        val1 = node1.value
    elif node1 == None:
        val0 = node0.value
        val1 = 0
    else:
        val0 = node0.value
        val1 = node1.value

        currSum = val0 + val1 + carryover
        if currSum >= 10:
            currSum -= 10
            carryover = 1
        else: carryover = 0

        newNode2 = node(currSum)
        newNode2.next = sumLinkedListRecursive(node0.next, node1.next, carryover)
        return newNode2

# create function to sum them
def sumLinkedLists(node0, node1):
    """
    sum the linked lists and store the result in a new one
    :param node0:
    :param node1:
    :return: nodeSum
    """
    thisNode0 = node0
    thisNode1 = node1
    rootSum = node0.value + node1.value
    add1 = False
    if rootSum >= 10:
        rootSum -= 10
        add1 = True
    rootNode = node(rootSum)
    print "pushed", rootSum
    thisNode2 = rootNode

    while (thisNode0 or thisNode1):
        prevNode0 = thisNode0
        prevNode1 = thisNode1
        if thisNode0.next:
            thisNode0 = thisNode0.next
            val0 = thisNode0.value
        else:
            val0 = 0
        if thisNode1.next:
            thisNode1 = thisNode1.next
            val1 = thisNode1.value
        else:
            val1 = 0

        # compute the value to add
        val2 = val0 + val1 + int(add1)
        add1 = False
        if val2 >= 10:
            val2 -= 10
            add1 = True

        # add it to the list
        newNode = node(val2)
        print "pushed", val2
        thisNode2.next = newNode
        thisNode2 = thisNode2.next

    # check if there is 1 more node to add
    if add1:
        newNode = node(1)
        thisNode2.next = newNode
        print "pushed", 1

    # return
    return rootNode


#rn = sumLinkedLists(node0_0, node1_0)
rnRec = sumLinkedListRecursive(node0_0, node1_0, 0)


# print the list
node2 = rnRec
while node2.next:
    print node2.value
    node2 = node2.next
print node2.value

