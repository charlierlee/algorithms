import math
import random
import mergeSort
from functools import cmp_to_key

class Point():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def comparator(a, b):
		if a.x>b.x:
			return -1
		if a.x<b.x:
			return 1
		return 0

class PointDSelect:

	def __init__(self, items, i):
		self.recursiveCalls = 0
		self.items = items
		self.i = i # ith order statistic

	def solve(self):
		return self.solveRecursive(self.items, 0, len(self.items))

	def medianOfMedian(self, A):
		self.recursiveCalls += 1
		n = len(A)
		if n == 1:
			return A[0]
		C = [0] * math.ceil(n/5)
		Ci = 0
		chunks = self.chunks(A,5)
		for k, x in enumerate(chunks):
			lst = sorted(x, key=cmp_to_key(Point.comparator))
			mid = len(lst)//2
			C[Ci] = lst[mid]
			Ci += 1
		return self.medianOfMedian(C)

	def dChoosePivot(self, A, l, r):
		#tmp = [0] * (r - l)
		#tmpi = 0
		#for k in range(l,r):
		#    tmp[tmpi] = A[k]
		#    tmpi += 1
		tmp = list(self.section(A,l,r))
		median = self.medianOfMedian(tmp)
		return A.index(median)

	def rChoosePivot(self, l, r):
		return random.randint(l, r-1)

	def section(self, lst, l,r):
		for i in range(l, r):
			yield lst[i]

	def chunks(self, lst, n):
		"""Yield successive n-sized chunks from lst."""
		for i in range(0, len(lst), n):
			yield lst[i:i + n]

	def swap(self, A, l, r):
		temp = A[l]
		A[l] = A[r]
		A[r] = temp
		return A

	def partition(self, A, l, r):
		p = A[l]
		i = l + 1
		for j in range(l+1,r):
			if A[j].x < p.x:
				A = self.swap(A, j, i)
				i += 1
			j += 1
		A = self.swap(A, l, i-1)
		return A, i-1

	def solveRecursive(self, A, l, r):
		self.recursiveCalls += 1
		if l >= r:
			return A[0]
			
		i = self.dChoosePivot(A, l, r)

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
