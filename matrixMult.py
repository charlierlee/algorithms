import pickle as pickle
import math
import numpy as np
class MatrixMult:
    def memoize(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = pickle.dumps(args) + pickle.dumps(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

    def __init__(self, X, Y):
        self.recursiveCalls = 0
        self.X = X
        self.Y = Y
        if not self.isPowerOfTwo(len(self.X)):
            raise Exception("Array Length not a power of 2", self.X) 
        if not self.isPowerOfTwo(len(self.Y)):
            raise Exception("Array Length not a power of 2", self.Y)
        if len(self.X) != len(self.Y):
            raise Exception("Matrix is not square", self.X, self.Y)

    def Log2(self,x):
        if x == 0:
            return False
        return (math.log10(x) /
                math.log10(2))
    # Function to check
    # if x is power of 2
    def isPowerOfTwo(self,n):
        return (math.ceil(self.Log2(n)) ==
                math.floor(self.Log2(n)))
    #Splitting string into equal halves
    def splitString(self,xs):
        x = len(xs)//2
        y = len(xs)//2
        #bl = bottom left, in latax it is top right
        #tr = top right, in latax it is bottom left
        tl,bl,tr,br = xs[:x, :y], xs[:x, y:], xs[x:, :y], xs[x:, y:]
        return tl,bl,tr,br

    def solve(self):
        return self.solveRecursive(self.X, self.Y)
        
    @memoize
    def solveRecursive(self, X, Y):
        self.recursiveCalls += 1
        n = len(X)
        if n == 0:
            raise Exception("this should not happen")
        if n == 1:
            return X[0][0] * Y[0][0]
        a, b, c, d = self.splitString(X)
        e, f, g, h = self.splitString(Y)

        p1 = self.solveRecursive(a,f - h)
        p2 = self.solveRecursive(a + b,h)
        p3 = self.solveRecursive(c + d, e)
        p4 = self.solveRecursive(d,g - e)
        p5 = self.solveRecursive(a + d,e + h)
        p6 = self.solveRecursive(b - d,g + h)
        p7 = self.solveRecursive(a - c,e + f)
        
        tl = p5 + p4 - p2 + p6
        bl = p3 + p4
        tr = p1 + p2
        br = p1 + p5 - p3 - p7
        #bl = in latax it is top right
        #tr = in latax it is bottom left
        return np.vstack([np.hstack([tl, bl]), np.hstack([tr, br])])

    def printRecursiveCalls(self):
        print('matrixMult', self.recursiveCalls)
    memoize = staticmethod( memoize )
