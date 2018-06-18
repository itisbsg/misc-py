#!/usr/bin/python

import collections

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def __insertBSTHelper(self, r, d):
        if r == None:
            return Node(d)

        if d > r.data:
            r.right = self.__insertBSTHelper(r.right, d)
        else:
            r.left = self.__insertBSTHelper(r.left, d)
        return r

    def insertBST(self, d):
        self.root = self.__insertBSTHelper(self.root, d)

    def insertBF(self, d):
        if self.root is None:
            self.root = Node(d)
            return

        q = collections.deque()
        q.append(self.root)
        while len(q) > 0:
            t = q.popleft()
            if t.left is None:
                t.left = Node(d)
                break
            else:
                q.append(t.left)

            if t.right is None:
                t.right = Node(d)
                break
            else:
                q.append(t.right)

    def __printPreOrder(self, r):
        if r == None:
            return
        print r.data,
        self.__printPreOrder(r.left)
        self.__printPreOrder(r.right)

    def printPreOrder(self):
        self.__printPreOrder(self.root)
        print

    def __printInOrder(self, r):
        if r == None:
            return
        self.__printInOrder(r.left)
        print r.data,
        self.__printInOrder(r.right)

    def printInOrder(self):
        self.__printInOrder(self.root)
        print

    def __printPostOrder(self, r):
        if r == None:
            return
        self.__printPostOrder(r.left)
        self.__printPostOrder(r.right)
        print r.data,

    def printPostOrder(self):
        self.__printPostOrder(self.root)
        print

    def __getHeight(self, r):
        if r == None:
            return 0
        return (max(self.__getHeight(r.left), self.__getHeight(r.right))+1)

    def getHeight(self):
        return self.__getHeight(self.root)

    def printBreadthFirst(self):
        bfQ = collections.deque()
        if self.root is not None: bfQ.append(self.root)
        while len(bfQ) > 0:
            t = bfQ.popleft()
            print t.data,
            if t.left is not None: bfQ.append(t.left)
            if t.right is not None: bfQ.append(t.right)
        print

    def checkSumPath(self, pathArr, val):
        #print pathArr
        i = len(pathArr)-1
        t = 0
        while i > 0:
            t += pathArr[i]
            if t == val:
                print pathArr[i:]
            i -= 1

    def __sumPath(self, r, path, val):
        if r is None:
            return

        path.append(r.data)
        self.checkSumPath(path, val)
        self.__sumPath(r.left, path, val)
        self.__sumPath(r.right, path, val)
        path.pop()

    def sumPath(self, sumVal):
        path = []
        self.__sumPath(self.root, path, sumVal)

    def __inOrderTrav(self, r, arr):
        if r is None:
            return
        self.__inOrderTrav(r.left, arr)
        arr.append(r.data)
        self.__inOrderTrav(r.right, arr)

    def isBST(self):
        if self.root is None: return True
        sortArr = []
        self.__inOrderTrav(self.root, sortArr)
        return checkOrder(sortArr)

def checkOrder(arr):
    prev = arr[0]
    for i in xrange(1, len(arr)):
        if arr[i] < prev:
            return False
        prev = arr[i]
    return True

def main():
    binTree = BT()

    binTree.insertBST(10)
    binTree.insertBST(5)
    binTree.insertBST(16)
    binTree.insertBST(14)
    binTree.insertBST(11)
    binTree.insertBST(0)
    print "Is BST:", binTree.isBST()

    binTree.insertBF(25)
    binTree.insertBF(150)
    binTree.insertBF(100)
    binTree.insertBF(110)
    binTree.insertBF(0)
    binTree.insertBF(112)
    binTree.insertBF(91)
    print "Is BST:", binTree.isBST()

    binTree.printPreOrder()
    binTree.printInOrder()
    binTree.printPostOrder()
    print binTree.getHeight()
    binTree.printBreadthFirst()
    binTree.sumPath(30)


if __name__ == '__main__':
    main()
