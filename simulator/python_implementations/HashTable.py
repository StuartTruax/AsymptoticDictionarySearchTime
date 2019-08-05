from DLL import *
from DictionaryImplementor import *


class HashTable(DictionaryImplementor):

    def __init__(self,M):
        self.M = M
        self.table = [None]*self.M

    def setSize(self,M):
        self.M = M
        self.table = [None]*self.M

    def insert(self, input):
        index = self.__hash(input)

        if self.table[index]:
            #collision, so chain
            head = self.table[index]
            if not DLL.search(head,input):
                self.table[index] = DLL.insert(head,input)
        else:
            head = DLLNode(input,None,None)
            self.table[index] = head

    def search(self, input):
        index = self.__hash(input)

        if self.table[index]:
            return DLL.search(self.table[index],input)
        return None

    def delete(self, input):
        index = self.__hash(input)

        if self.table[index]:
            DLL.delete(self.table[index],input)

    def sort(self,input):
        pass


    def __hash(self,input):
        """
        naive hash function
        could do an implementation of MurmurHash3 at some point
        """
        return int(input)%self.M


    def __str__(self):
        ret = "[ "

        for i in range(0,self.M):
            if self.table[i]:
                ret+=" "+DLL.toString(self.table[i])+", "
            else:
                ret+=", ,"
        ret+="]"

        return ret
