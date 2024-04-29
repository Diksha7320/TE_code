'''
Implement Depth first search algorithm and Breadth
First Search algorithm, use an undirected graph and develop a recursive algorithm for
searching all the vertices of a graph or tree data structure.
'''
class Node:
    def __init__(self, num):
        self.data = num
        self.left = None
        self.right = None

head=None

def depthFirstSearch(root):
    if root is not None:
        print(root.data)
        depthFirstSearch(root.left)
        depthFirstSearch(root.right)

def breadthFirstSearch(root):
    if root is None:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


def insertnode(num):
    global head
    if head is None:
        head = Node(num)
    else:
        current = head
        while True:
            if num < current.data:
                if current.left is None:
                    current.left = Node(num)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(num)
                    break
                else:
                    current = current.right


for i in range(7):
    num = int(input("Enter number:"))
    insertnode(num)

print(head.data)

print("Depth-First Search:")
depthFirstSearch(head)

print("\nBreadth-First Search:")
breadthFirstSearch(head)
