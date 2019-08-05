from DictionaryImplementor import *

class BSTNode(object):
    def __init__(self,val, left, right):
        self.val = val
        self.left = left
        self.right = right

class BST(DictionaryImplementor):

    @staticmethod
    def search(root,x):
        if not root:
            return False

        if root.val == x :
            return True
        elif  x < root.val:
            return BST.search(root.left, x)
        else:
            return BST.search(root.right,x)

    @staticmethod
    def insert(root,x):

        toInsert = BSTNode(x,None,None)

        if not root:
            root = toInsert
        else:
            BST.__insertNode(root, toInsert)

        return root

    @staticmethod
    def __insertNode(root,toInsert):

        if toInsert.val < root.val:
            if not root.left:
                root.left = toInsert
                return
            BST.__insertNode(root.left, toInsert)
        else:
            if not root.right:
                root.right = toInsert
                return
            BST.__insertNode(root.right,toInsert)



    @staticmethod
    def delete(root,x):
        if not root:
            return None

        if root.val == x:
            if not root.right and not root.left:
                return None
            elif root.right and not root.left:
                return root.right
            elif not root.right and root.left:
                return root.left
            else:
                min = BST.__findMin(root)
                root.val = min.val
                root.left = BST.delete(root.left,min.val)
        else:
            root.left = BST.delete(root.left,x)
            root.right = BST.delete(root.right,x)
        return root


    @staticmethod
    def __findMin(root):
        if root.left:
            return BST.__findMin(root.left)
        else:
            return root

    @staticmethod
    def sort():
        pass

    @staticmethod
    def toStringInOrder(root):
        return BST.__inorderAppend(root)

    @staticmethod
    def __inorderAppend(root):
        s = ""
        if not root:
            return s
        else:
            s+=BST.__inorderAppend(root.left)
            s+=" "+str(root.val)
            s+=BST.__inorderAppend(root.right)
            return s


    @staticmethod
    def insertInOrder(root,a):
        for val in a:
            BST.__insert(root,val)

        return root
