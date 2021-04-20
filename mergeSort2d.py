import math

class MergeSort2d:

    def __init__(self):
        self.recursiveCalls = 0

    def solve(self, items, keyIndex):
        self.key = keyIndex
        n = len(items[self.key])
        self.solveRecursive(items,0,n-1)
        return items

    # Merges two subarrays of arr[self.key][].
    # First subarray is arr[self.key][l..m]
    # Second subarray is arr[self.key][m+1..r]
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r- m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0 , n1):
            L[i] = arr[self.key][l + i]

        for j in range(0 , n2):
            R[j] = arr[self.key][m + 1 + j]

        # Merge the temp arrays back into arr[self.key][l..r]
        i = 0	 # Initial index of first subarray
        j = 0	 # Initial index of second subarray
        k = l	 # Initial index of merged subarray

        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[self.key][k] = L[i]
                i += 1
            else:
                arr[self.key][k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[self.key][k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[self.key][k] = R[j]
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted
    def solveRecursive(self,arr,l,r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = (l+(r-1))//2

            # Sort first and second halves
            self.solveRecursive(arr, l, m)
            self.solveRecursive(arr, m+1, r)
            self.merge(arr, l, m, r)

    def printRecursiveCalls(self):
        print('MergeSort2d', self.recursiveCalls)

