import math
import random
class RSelect:

    def __init__(self, items, i):
        self.recursiveCalls = 0
        self.items = items
        self.i = i # ith order statistic

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
            return self.items[0]
        i = self.choosePivot(l, r)
        self.swap(l, i)
        j = self.partition(l,r)
        if j == self.i:
            return self.items[j]
        elif j > self.i:
            return self.solveRecursive(l, j)
        else:
            return self.solveRecursive(j+1, r)
    
    def printRecursiveCalls(self):
        print('rSelect', self.recursiveCalls, 'completed')

