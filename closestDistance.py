import math
import copy
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class ClosestDistance:

    # A utility function to find the 
    # distance between two points 
    def dist(self, p1, p2):
        return math.sqrt((p1.x - p2.x) * 
                        (p1.x - p2.x) +
                        (p1.y - p2.y) * 
                        (p1.y - p2.y)) 
    
    # A Brute Force method to return the 
    # smallest distance between two points 
    # in P[] of size n
    def bruteForce(self, P, n):
        min_val = float('inf') 
        for i in range(n):
            for j in range(i + 1, n):
                if self.dist(P[i], P[j]) < min_val:
                    min_val = self.dist(P[i], P[j])
    
        return min_val
    
    # A utility function to find the 
    # distance beween the self.closest points of 
    # strip of given size. All points in 
    # strip[] are sorted accordint to 
    # y coordinate. They all have an upper 
    # bound on minimum distance as d. 
    # Note that this method seems to be 
    # a O(n^2) method, but it's a O(n) 
    # method as the inner loop runs at most 6 times
    def stripClosest(self, strip, size, d):
    
        # Initialize the minimum distance as d 
        min_val = d 

        for i in range(size):
            j = i + 1
            while j < size:
                dist = self.dist(strip[i], strip[j])
                if dist < min_val:
                    min_val = dist
                j += 1

        return min_val 
    
    # A recursive function to find the 
    # smallest distance. The array P contains 
    # all points sorted according to x coordinate
    def closestUtil(self, P, Q, n):
        
        # If there are 2 or 3 points, 
        # then use brute force 
        if n <= 3: 
            return self.bruteForce(P, n) 
    
        # Find the middle point 
        mid = n // 2
        midPoint = P[mid]
    
        # Consider the vertical line passing 
        # through the middle point calculate 
        # the smallest distance dl on left 
        # of middle point and dr on right side 
        l = P[:mid]
        r = P[mid:]
        dl = self.closestUtil(P[:mid], Q, mid)
        dr = self.closestUtil(P[mid:], Q, n - mid) 
    
        # Find the smaller of two distances 
        d = min(dl, dr)
    
        # Build an array strip[] that contains 
        # points close (closer than d) 
        # to the line passing through the middle point 
        strip = [] 
        lr = l + r
        for i in range(n): 
            if abs(lr[i].x - midPoint.x) < d: 
                strip.append(lr[i])
        strip.sort(key = lambda point: point.y)
        min_a = min(d, self.stripClosest(strip, len(strip), d))

        strip = []   
        for i in range(n): 
            if abs(Q[i].x - midPoint.x) < d: 
                strip.append(Q[i])
        min_b = min(d, self.stripClosest(strip, len(strip), d))
        strip.sort(key = lambda point: point.y) 
        
        # Find the self.closest points in strip. 
        # Return the minimum of d and self.closest 
        # distance is strip[] 
        return min(min_a,min_b)
    
    # The main function that finds
    # the smallest distance. 
    # This method mainly uses self.closestUtil()
    def closest(self,P, n):
        P.sort(key = lambda point: point.x)
        Q = copy.deepcopy(P)
        Q.sort(key = lambda point: point.y)    
    
        # Use recursive function self.closestUtil() 
        # to find the smallest distance 
        return self.closestUtil(P, Q, n)
