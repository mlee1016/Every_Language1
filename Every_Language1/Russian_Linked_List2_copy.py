
class Node:
    def __init__(self, data:str):
        self.data:str = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    
    
    def append(self, data:str):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


    

    
    def get_next(self, current_node):
        if current_node is None:
            return None
        else:
            return current_node.next

    
    def get_node(self, index):
        if index < 0:
            return None

        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1

        return None




    def delete_node(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in linked list
        if temp == None:
            return




        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
    
    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count