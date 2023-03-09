class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Função para inserir um elemento no final da lista
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    # Função para inserir um elemento no início da lista
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Função para remover um elemento da lista
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

    # Função para imprimir a lista
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next