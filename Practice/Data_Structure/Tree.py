class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left = left_child
        self.right = right_child


def insert(parent, child):
    if parent.data < child.data:
        if parent.right:
            insert(parent.right, child)
        else:
            parent.right = child
    if parent.data > child.data:
        if parent.left:
            insert(parent.left, child)
        else:
            parent.left = child

def printTree(node, order=2):
    if order == 1:
        print(node.data)
    if node.left:
        printTree(node.left, order)
    if order == 2:
        print(node.data)
    if node.right:
        printTree(node.right, order)
    if order == 3:
        print(node.data)

def findElement(node, data):
    if node is None:
        return False
    if node.data == data:
        return True
    if findElement(node.left, data):
        return True
    if findElement(node.right, data):
        return True
    return False


root = Node(5)
insert(root, Node(1))
insert(root, Node(25))
insert(root, Node(4))
insert(root, Node(17))
insert(root, Node(9))
printTree(root)#, int(input("Print in order for pre-order = 1, in-order = 2, post-order = 3")))
if findElement(root, 9):#, int(input('Enter the value to find')):
    print('Present')
else:
    print('Not Present')
