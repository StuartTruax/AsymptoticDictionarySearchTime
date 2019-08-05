from DictionaryImplementor import *

class LLNode(object):
  def __init__(self, val, next):
      self.val = val
      self.next = next

  def __str__(self):
      return "[ "+str(self.val)+" ]->"


class LL(DictionaryImplementor):

    @staticmethod
    def search(head, val):
        if not head:
            return None

        #if head.val == val:
        #    return head
        #else:
        #    return LL.search(head.next, val)

        cur = head

        while cur:
            if cur.val == val:
                return cur
            cur = cur.next

        return None

    @staticmethod
    def insert(head, val):
        node = LLNode(val,head)
        return node

    @staticmethod
    def delete(head, val):
        targetNode = LL.search(head,val)

        if targetNode:

            pred = LL.getPredecessorList(head,val)

            if not pred:
                head = targetNode.next
            else:
                pred.next = targetNode.next
            return head


    @staticmethod
    def getPredecessorList(head,val):
        if not head or not head.next:
            return None

        if head.next.val == val:
            return head
        else:
            return LL.getPredecessorList(head.next,val)

    @staticmethod
    def sort(head):
        #mergesort
        if not head:
            return None
        elif not head.next:
            return head
        else:
            (a,b) = LL.__frontBackSplit(head)
            a = LL.sort(a)
            b = LL.sort(b)
            return LL.__merge(a,b)

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

        cur = head

        while cur.next != b:
            cur = cur.next

        cur.next = None


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

                temp = cur_a
                cur_a = cur_a.next
                temp.next = None
            else:
                if temp:
                    temp.next = cur_b
                temp = cur_b
                cur_b = cur_b.next
                temp.next = None

            if not retHead:
                retHead = temp

        while cur_a:
            if temp:
                temp.next = cur_a
            temp = cur_a
            cur_a = cur_a.next
            temp.next = None

        while cur_b:
            if temp:
                temp.next = cur_b
            temp = cur_b
            cur_b = cur_b.next
            temp.next = None

        return retHead

    @staticmethod
    def arrayToLL(array):

        head = None
        prev = None

        for i in range(0,len(array)):
            if i ==0:
                head = LLNode(array[i],None)
                prev = head
            else:
                cur = LLNode(array[i], None)
                prev.next = cur
                prev = cur

        return head


    @staticmethod
    def toString(head):
        if not head:
            return ""

        ret = str(head)

        return ret+LL.toString(head.next)
