import pickle as pickle
import math
class RecIntMult:
    def memoize(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = pickle.dumps(args) + pickle.dumps(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

    def __init__(self, inputA, inputB):
        self.inputA = inputA
        self.inputB = inputB
        self.inputA, self.inputB = str(self.inputA), str(self.inputB)
        while len(self.inputA) < len(self.inputB) or not self.isPowerOfTwo(len(self.inputA)):
            self.inputA = "0" + str(self.inputA)
        while len(self.inputB) < len(self.inputA) or not self.isPowerOfTwo(len(self.inputB)):
            self.inputB = "0" + str(self.inputB)
        if not self.isPowerOfTwo(len(self.inputA)):
            raise Exception("Digits not a power of 2", self.inputA) 
        if not self.isPowerOfTwo(len(self.inputB)):
            raise Exception("Digits not a power of 2", self.inputB)
        if len(self.inputA) != len(self.inputB):
            raise Exception("input size must match", self.inputA, self.inputB)

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
    def splitString(self,s):
        return s[:len(s)//2], s[len(s)//2:]

    def solve(self):
        return self.solveRecursive(self.inputA, self.inputB)
        
    @memoize
    def solveRecursive(self, inputA, inputB):
        n = len(inputA)
        if n <= 1:
            return int(inputA)*int(inputB)
        a, b = self.splitString(inputA)
        c, d = self.splitString(inputB)
        ac = self.solveRecursive(a,c)
        ad = self.solveRecursive(a,d)
        bc = self.solveRecursive(b,c)
        bd = self.solveRecursive(b,d)
        return 10**n * ac + 10**(n/2) * (ad + bc) + bd
    memoize = staticmethod( memoize )
