from DSFactory import *
from CPPFactory import *
import python_implementations.BST as pyBST
import numpy as np
import time



class ImplementationComparisonStudy(object):

    def __init__(self,data):
        data_structure_names = { 'ua':'unsorted array', 'sa': 'sorted array',\
                    'bst':'BST', 'ht':'hash table'}


        linked_ds = ['bst']


        self.ds = dict()
        self.cpp_ds = dict()

        for k in data_structure_names.keys():
            self.ds[k]=DSFactory.factory(data_structure_names[k])
            self.cpp_ds[k]=CPPFactory.factory(data_structure_names[k],len(data))


        for k in self.ds.keys():
            if k in linked_ds:
                head = self.ds[k]
                head.val = data[0]
                self.ds[k] = head

        self.ds['ht'].setSize(len(data)) 

        for i in range(1,len(data)):

            for k in self.cpp_ds.keys():

                self.cpp_ds[k].insert(int(data[i]))

                if k=='bst':
                    self.ds[k] = pyBST.insert(self.ds['bst'],data[i])
                else:
                    self.ds[k].insert(data[i])




    def perform_search(self,data,search_times,i,j):

        start = time.time()
        self.ds['ua'].search(data[i])
        end = time.time()
        search_times[0][j] = end-start

        start = time.time()
        self.ds['sa'].search(data[i])
        end = time.time()
        search_times[1][j] = end-start

        start = time.time()
        assert pyBST.search(self.ds['bst'],data[i])
        end = time.time()
        search_times[2][j] = end-start


        start = time.time()
        self.ds['ht'].search(data[i])
        end = time.time()
        search_times[3][j] = end-start


        start = time.time()
        self.cpp_ds['ua'].search(int(data[i]))
        end = time.time()
        search_times[4][j] = end-start

        start = time.time()
        self.cpp_ds['sa'].search(int(data[i]))
        end = time.time()
        search_times[5][j] = end-start

        start = time.time()
        self.cpp_ds['bst'].search(int(data[i]))
        end = time.time()
        search_times[6][j] = end-start


        start = time.time()
        self.cpp_ds['ht'].search(int(data[i]))
        end = time.time()
        search_times[7][j] = end-start

        return search_times
