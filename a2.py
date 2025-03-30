class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublySortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif data <= self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif data >= self.tail.data:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def is_present(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    linked_list = DoublySortedLinkedList()
    # Insert some data
    linked_list.insert(5)
    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(3)
    linked_list.insert(6)
    # Display the list
    linked_list.display()
    # Test remove
    linked_list.remove(3)
    linked_list.display()
    # Test is_present
    print(linked_list.is_present(7))
    print(linked_list.is_present(3))
    # Test __len__
    print(len(linked_list))  # Should print 4

if __name__ == '__main__':
    main()
