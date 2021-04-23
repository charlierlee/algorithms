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

    def splitArray(self,arrA):
        return arrA[:len(arrA)//2], arrA[len(arrA)//2:]

    def solveRecursive(self, arrA, arrB):
        self.recursiveCalls += 1
        n = len(arrA)
        if n == 0:
            raise Exception('n=0')
        # If there are 2 or 3 points, 
        # then use brute force 
        if n <= 3:
            min_val = self.bruteForce(arrA, n)
            #baseCaseR, min_r = self.bruteForce(arrB, n)
            return arrA, min_val

        mid = n // 2
        midPoint = arrA[mid]
        leftA, rightA = self.splitArray(arrA)
        dividedLeftA, distLeftA = self.solveRecursive(leftA, arrB)
        dividiedRightA, distRightA = self.solveRecursive(rightA, arrB)
        mergedA, merge_min = self.merge(dividedLeftA,dividiedRightA, distLeftA, distRightA, n, midPoint, arrB)
        return mergedA, merge_min

    def merge(self, a, b, distLeftA, distRightA, n, midPoint, Q):
        lr_d = min(distLeftA, distRightA)

        m = n//2
        inversionCount = 0
        result = [0] * n
        a = a + [Point(math.inf,math.inf)]
        b = b + [Point(math.inf,math.inf)]
        i, j = 0, 0
        stripA = []
        stripB = []
        for k in range(0, n):
            if a[i].x < b[j].x:
                result[k] = a[i]
                i+=1
            else:
                result[k] = b[j]
                inversionCount += n//2 - i
                if inversionCount > 0:
                    raise Exception('inversionCount increased. List is not sorted')
                j+=1

            if abs(result[k].x - midPoint.x) < lr_d: 
                stripA.append(result[k])
            if abs(Q[k].x - midPoint.x) < lr_d: 
                stripB.append(Q[k])
        
        #REQUIRED 
        # because: while j < size and (dist := self.dist(strip[j],strip[i])) < min_val
        # meaning this will stop the moment it finds the first y value that is less than
        # min_val (or it gets to the end of the list). See stripClosest for more info
        stripA.sort(key = lambda point: point.y)

        min_a = self.stripClosest(stripA, len(stripA), lr_d)
        min_b = self.stripClosest(stripB, len(stripB), lr_d)
        
        return result, min(min_a, min_b)

    # A Brute Force method to return the
    # smallest distance between two points
    # in P[] of size n
    def bruteForce(self, P, n, min_val=float('inf')):
        for i in range(n):
            for j in range(i + 1, n):
                min_distance = self.dist(P[i], P[j])
                if min_distance < min_val:
                    min_val = self.dist(P[i], P[j])
        return min_val
    
    # A utility function to find the 
    # distance beween the closest points of 
    # strip of given size. All points in 
    # strip[] are sorted accordint to 
    # y coordinate. They all have an upper 
    # bound on minimum distance as d. 
    # Note that this method seems to be 
    # a O(n^2) method, but it's a O(n) 
    # method as the inner loop runs at most 6 times
    # IMPORTANT: Preprocessing Ruequired: strip must be sorted by 'y' point asc
    def stripClosest(self, strip, size, d):
        
        # Initialize the minimum distance as d 
        min_val = d 
    
        # Pick all points one by one and 
        # try the next points till the difference 
        # between y coordinates is smaller than d. 
        # This is a proven fact that this loop
        # runs at most 6 times 
        for i in range(size):
            j = i + 1
            while j < size and (dist := self.dist(strip[j],strip[i])) < min_val: 
                min_val = dist
                j += 1
    
        return min_val 
