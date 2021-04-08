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
    @memoize
    def solve(self, inputA, inputB):
        inputADigits = len(str(inputA))
        inputBDigits = len(str(inputB))
        if not self.isPowerOfTwo(inputADigits):
            raise Exception("Not a power of 2", inputADigits) 
        if not self.isPowerOfTwo(inputBDigits):
            raise Exception("Not a power of 2", inputBDigits)
        if inputADigits != inputBDigits:
            raise Exception("input size must match", inputADigits, inputBDigits)
        n = inputADigits
        print(n)
        if len(str(inputA)) <= 1:
            return inputA*inputB
        inputAString, inputBString = str(inputA), str(inputB)
        a, b = self.splitString(inputAString)
        a, b = int(a), int(b)
        c, d = self.splitString(inputBString)
        c, d = int(a), int(b)
        ac = self.solve(a,c)
        ad = self.solve(a,d)
        bc = self.solve(b,c)
        bd = self.solve(b,d)
        return 10**n * ac + 10**(n/2) * (ad + bc) + bd
    memoize = staticmethod( memoize )
