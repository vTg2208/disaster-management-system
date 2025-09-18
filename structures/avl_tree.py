class AVLNode:
    def __init__(self, key, severity):
        self.key = key
        self.severity = severity
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return y

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def insert(self, root, key, severity):
        if not root:
            return AVLNode(key, severity)
        if severity < root.severity:
            root.left = self.insert(root.left, key, severity)
        else:
            root.right = self.insert(root.right, key, severity)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and severity < root.left.severity:
            return self.rotate_right(root)
        if balance < -1 and severity > root.right.severity:
            return self.rotate_left(root)
        if balance > 1 and severity > root.left.severity:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and severity < root.right.severity:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root


    def inorder(self,root):

        if root:
            self.inorder(root.left)
            print("(",root.key,",",root.severity,")",end=" ")
            self.inorder(root.right)

