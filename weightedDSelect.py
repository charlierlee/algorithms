import math
import random
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

class WeightedDSelect:

	def __init__(self, items):
		self.recursiveCalls = 0
		self.items = items
		self.total = 0
		self.Dl = 0
		self.Dr = 0
		self.Wl = 0
		self.Wr = 0

	def solve(self):
		for i in range(0,len(self.items)):
			self.total += self.items[i].y
		print(self.total)
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

	def generalRecursive(self, A, l, r, Dl, Dr):
		self.recursiveCalls += 1
		if l >= r:
			return A[0]
			
		index = self.dChoosePivot(A, l, r)

		A = self.swap(A, l, index)
		A, j = self.partition(A, l, r)
		Wl = 0
		Wr = 0
		for i in range(l,j):
			Wl += A[i].y
		for i in range(j+1,r):
			Wl += A[i].y
		print(Dl,Dr)
		if Wl == self.total / 2 and Wr == self.total / 2:
			print('aj')
			return A[j]
		elif self.Wl > self.total / 2:
			tmp = self.solveRecursive(A, l, j)
			self.Wr += tmp.y
			self.Wl -= tmp.y
			return tmp
		else:
			tmp = self.solveRecursive(A, j+1, r)
			self.Wl += tmp.y
			self.Wr -= tmp.y
			return tmp
			
	def solveRecursive(self, A, l, r):
		self.recursiveCalls += 1
		if l >= r:
			return A[0]
		A = list(self.section(A,l,r))
		l = 0
		r = len(A)
		if r == 1:
			print('r == 1')
			return A[0]
		import pointDSelect
		obj = pointDSelect.PointDSelect(A,len(A)//2)
		median = obj.solve()
		print('median.x',median.x)
		index = A.index(median)


		A = self.swap(A, l, index)
		A, j = self.partition(A, l, r)
		i = l
		while self.Dl + A[i].y <= self.total / 2 and i < j:
			self.Dl += A[i].y
			i += 1
		ii = j+1
		while self.Dr + A[ii].y <= self.total / 2 and ii < r:
			self.Dr += A[ii].y
			ii += 1
		print(self.Dl,self.Dr)
		if self.Dl == self.total / 2 and Dr == self.total / 2:
			print('aj')
			return A[j]
		elif i < j:
			print('i,j',i,j)
			tmp = self.solveRecursive(A, i, j)
			return tmp
		elif ii < r:
			print('ii,r',ii,r)
			tmp = self.solveRecursive(A, ii, r)
			
			return tmp
		

	
	def printRecursiveCalls(self):
		print('WeightedDSelect', self.recursiveCalls, 'completed')
