"""

    CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT -  DATA STRUCTURES AND ALGORITHM
    GIẢI THUẬT: DANH SÁCH LIÊN KẾT - LINKED LIST

    >> SIMPLE LINKED LIST <<

    ----

    Facebook: https://facebook.com/yew210.4
    Github: https://github.com/iyew-2104
    Blog: https://www.iyew.io.vn

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class ListNode:


    def __init__(self):
        self.head = None

    
    def add_frist_node(self, data):

        new_node = Node(data)

        if not self.head:   # or **if self.head == None:**
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    
    def delete_first_node(self):
        
        if not self.head:
            print("Liked List is empty.")
            return
        
        self.head = self.head.next


    def delete_middle_node(self, position):

        current_node = self.head
        count = 1
        prev_node = Node

        if not self.head:
            print("Liked List is empty.")
            return

        if position <= 0:
            print(">> Position should be a positive integer greater than 0. !")

        while current_node and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if count == position:

            if count == 1:
                self.head = self.head.next

            else:
                prev_node.next = current_node.next

        else:
            print(">> Position does not exist. !")
        

    def delete_last_node(self):
        
        if not self.head:
            print("Liked List is empty.")
            return
        
        last_node = self.head
        prev_node = None

        while last_node.next:
            prev_node = last_node
            last_node = last_node.next
        
        prev_node.next = None
        

    def add_middle_node(self, position ,data):
        
        new_node = Node(data)
        current_node = self.head
        count = 1

        if position <= 0:
            print(">> Position should be a positive integer greater than 0. !")
        
        while current_node and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if count == position:
            new_node.next = current_node

            if count == 1:
                self.head = new_node

            else:
                prev_node.next = new_node

        else:
            print(">> Position does not exist. !")


    def add_last_node(self, data):

        new_node = Node(data)

        if not self.head:   # or **if self.head == None:**
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        

    def search(self, value):

        current_node = self.head

        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next

        return False

    def show_list(self):
        
        current_node = self.head

        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next

        print("None")


if __name__ == "__main__":

    # Demo

    linked_lisk = ListNode()

    linked_lisk.add_last_node(2)
    linked_lisk.add_last_node(1)
    linked_lisk.add_last_node(0)
    linked_lisk.add_last_node(4)
    linked_lisk.add_last_node(5)
    linked_lisk.show_list()


    linked_lisk.add_frist_node(9)
    linked_lisk.show_list()

    linked_lisk.delete_first_node()
    linked_lisk.show_list()

    linked_lisk.add_middle_node(2,3)
    linked_lisk.show_list()

    linked_lisk.delete_middle_node(2)
    linked_lisk.show_list()

    linked_lisk.delete_last_node()
    linked_lisk.show_list()