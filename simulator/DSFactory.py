from python_implementations import *


class DSFactory(object):

    @staticmethod
    def factory(type):
        if type=="unsorted array":
            return Array(False)
        elif type=="sorted array":
            return Array(True)
        elif type=="unsorted LL":
            return LLNode(None,None)
        elif type=="sorted LL":
            return LLNode(None,None)
        elif type=="unsorted DLL":
            return DLLNode(None,None,None)
        elif type=="sorted DLL":
            return DLLNode(None,None,None)
        elif type=="BST":
            return BSTNode(None,None,None)
        elif type=="hash table":
            return HashTable(1)
