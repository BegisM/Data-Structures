from typing import Optional, List


class Node:
    def __init__(self, data: Optional[int] = None, next_node: Optional['Node'] = None) -> None:
        self.data: Optional[int] = data
        self.next: Optional['Node'] = next_node


class LinkedList:
    def __init__(self, data: Optional[int] = None, next_node: Optional['Node'] = None) -> None:
        if data is None:
            self.head: Optional['Node'] = None
            self.tail: Optional['Node'] = None
            self.__size: int = 0
            return

        self.head: Optional['Node'] = Node(data, next_node=next_node)
        self.tail: Optional['Node'] = self.head
        self.__size: int = 1

    def append(self, data: Optional[int]) -> None:
        self.__size += 1
        if not self.tail:
            self.head = self.tail = Node(data)
            return

        if self.tail is self.head:
            self.tail = self.head.next = Node(data)

        else:
            self.tail.next = self.tail = Node(data)

    def prepend(self, data: Optional[int]) -> None:
        self.__size += 1
        if not self.head:
            self.head = self.tail = Node(data)
            return

        self.head = Node(data, self.head)

    def insertion(self, after: Optional[int], data: Optional[int]) -> None:
        if not self.head:
            raise Exception(f"There is no number {after} in this linked list! (Linked list is empty)")

        current: 'Node' = self.head
        while current:
            if current.data == after:
                current.next = Node(data, current.next)
                self.__size += 1
                return
            current = current.next
        raise Exception(f"There is no number {after} in this linked list!")

    def show(self) -> None:
        if not self.head:
            print("No elements in the list")
            return

        current: 'Node' = self.head
        result: List[Optional[int]] = []
        while current:
            result.append(current.data)
            current = current.next

        print(f"There are {self.__size} elements:", *result, sep=' ')

    def search(self, target: Optional[int]) -> Optional['Node']:
        if not self.head:
            return None

        current: 'Node' = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def deletion(self, target: Optional[int]) -> None:
        del_element: Optional['Node'] = self.search(target)
        if not del_element:
            raise Exception("No such element in this list")

        self.__size -= 1

        if del_element is self.head and del_element is self.tail:
            self.head = self.tail = None
            return

        if del_element is self.head:
            self.head = self.head.next
            return


        current: 'Node' = self.head
        while current.next:
            if current.next is del_element:
                current.next = current.next.next
                return
            current = current.next

    @staticmethod
    def partition_last(start: Optional['Node'], end: Optional['Node']) -> Optional['Node']:
        if start is end or not start or not end:
            return start

        pivot_prev: 'Node' = start
        current: 'Node' = start
        pivot: int = end.data

        while start is not end:
            if start.data < pivot:
                pivot_prev = current
                temp: int = current.data
                current.data = start.data
                start.data = temp
                current = current.next
            start = start.next

        end.data = current.data
        current.data = pivot
        return pivot_prev

    def _quick_sort(self, start: Optional['Node'], end: Optional['Node']) -> None:
        if not start or start is end or start is end.next:
            return

        pivot_prev: Optional['Node'] = self.partition_last(start, end)
        self._quick_sort(start, pivot_prev)

        if pivot_prev and pivot_prev is start:
            self._quick_sort(pivot_prev.next, end)

        elif pivot_prev and pivot_prev.next:
            self._quick_sort(pivot_prev.next.next, end)

    def sort(self) -> None:
        self._quick_sort(self.head, self.tail)

    def size(self) -> int:
        return self.__size
