# a python program to implement a double linked list and a function which finds if there is loop in doubly linkedin list.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node = Node(data)
            current.next = new_node
            new_node.prev = current

    def detect_loop(self):
        # Using Floyd's Cycle-Finding Algorithm
        if not self.head:
            return False

        tortoise = self.head
        hare = self.head

        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True

        return False

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    # Introduce a loop for testing
    dll.head.next.next.next.next = dll.head

    if dll.detect_loop():
        print("Loop detected!")
    else:
        print("No loop detected!")
