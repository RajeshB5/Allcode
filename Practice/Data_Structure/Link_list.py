class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.head = new_node

    def printList(self):
        elements = []
        cur_node = self.head
        while cur_node.next:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        elements.append(cur_node.data)
        print(elements)

    def deleteNode(self, data):
        cur_node = self.head
        if cur_node.data == data:
            self.head = cur_node.next
            return
        while cur_node.next:
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next
        print(data, 'is not present in linked list')


sl = LinkList()
sl.insert(5)
sl.insert(2)
sl.insert(242)
sl.printList()
sl.deleteNode(25)
sl.printList()
