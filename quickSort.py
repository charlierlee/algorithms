import math
import random
class QuickSort:

    def __init__(self, items):
        self.recursiveCalls = 0
        self.items = items

    def solve(self):
        return self.solveRecursive(0, len(self.items))

    def swap(self, l, r):
        temp = self.items[l]
        self.items[l] = self.items[r]
        self.items[r] = temp

    def choosePivot(self, l, r):
        return random.randint(l, r-1)

    def partition(self, l, r):
        p = self.items[l]
        i = l + 1
        for j in range(l+1,r):
            if self.items[j] < p:
                self.swap(j, i)
                i += 1
            j += 1
        self.swap(l, i-1)
        return i-1

    def solveRecursive(self, l, r):
        self.recursiveCalls += 1
        if l >= r:
            return
        i = self.choosePivot(l, r)
        self.swap(l, i)
        j = self.partition(l,r)
        self.solveRecursive(l, j)
        self.solveRecursive(j+1, r)
    
    def printRecursiveCalls(self):
        print('QuickSort', self.recursiveCalls, 'completed')

