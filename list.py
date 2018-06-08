#!/usr/bin/python

'''
class Node
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


'''
class List
'''
class List:
    def __init__(self):
        self.head = None

    # Insert at the tail
    def insert(self, d):
        if self.head is None:
            self.head = Node(d)
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            n = Node(d)
            t.next = n

    # Insert at head
    def insertHead(self, d):
        if self.head is None:
            self.head = Node(d)
        else:
            n = Node(d)
            n.next = self.head
            self.head = n

    # Insert an array into the list
    def insertArray(self, arr):
        for a in arr:
            self.insert(a)

    # Delete the node that head is pointing to
    def deleteHead(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    # Delete the first occurance
    def delete(self, d):
        prev = None
        t = self.head
        while t is not None:
            if t.data == d:
                if prev is None: self.head = t.next
                else: prev.next = t.next
                break
            prev = t
            t = t.next

    # Length of the List (num nodes)
    def length(self):
        len = 0
        t = self.head
        while t is not None:
            len = len + 1
            t = t.next
        return len

    # Print the list
    def printList(self):
        t = self.head
        while t is not None:
            print t.data,
            t = t.next
        print

    def reverse(self):
        if self.head is None:
            return
        t = self.head
        prev = None
        while t is not None:
            save = t.next
            t.next = prev
            prev = t
            t = save
        self.head = prev



'''
addList
'''
def addList(l1, l2):
    l = []
    l1.reverse()
    l2.reverse()

    t1 = l1.head
    t2 = l2.head
    a = 0
    while t1 is not None and t2 is not None:
        a = t1.data + t2.data + a
        l.append(a%10)
        a = a/10
        t1 = t1.next
        t2 = t2.next

    t = t1 if t1 is not None else t2

    while t is not None:
        a = t.data+a
        l.append(t.data%10)
        t = t.next
        a = a/10

    if a > 0: l.append(a)

    l.reverse()
    l1.reverse()
    l2.reverse()
    print l


'''
addListRecurseHelp
'''
def addListRecurseHelp(l1, l2, l):
    if l1 is None and l2 is None:
        return 0

    a = l1.data + l2.data + addListRecurseHelp(l1.next, l2.next, l)
    l.append(a%10)
    return(a/10)

'''
addListRecurse
'''
def addListRecurse(l1, l2):
    diff = l2.length() - l1.length()
    if diff > 0:
        while diff > 0:
            l1.insertHead(0)
            diff -= 1
    else:
        while diff < 0:
            l2.insertHead(0)
            diff += 1

    l = []
    if addListRecurseHelp(l1.head, l2.head, l) > 0:
        l.append(1)
    l.reverse()
    print l

'''
main
'''
def main():
    l1 = List()
    l1.insertArray([9,9,9,4,5,6])

    l2 = List()
    l2.insertArray([5,5,6])
    #addList(l1, l2)

    l1.printList()
    l2.printList()
    addListRecurse(l1, l2)
    addList(l1, l2)

if __name__ == '__main__':
    main()
