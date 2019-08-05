from DictionaryImplementor import *


class Array(DictionaryImplementor):

    def __init__(self,isSorted):
        self.isSorted = isSorted
        self.N = 0
        self.data = list()


    def __str__(self):
        ret = "["

        for i in range(0,self.N):
            if i == 0:
                ret+=str(self.data[i])
            else:
                ret+=","+str(self.data[i])

        ret+="]"

        return ret


    def insert(self, x):
        self.data.append(x)
        self.N+=1

        if self.isSorted:
            self.sort()

    def delete(self,x):
        index = -1

        if self.isSorted:
            index = self.__binarySearch(x,0,self.N-1)
        else:
            index = self.__linearSearch(x)

        if index >=0 and index < self.N:
            self.data[index] = self.data[self.N-1]
            self.N -=1

        if isSorted:
            self.sort()

    def sort(self):
        self.data = self.__mergeSort(self.data)

    def __mergeSort(self, input):
        if not input:
            return None
        elif len(input) == 1:
            return input
        else:
            (a,b) = self.__frontBackSplit(input)
            a = self.__mergeSort(a)
            b = self.__mergeSort(b)
            return self.__merge(a,b)

    def __frontBackSplit(self,a):

        if not a:
            return (None, None)

        N = len(a)

        front = list(a[:N//2])
        back  = list(a[N//2:])

        return (front,back)

    def __merge(self,a,b):

        ret =list()

        i=0
        j=0

        while a and b and i < len(a) and j < len(b):
            if a[i] < b[j]:
                ret.append(a[i])
                i+=1
            else:
                ret.append(b[j])
                j+=1

        while a and i < len(a):
            ret.append(a[i])
            i+=1

        while b and j < len(b):
            ret.append(b[j])
            j+=1

        return ret


    def search(self,x):
        if self.isSorted:
            if self.__binarySearch(x,0,self.N-1) == -1:
                return False
            return True
            #return bool(self.__binarySearch(x,0,self.N-1)+1)
        else:
            if self.__linearSearch(x) == -1:
                return False
            return True
            #return bool(self.__linearSearch(x)+1)


    def __binarySearch(self,x,lo,hi):

        if lo==hi:
            if self.data[hi] == x:
                return hi
            else:
                return -1

        mid = (lo+hi)//2

        if x > self.data[mid] and x <= self.data[hi]:
            lo = mid+1
            return self.__binarySearch(x,lo,hi)
        elif x >= self.data[lo] and x <= self.data[mid]:
            hi=mid
            return self.__binarySearch(x,lo,hi)
        else:
            return -1


    def __linearSearch(self,x):

        for i in range(0,self.N):
            if self.data[i] == x:
                return i
        return -1
