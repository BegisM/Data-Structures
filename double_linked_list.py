from typing import Optional, List


class Node:
    def __init__(self, data: Optional[int] = None, next_node: Optional['Node'] = None,
                 prev_node: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoubleLinkedList:
    def __init__(self, data: Optional['int'] = None, next_node: ['Node'] = None, prev_node: ['Node'] = None) -> None:
        if not data:
            self.head: Optional['Node'] = None
            self.tail: Optional['Node'] = None
            self.__size: int = 0
            return

        self.__size: int = 1
        self.head: Optional['Node'] = Node(data, next_node=next_node, prev_node=prev_node)
        self.tail: Optional['Node'] = self.head

    def append(self, data: Optional[int]) -> None:
        self.__size += 1
        if not self.head:
            self.head = self.tail = Node(data)
            return

        if self.head is self.tail:
            self.head.next = Node(data, prev_node=self.head)
            self.tail = self.head.next
            return

        self.tail.next = Node(data, prev_node=self.tail)
        self.tail = self.tail.next

    def prepend(self, data: Optional[int]) -> None:
        self.__size += 1
        if not self.head:
            self.head = self.tail = Node(data)
            return

        self.head.prev = Node(data, next_node=self.head)
        self.head = self.head.prev

    def insertion_after(self, after: Optional[int], data: Optional['int']) -> None:
        if not self.head:
            raise Exception(f'There is no element {after}! (No elements in the list)')

        current: Optional['Node'] = self.head
        while current:
            if after == current.data:
                self.__size += 1
                if not current.next:
                    self.append(data)
                    return

                current.next = Node(data, next_node=current.next, prev_node=current)
                current.next.prev = current.next
                return
            current = current.next

        raise Exception(f"There is no element {after}!")

    def insertion_between(self, after: Optional[int], before: Optional[int], data: Optional[int]) -> None:
        if not self.head:
            raise Exception(f'There is no element {after} and element {before}! (No elements in the list)')

        current: Optional['Node'] = self.head
        while current.next:
            if after == current.data and current.next.data == before:
                self.__size += 1
                current.next = Node(data, next_node=current.next, prev_node=current)
                current.next.prev = current.next
                return
            current = current.next

        raise Exception(f"There is no element {after} or element {before}!")

    def searching(self, target: Optional[int]) -> Optional['Node']:
        if not self.head:
            return None

        current: Optional['Node'] = self.head
        while current:
            if current.data == target:
                return current
            current = current.next

        return None

    def deletion(self, target: Optional[int]) -> None:
        del_element: Optional['Node'] = self.searching(target)
        if not del_element:
            raise Exception(f'No such element {target}!')

        self.__size -= 1

        if del_element is self.head and self.head is self.tail:
            self.head = self.tail = None
            return

        if del_element is self.head:
            self.head = self.head.next
            self.head.prev = None
            return

        current: Optional['Node'] = self.head
        while current.next:
            if current.next is del_element:
                if not current.next.next:
                    current.next, del_element.prev = None, None
                    return

                current.next = current.next.next
                current.next.prev = current
                return
            current = current.next

    def show(self) -> None:
        if not self.head:
            print('There are no elements in the double linked list!')
            return

        current: Optional['Node'] = self.head
        result: List[Optional[int]] = []
        while current:
            result.append(current.data)
            current = current.next
        print(f"There are {self.__size} elements in the double linked list", *result, sep=' ')

    @staticmethod
    def partition(left: Optional['Node'], right: Optional['Node']) -> Optional['Node']:
        pivot: Optional['Node'] = right
        i: Optional['Node'] = left.prev
        ptr: Optional['Node'] = left
        while ptr != right:
            if ptr.data <= pivot.data:
                i = left if i is None else i.next
                i.data, ptr.data = ptr.data, i.data
            ptr = ptr.next
        i = left if i is None else i.next
        i.data, pivot.data = pivot.data, i.data
        return i

    def _quick_sort(self, left: Optional['Node'], right: Optional['Node']) -> None:
        if right and left is not right and left is not right.next:
            pivot: Optional['Node'] = self.partition(left, right)
            self._quick_sort(left, pivot.prev)
            self._quick_sort(pivot.next, right)

    def sort(self) -> None:
        self._quick_sort(self.head, self.tail)

    def size(self) -> int:
        return self.__size
