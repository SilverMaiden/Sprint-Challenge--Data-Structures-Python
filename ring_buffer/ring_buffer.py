from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif len(self.storage) < self.capacity:
            self.current.insert_after(item)
            self.storage.length += 1
            if len(self.storage) == self.capacity:
                self.current = self.storage.head
            else:
                self.current = self.current.next

        else:
            self.current.insert_after(item)
            if self.current == self.storage.head:
                self.storage.head = self.current.next
            self.current = self.current.next
            self.storage.delete(self.current.prev)
            self.storage.length += 1

            if self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        outputList = []
        currentNode = self.storage.head

        while currentNode.next != None:
            if currentNode.value != None:
                outputList.append(currentNode.value)
            currentNode = currentNode.next
        return outputList
