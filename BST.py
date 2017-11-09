class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root != None:
            x = self.root
            while x != None:
                y = x
                if x.value < new_val:
                    x = x.right
                else:
                    x = x.left
            if y != None:
                if y.value < new_val:
                    y.right = Node(new_val)
                else:
                    y.left = Node(new_val)
        else:
            self.root = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, start, find_val):
        if start != None:
            if start.value == find_val:
                return True
            else:
                if start.value < find_val:
                    return self.search_helper(start.right, find_val)
                else:
                    return self.search_helper(start.left, find_val)
        return False
        
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
