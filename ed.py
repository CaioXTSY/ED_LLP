class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        current_node = self.head
        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node is not None and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def print_node_index(self, index):
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                print(current_node.data)
            current_node = current_node.next
            count += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()  # Out 1 2 3
my_list.print_node_index(1)  # Out 2