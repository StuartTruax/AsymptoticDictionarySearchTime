from DSFactory import *
import numpy as np
import time



class AsymptoticSearchTimeStudy(object):

    def __init__(self,data):
        data_structure_names = {'ull': 'unsorted LL', 'sll': 'sorted LL', 'sdll': 'sorted DLL',\
                    'udll': 'unsorted DLL', 'ua':'unsorted array', 'sa': 'sorted array',\
                    'bst':'BST', 'ht':'hash table'}


        linked_ds = ['ull','sll','sdll','udll','bst']


        self.ds = dict()

        for k in data_structure_names.keys():
            self.ds[k]=DSFactory.factory(data_structure_names[k])


        for k in self.ds.keys():
            if k in linked_ds:
                head = self.ds[k]
                head.val = data[0]
                self.ds[k] = head

        self.ds['ht'].setSize(len(data))


        for i in range(1,len(data)):
            self.ds['ull']=LL.insert(self.ds['ull'],data[i])
            self.ds['sll']=LL.insert(self.ds['sll'],data[i])
            self.ds['sll']=LL.sort(self.ds['sll'])

            self.ds['udll']=DLL.insert(self.ds['udll'],data[i])
            self.ds['sdll']=DLL.insert(self.ds['sdll'],data[i])
            self.ds['sdll']=DLL.sort(self.ds['sdll'])


            self.ds['ua'].insert(data[i])
            self.ds['sa'].insert(data[i])

            self.ds['bst'] = BST.insert(self.ds['bst'],data[i])

            self.ds['ht'].insert(data[i])


        self.ds['sll']=LL.sort(self.ds['sll'])
        self.ds['sdll']=DLL.sort(self.ds['sdll'])



    def perform_search(self,data,search_times,i,j):
        start = time.time()
        assert LL.search(self.ds['ull'],data[i])
        end = time.time()
        search_times[0][j] = end-start

        start = time.time()
        assert LL.search(self.ds['sll'],data[i])
        end = time.time()
        search_times[1][j] = end-start

        start = time.time()
        assert DLL.search(self.ds['udll'],data[i])
        end = time.time()
        search_times[2][j] = end-start

        start = time.time()
        assert DLL.search(self.ds['sdll'],data[i])
        end = time.time()
        search_times[3][j] = end-start


        start = time.time()
        self.ds['ua'].search(data[i])
        end = time.time()
        search_times[4][j] = end-start

        start = time.time()
        self.ds['sa'].search(data[i])
        end = time.time()
        search_times[5][j] = end-start

        start = time.time()
        assert BST.search(self.ds['bst'],data[i])
        end = time.time()
        search_times[6][j] = end-start


        start = time.time()
        self.ds['ht'].search(data[i])
        end = time.time()
        search_times[7][j] = end-start

        return search_times
