"""

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and
deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root_node):
    string = []

    def serializer(root):
        if root is None:
            string.append("-1")
            return
        string.append(root.val)
        serializer(root.left)
        serializer(root.right)

    serializer(root_node)
    return string


index = 0


def deserialize(array):
    global index
    if index == len(array) or array[index] == "-1":
        index += 1
        return None

    root = Node(array[index])
    index += 1

    root.left = deserialize(array)
    root.right = deserialize(array)
    return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
