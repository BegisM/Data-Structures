from typing import Optional, List


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data


class Heap:
    def __init__(self, data: Optional['int'] = None, heap: Optional[List[Optional['Node']]] = None) -> None:
        self.heap: List['Node'] = []
        if not data:
            self.heap = []
            self._size: int = 0
            if heap:
                self.heap = heap
                self._size = len(heap)
            return

        self.heap.append(Node(data))
        self._size: int = 1

    @staticmethod
    def parent(position: int) -> int:
        if position < 3:
            return 0
        return position // 2

    @staticmethod
    def left_child(position: int) -> int:
        if position == 0:
            return 1
        return position * 2

    @staticmethod
    def right_child(position: int) -> int:
        if position == 0:
            return 2
        return position * 2 + 1

    def swap(self, first: int, second: int) -> None:
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def append(self, data: int) -> None:
        self._size += 1
        if len(self.heap) == 0:
            self.heap.append(Node(data))
            return

        self.heap.append(Node(data))
        self.heapify(self._size - 1)

    def show(self) -> None:
        for i in range(self._size):
            print(f'Parent: {self.heap[i].data}')
            if self.left_child(i) < self._size:
                print(f'Left Child: {self.heap[self.left_child(i)].data}')
            if self.right_child(i) < self._size:
                print(f'Right Child: {self.heap[self.right_child(i)].data}')

    def is_leaf(self, position) -> bool:
        if (self._size // 2 - 1) < position < self._size:
            return True
        return False

    def max_heapify(self, position: int) -> None:
        if not self.is_leaf(position):
            if (self.heap[position].data < self.heap[Heap.left_child(position)].data or
                    self.heap[position].data < self.heap[Heap.right_child(position)].data):
                if self.heap[Heap.left_child(position)].data > self.heap[Heap.right_child(position)].data:
                    self.swap(position, Heap.left_child(position))
                    self.max_heapify(Heap.left_child(position))

                else:
                    self.swap(position, Heap.right_child(position))
                    self.max_heapify(Heap.right_child(position))

    def heapify(self, position: int) -> int:
        if self.heap[position].data > self.heap[Heap.parent(position)].data:
            self.swap(position, Heap.parent(position))
            return self.heapify(Heap.parent(position))
        return position
