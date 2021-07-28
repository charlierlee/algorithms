import math
import random
import mergeSort
class DSelect:

    def __init__(self, items, i):
        self.recursiveCalls = 0
        self.items = items
        self.i = i # ith order statistic

    def solve(self):
        return self.solveRecursive(self.items, 0, len(self.items))

    def swap(self, A, l, r):
        temp = A[l]
        A[l] = A[r]
        A[r] = temp
        return A

    def choosePivot(self, l, r):
        return random.randint(l, r-1)

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
            
    def partition(self, A, l, r):
        p = A[l]
        i = l + 1
        for j in range(l+1,r):
            if A[j] < p:
                A = self.swap(A, j, i)
                i += 1
            j += 1
        A = self.swap(A, l, i-1)
        return A, i-1

    def medianOfMedian(self, A):
        self.recursiveCalls += 1
        if len(A) == 1:
            return A[0]
        C = []
        chunks = list(self.chunks(list(A),5))
        for k in range(0,len(chunks)):
            obj = mergeSort.MergeSort(chunks[k])
            lst = obj.solve()
            #print('lst',lst)
            mid = len(lst)//2
            #print('mid',mid)
            C.append(lst[mid])
        return self.medianOfMedian(C)

    def solveRecursive(self, A, l, r):
        self.recursiveCalls += 1
        if l >= r:
            return A[0]
        tmp = []
        for k in range(l,r):
            tmp.append(A[k])
        i = self.medianOfMedian(tmp)
        i = A.index(i)

        #i = self.choosePivot(l, r)

        A = self.swap(A, l, i)
        A, j = self.partition(A, l,r)
        if j == self.i:
            return A[j]
        elif j > self.i:
            return self.solveRecursive(A, l, j)
        else:
            return self.solveRecursive(A, j+1, r)
    
    def printRecursiveCalls(self):
        print('dSelect', self.recursiveCalls, 'completed')
