from DictionaryImplementor import *

class DLLNode(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return "<-[ "+str(self.val)+" ]->"


class DLL(DictionaryImplementor):

    @staticmethod
    def search(head, val):
        if not head:
            return None

        #if head.val == val:
        #    return head
        #else:
        #    return DLL.search(head.next, val)

        cur = head

        while cur:
            if cur.val == val:
                return cur
            cur = cur.next

        return None

    @staticmethod
    def insert(head, val):
        node = DLLNode(val,None,head)
        head.prev = node
        return node

    @staticmethod
    def delete(head, val):
        targetNode = DLL.search(head,val)

        if targetNode:

            pred = DLL.getPredecessorList(targetNode)

            if not pred:
                head = targetNode.next
                if head:
                    head.prev = None
            else:
                pred.next = targetNode.next
                if targetNode.next:
                    targetNode.next.prev = pred
            return head


    @staticmethod
    def getPredecessorList(head):
        if not head or not head.prev:
            return None
        return head.prev


    @staticmethod
    def sort(head):
        #mergesort
        if not head:
            return None
        elif not head.next:
            return head
        else:
            (a,b) = DLL.__frontBackSplit(head)
            a = DLL.sort(a)
            b = DLL.sort(b)
            return DLL.__merge(a,b)

    @staticmethod
    def __frontBackSplit(head):

        if not head:
            return (None, None)

        count = 0
        cur = head
        while cur:
            count+=1
            cur = cur.next

        halfIndex = count//2

        cur = head
        count = 0
        while cur.next and count<=halfIndex:
            count+=1
            cur = cur.next

        b = cur
        a = head

        if b.prev:
            b.prev.next = None
        b.prev = None

        return (a,b)

    @staticmethod
    def __merge(a,b):
        temp = None
        retHead = None
        cur_a = a
        cur_b = b

        while cur_a and cur_b:
            if cur_a.val < cur_b.val:
                if temp:
                    temp.next = cur_a
                cur_a.prev = temp

                if not temp:
                    temp = cur_a
                    retHead = temp
                else:
                    temp = cur_a

                cur_a = cur_a.next
                if cur_a:
                    cur_a.prev = None
                temp.next = None
            else:
                if temp:
                    temp.next = cur_b
                cur_b.prev = temp


                if not temp:
                    temp = cur_b
                    retHead = temp
                else:
                    temp = cur_b

                cur_b = cur_b.next
                if cur_b:
                    cur_b.prev = None
                temp.next = None

        while cur_a:
            if temp:
                temp.next = cur_a
            cur_a.prev = temp
            temp = cur_a
            cur_a = cur_a.next

            if cur_a:
                cur_a.prev = None
            temp.next = None

        while cur_b:
            if temp:
                temp.next = cur_b
            cur_b.prev = temp
            temp = cur_b

            cur_b = cur_b.next

            if cur_b:
                cur_b.prev = None
            temp.next = None

        return retHead


    @staticmethod
    def arrayToDLL(array):

        if not array.any():
            return None

        N = len(array)
        node = DLLNode(array[N-1],None,None)

        for i in range(N-2,-1,-1):
            next = node
            node = DLLNode(array[i],None,next)
            next.prev = node

        return node


    @staticmethod
    def toString(head):
        if not head:
            return ""

        ret = str(head)

        return ret+DLL.toString(head.next)
