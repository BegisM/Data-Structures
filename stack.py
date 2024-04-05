from typing import Optional


class Node:
    def __init__(self, data: Optional[int] = None, prev: Optional['Node'] = None) -> None:
        self.data: Optional[int] = data
        self.prev: Optional['Node'] = prev


class Stack:
    def __init__(self, data: Optional[int] = None) -> None:
        if not data:
            self.tail: Optional['Node'] = None
            self.__size: int = 0
            return

        self.tail: Optional['Node'] = Node(data)
        self.__size: int = 1

    def push(self, data: int) -> None:
        self.__size += 1
        if not self.tail:
            self.tail = Node(data)
            return

        self.tail = Node(data, self.tail)

    def pop(self) -> Optional[int]:
        if not self.tail:
            return None

        self.__size -= 1
        result: int = self.tail.data
        if not self.tail.prev:
            self.tail = None
        else:
            self.tail = self.tail.prev
        return result

    def peek(self) -> Optional[int]:
        return self.tail.data if self.tail else None

    def is_empty(self) -> bool:
        return not self.tail

    def size(self) -> int:
        return self.__size
