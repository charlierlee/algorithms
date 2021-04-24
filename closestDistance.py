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
        return self.solveRecursive(self.A, self.B, len(self.A))

    def splitArray(self,arrA,arrB):
        m = len(arrA)//2
        return arrA[:m], arrB[:m], arrA[m:], arrB[m:]
        
    # A Brute Force method to return the
    # smallest distance between two points
    # in P[] of size n
    def bruteForce(self, P, n, min_val=float('inf')):
        best = []
        for i in range(n):
            for j in range(i + 1, n):
                min_distance = self.dist(P[i], P[j])
                if min_distance < min_val:
                    min_val = self.dist(P[i], P[j])
                    best = [P[i], P[j]]
        return best, min_val

    def solveRecursive(self, x, y, n):
        self.recursiveCalls += 1
        n = len(x)
        if n == 0:
            raise Exception('n=0')
        # If there are 2 or 3 points, 
        # then use brute force 
        if n <= 3:
            return self.bruteForce(x, n)

        mid = n//2
        #midPoint = x[mid-1]

        Lx, Ly, Rx, Ry = self.splitArray(x,y)
        l12, bestL = self.solveRecursive(Lx, Ly, mid)
        r12, bestR = self.solveRecursive(Rx, Ry, n - mid)
        bestP = []
        best = math.inf
        if bestL < bestR:
            bestP = l12
            best = bestL
        else:
            bestP = r12
            best = bestR
        s12, bestS = self.merge(Lx, Rx, Ly, Ry, best, n)
        if bestS < best:
            bestP = s12
            best = bestS
        return bestP, best
    def merge(self, Lx, Rx, Ly, Ry, lr_d, n):
        midPoint = Lx[len(Lx)-1]
        Sx = []
        Px = [0] * n
        i, j = 0, 0
        Lx = Lx + [Point(math.inf,math.inf)]
        Rx = Rx + [Point(math.inf,math.inf)]
        for k in range(0, n):
            if Lx[i].x < Rx[j].x:
                Px[k] = Lx[i]
                i+=1
            else:
                Px[k] = Rx[j]
                j+=1
        
            if abs(Px[k].x - midPoint.x) < lr_d: 
                Sx.append(Px[k])

        Sx.sort(key = lambda point: point.y) #<-- REQUIRED

        bestL, lr_d2 = self.stripClosest(Sx, len(Sx), [], lr_d)

        Sy = []
        Py = [0] * n
        Ly = Ly + [Point(math.inf,math.inf)]
        Ry = Ry + [Point(math.inf,math.inf)]
        i, j = 0, 0
        
        leftside = abs(midPoint.x - lr_d)
        for k in range(0, n):
            if Ly[i].y < Ry[j].y:
                Py[k] = Ly[i]
                i+=1
            else:
                Py[k] = Ry[j]
                j+=1
            if abs(Py[k].x - midPoint.x) < leftside: 
                Sy.append(Py[k])
        best, lr_d = self.stripClosest(Sy, len(Sy), bestL, lr_d)

        if lr_d2 < lr_d:
            best = bestL
            lr_d = lr_d2
        return best, lr_d
    
    def stripClosest(self, strip, size, best, min_dis):
        '''
        for i in range(min(6, size - 1), size):
            for j in range(max(0, i - 6), i):
                current_dis = self.dist(strip[i],strip[j])
                if current_dis < min_dis:
                    min_dis = current_dis
                    best = [strip[i], strip[j]]
        return best, min_dis
        '''
        for i in range(size):
            j = i + 1
            while j < size and (dist := self.dist(strip[i],strip[j])) < min_dis: 
                min_dis = dist
                best = [strip[i], strip[j]]
                j += 1
        return best, min_dis
