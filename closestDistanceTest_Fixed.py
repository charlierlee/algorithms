# A divide and conquer program in Python3
# to find the smallest distance from a
# given set of points.
import math
import copy
# A class to represent a Point in 2D plane
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

# A utility function to find the
# distance between two points
def dist(p1, p2):
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y))

# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def bruteForce(P):
	n = len(P)
	min_val = float('inf')
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j]) < min_val:
				min_val = dist(P[i], P[j])

	return min_val

def stripClosest(xy_arr_y_sorted, dmin):
	# takes in array sorted in y, and minimum distance of n/2 halves
	# for each point it computes distance to 7 subsequent points
	# output min distance encountered

	dmin_rec = dmin
	if len(xy_arr_y_sorted) == 1:
		return math.inf

	if len(xy_arr_y_sorted) > 7:            
		for i, pnt_i in enumerate(xy_arr_y_sorted[:-7]):
			dis_storage_min = math.inf
			for pnt_j in xy_arr_y_sorted[i+1:i+1+7]:
				dis_storage_min = dist(pnt_i, pnt_j)
				if dis_storage_min < dmin_rec:
					dmin_rec = dis_storage_min
			if dis_storage_min < dmin_rec:
				dmin_rec = dis_storage_min
		dis_storage_min = bruteForce(xy_arr_y_sorted[-7:])
		if dis_storage_min < dmin_rec:
			dmin_rec = dis_storage_min
	else:
		for k, pnt_k in enumerate(xy_arr_y_sorted[:-1]):    
			dis_storage_min = math.inf
			for pnt_l in xy_arr_y_sorted[k+1:]:
				dis_storage_min = dist(pnt_k, pnt_l)
				if dis_storage_min < dmin_rec:
					dmin_rec = dis_storage_min 
			if dis_storage_min < dmin_rec:
				dmin_rec = dis_storage_min 
	return dmin_rec

# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def closestUtil(P, Q, n):
	
	# If there are 2 or 3 points,
	# then use brute force
	if n <= 3:
		return bruteForce(P)

	# Find the middle point
	mid = n // 2
	midPoint = P[mid]

	#keep a copy of left and right branch
	Pl = P[:mid]
	Pr = P[mid:]

	# Consider the vertical line passing
	# through the middle point calculate
	# the smallest distance dl on left
	# of middle point and dr on right side
	dl = closestUtil(Pl, Q, mid)
	dr = closestUtil(Pr, Q, n - mid)

	# Find the smaller of two distances
	d = min(dl, dr)

	# Build an array strip[] that contains
	# points close (closer than d)
	# to the line passing through the middle point
	# Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    #stripP = []
	stripQ = []
	lr = Pl + Pr
	x_space = abs(midPoint.x - d)*2
	for i in range(n):
		if abs(Q[i].x - midPoint.x) <= x_space:
			stripQ.append(Q[i])

	return min(d, stripClosest(stripQ, d))

# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def closest(P, n):
	P.sort(key = lambda point: point.x)
	Q = copy.deepcopy(P)
	Q.sort(key = lambda point: point.y)

	# Use recursive function closestUtil()
	# to find the smallest distance
	return closestUtil(P, Q, n)

# Driver code
P = [Point(2, 3), Point(12, 30),
	Point(40, 50), Point(5, 1),
	Point(12, 10), Point(3, 4)]
n = len(P)
print("The smallest distance is",
				closest(P, n))
