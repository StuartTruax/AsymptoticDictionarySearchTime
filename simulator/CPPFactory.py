from cpp_implementations import *


class CPPFactory(object):

    @staticmethod
    def factory(type, N):
        if type=="unsorted array":
            return Array(N,False)
        elif type=="sorted array":
            return Array(N,True)
        elif type=="BST":
            return BST()
        elif type=="hash table":
            return HashTable(N)
