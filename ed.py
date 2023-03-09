"""
Working on Terminal, Without GUI

import tkinter
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

def menu():
    dec = ("-" * 50)
    print(dec)
    print("1. Insert New Item")
    print("2. Remove an Item")
    print("3. Show All Items")
    print("5. Exit")
    print(dec)
    choice = int(input("Enter your choice: "))
    return choice

def main():
    my_list = LinkedList()
    while True:
        choice = menu()
        if choice == 1:
            item = input("Enter item: ")
            my_list.append(item)
        elif choice == 2:
            item = input("Enter item: ")
            my_list.remove(item)
        elif choice == 3:
            my_list.print_list()
        elif choice == 4:
            index = int(input("Enter index: "))
            my_list.print_node_index(index)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

main()
"""
#Working on GUI
#Things To-Do(ironically on a todo list)
#1. Add a scrollbar to the listbox
#2. Add a delete button to delete items from the listbox
#3. Add a save button to save the listbox items to a file
#4. Add a load button to load the listbox items from a file
#5. Add a clear button to clear the listbox
#6. Add a search button to search for items in the listbox
#7. Add a sort button to sort the listbox items
#8. Add a count button to count the number of items in the listbox
#9. Add a reverse button to reverse the listbox items
#10. Add a copy button to copy the listbox items to the clipboard

from tkinter import *

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
                return current_node.data
            current_node = current_node.next
            count += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Todo List")
        self.pack()
        self.my_list = LinkedList()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, text="Add an item:")
        self.label.pack()

        self.entry = Entry(self)
        self.entry.pack()

        self.add_button = Button(self, text="Add", command=self.add_item)
        self.add_button.pack()

        self.show_button = Button(self, text="Show All", command=self.show_items)
        self.show_button.pack()

        self.quit_button = Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def add_item(self):
        item = self.entry.get()
        self.my_list.append(item)
        self.entry.delete(0, END)

    def show_items(self):
        list_window = Toplevel(self)
        list_window.title("Todo List")

        scrollbar = Scrollbar(list_window)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(list_window, yscrollcommand=scrollbar.set)
        listbox.pack(side=LEFT, fill=BOTH)

        for item in self.my_list:
            listbox.insert(END, item)

        scrollbar.config(command=listbox.yview)

root = Tk()
app = Application(master=root)
app.mainloop()