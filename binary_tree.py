from typing import Optional, List


class Node:
    def __init__(self, data: Optional[int] = None, left: Optional['Node'] = None,
                 right: Optional['Node'] = None) -> None:
        self.data: Optional[int] = data
        self.left: Optional['Node'] = left
        self.right: Optional['Node'] = right


class BinaryTree:
    def __init__(self, data: Optional[int] = None, left: Optional['Node'] = None,
                 right: Optional['Node'] = None) -> None:
        if not data:
            self.root: Optional['Node'] = None
            self.__size: int = 0
            return

        self.__size: int = 1
        self.root: Optional['Node'] = Node(data, left, right)

    def append(self, data: int) -> None:
        self.__size += 1
        if not self.root:
            self.root = Node(data)
            return

        self.__append(data, self.root)

    def __append(self, data: int, node: Optional['Node']) -> None:
        if data < node.data:
            if node.left:
                self.__append(data, node.left)

            else:
                node.left = Node(data)

        elif data > node.data:
            if node.right:
                self.__append(data, node.right)

            else:
                node.right = Node(data)

    def inorder_show(self) -> None:
        result: List[Optional[int]] = self.inorder_list()
        print(*result, sep=' ')

    def __inorder_traversal(self, node: Optional['Node'], result: List[Optional[int]]) -> None:
        if node:
            self.__inorder_traversal(node.left, result)
            result.append(node.data)
            self.__inorder_traversal(node.right, result)

    def inorder_list(self) -> List[int]:
        result: List[Optional[int]] = []
        self.__inorder_traversal(self.root, result)
        return result

    def search(self, target: int) -> Optional['Node']:
        return self.__search(target, self.root)

    def __search(self, target: int, node: Optional['Node']) -> Optional['Node']:
        if not node or node.data == target:
            return node

        if node.data > target:
            return self.__search(target, node.left)

        else:
            return self.__search(target, node.right)

    def preorder_show(self) -> None:
        result: List[Optional[int]] = self.preorder_list()
        print(*result, sep=' ')

    def __preorder_traversal(self, node: Optional['Node'], result: List[int]) -> None:
        if node:
            result.append(node.data)
            self.__preorder_traversal(node.left, result)
            self.__preorder_traversal(node.right, result)

    def preorder_list(self) -> List[int]:
        result: List[Optional[int]] = []
        self.__preorder_traversal(self.root, result)
        return result

