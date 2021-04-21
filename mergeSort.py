import math

class MergeSort:

    def __init__(self, items):
        self.recursiveCalls = 0
        self.items = items

    #Splitting string into equal halves
    def splitArray(self,s):
        return s[:len(s)//2], s[len(s)//2:]

    def solve(self):
        return self.solveRecursive(self.items)

    # the idea here is i+j should sum to n as you increment i and j, 
    # but once out of bound, the next item of a or b is infinity 
    # therefore, the comparison will always switch to the other array
    def merge(self, a, b, n):
        result = [0] * n
        a = a + [math.inf]
        b = b + [math.inf]
        i, j = 0, 0
        for k in range(0, n):
            if a[i] < b[j]:
                result[k] = a[i]
                i+=1
            else:
                result[k] = b[j]
                j+=1
        return result

    def solveRecursive(self, items):
        self.recursiveCalls += 1
        n = len(items)
        baseCase = []
        if n == 0:
            return baseCase
        if n == 1:
            baseCase.append(items[0])
            return baseCase
        if n == 2:
            if items[0] < items[1]:
                baseCase.append(items[0])
                baseCase.append(items[1])
                return baseCase
            else:
                baseCase.append(items[1])
                baseCase.append(items[0])
                return baseCase
        left, right = self.splitArray(items)
        sortedLeft = self.solveRecursive(left)
        sortedRight = self.solveRecursive(right)
        return self.merge(sortedLeft,sortedRight,n)
    
    def printRecursiveCalls(self):
        print('MergeSort', self.recursiveCalls, 'completed')

