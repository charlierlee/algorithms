import math
import copy
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class ClosestDistance:

    def dist(self, p1, p2):
        return math.sqrt((p1.x - p2.x) *
                        (p1.x - p2.x) +
                        (p1.y - p2.y) *
                        (p1.y - p2.y))
                        
    def __init__(self, items):
        self.recursiveCalls = 0
        self.A = sorted(items, key=lambda point: point.x)
        self.B = sorted(items, key=lambda point: point.y)

    def solve(self):
        return self.solveRecursive(self.A, self.B)

    def splitArray(self,arrA, arrB):
        return arrA[:len(arrA)//2], arrA[len(arrA)//2:], arrB[:len(arrB)//2], arrB[len(arrB)//2:]

    def solveRecursive(self, arrA, arrB):
        self.recursiveCalls += 1
        n = len(arrA)
        baseCaseA = []
        baseCaseB = []
        if n == 0:
            raise Exception('n=0')
        if n == 1:
            raise Exception('n=1')
        if n == 2:
            return arrA, arrB, self.dist(arrA[0], arrA[1]), self.dist(arrB[0], arrB[1])

        leftA, rightA, leftB, rightB = self.splitArray(arrA, arrB)
        dividedLeftA, dividedLeftB, distLeftA, distLeftB = self.solveRecursive(leftA, leftB)
        dividiedRightA, dividedRightB, distRightA, distRightB = self.solveRecursive(rightA, rightB)
        mergedA, mergedB, mergeCount = self.merge(dividedLeftA,dividiedRightA,dividedLeftB,dividedRightB, distLeftA, distLeftB, distRightA,distRightB, n)
        return mergedA, mergedB, mergeCount, mergeCount

    def merge(self, la, ra, lb, rb, distLeftA, distLeftB, distRightA, distRightB, n):
        min_distance = math.inf
        if distLeftA < min_distance:
            min_distance = distLeftA
        if distLeftB < min_distance:
            min_distance = distLeftB
        if distRightA < min_distance:
            min_distance = distRightA
        if distRightB < min_distance:
            min_distance = distRightB
        resultX = [0] * n
        resultY = [0] * n
        la = la + [Point(0,0)]
        ra = ra + [Point(math.inf,math.inf)]
        lb = lb + [Point(0,0)]
        rb = rb + [Point(math.inf,math.inf)]
        i, j = 0, 0
        for k in range(0, n):
            d1, d2 = self.dist(la[i],ra[i]), self.dist(lb[j],rb[j])
            if d1 < d2:
                resultX[k] = la[i]
                resultY[k] = ra[i]
                i+=1
                if d1 < min_distance:
                    min_distance = d1
            else:
                resultX[k] = lb[j]
                resultY[k] = rb[j]
                if d2 < min_distance:
                    min_distance = d2
                j+=1
        return resultX, resultY, min_distance