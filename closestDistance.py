import math

class ClosestDistance:

    def __init__(self, items):
        self.recursiveCalls = 0
        self.items = items

    #Splitting string into equal halves
    def splitArray(self,s):
        return s[:len(s)//2], s[len(s)//2:]

    def solve(self):
        return self.solveRecursive(self.items)

    def merge(self, a, b, n):
        distance = math.inf
        result = [0] * n
        a = a + [math.inf]
        b = b + [math.inf]
        i, j = 0, 0
        q, r = 0, 0
        for k in range(0, n):
            if a[i] < b[j]:
                result[k] = a[i]
                i+=1
            else:
                result[k] = b[j]
                j+=1
            if k > 0:
                d = (result[k] - result[k-1]) ** 2
                if d < distance:
                    distance = d
        return result, distance

    def solveRecursive(self, items):
        self.recursiveCalls += 1
        n = len(items)
        baseCase = []
        if n == 0:
            return baseCase, math.inf
        if n == 1:
            baseCase.append(items[0])
            return baseCase, math.inf
        if n == 2:
            if items[0] < items[1]:
                baseCase.append(items[0])
                baseCase.append(items[1])
                return baseCase, (items[0] - items[1]) ** 2
            else:
                baseCase.append(items[1])
                baseCase.append(items[0])
                return baseCase, (items[0] - items[1]) ** 2
        left, right = self.splitArray(items)
        sortedLeft, distanceLeft = self.solveRecursive(left)
        sortedRight, distanceRight = self.solveRecursive(right)
        merged, distanceCenter = self.merge(sortedLeft,sortedRight,n)
        distance = math.inf
        if distanceLeft < distanceRight:
            distance = distanceLeft
        else:
            distance = distanceRight
        if distanceCenter < distance:
            distance = distanceCenter
        return merged, distance
    
    def printRecursiveCalls(self):
        print('ClosestDistance', self.recursiveCalls)

