from typing import Optional


class Node:  # creating Node class for using in the Queue class
    def __init__(self, data: Optional[int] = None, next_node: Optional['Node'] = None) -> None:
        self.data: Optional[int] = data
        self.next: Optional['Node'] = next_node


class Queue:
    def __init__(self, node: Optional['Node'] = None) -> None:
        self.tail: Optional['Node'] = node
        self.head: Optional['Node'] = self.tail
        self.__size: int = 0 if not self.tail else 1

    def enqueue(self, data: int) -> None:   # adds new data to the end of queue
        self.__size += 1
        if not self.head:
            self.head = self.tail = Node(data)
            return

        if self.head is self.tail:
            self.tail = self.head.next = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self) -> Optional[int]:  # removes and returns first element from the queue
        if not self.tail:
            return None

        result: int = self.head.data
        self.__size -= 1
        if self.tail is self.head:
            self.tail = self.head = None
            return result

        self.head = self.head.next
        return result

    def is_empty(self) -> bool:
        return not bool(self.tail)

    def peek(self) -> Optional[int]:  # returns first element of the queue
        if not self.tail:
            return None

        return self.head.data

    def size(self) -> int:
        return self.__size
