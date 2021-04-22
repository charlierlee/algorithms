import time

def testCoinchange():
    import coinChange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinChange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')


def testRecIntMult():
    import recIntMult
    a = "3141592653589793238462643383279502884197169399375105820974944592"
    b = "2718281828459045235360287471352662497757247093699959574966967627"
    wolframAlpha = int("8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184")
    r = recIntMult.RecIntMult(a,b)
    result = r.solve()
    testA = int(a)*int(b)
    testB = int(result)
    print('a*b',testA)
    print('RecIntMult',testB)
    print('a*b == RecIntMult',testA == testB)
    print('wolframAlpha == RecIntMult',wolframAlpha == testB)
    r.printRecursiveCalls()
    return testA

def testKaratsuba():
    import karatsuba
    a = "3141592653589793238462643383279502884197169399375105820974944592"
    b = "2718281828459045235360287471352662497757247093699959574966967627"
    wolframAlpha = int("8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184")
    r = karatsuba.Karatsuba(a,b)
    result = r.solve()
    testA = int(a)*int(b)
    testB = int(result)
    print('a*b',testA)
    print('Karatsuba',testB)
    print('a*b == Karatsuba',testA == testB)
    print('wolframAlpha == Karatsuba',wolframAlpha == testB)
    r.printRecursiveCalls()
    return testA

def testMergeSort():
    import mergeSort
    import random
    a = random.sample(range(1, 10**18), 10**6)
    print('mergeSort started')
    tA = mergeSort.MergeSort(a)
    testA = tA.solve()
    tA.printRecursiveCalls()
    print('pysort started')
    from sorting_techniques import pysort
    sortObj = pysort.Sorting()
    testB = sortObj.mergeSort(a)
    print('pysort done')
    '''
    if len(testA) != len(testB):
        print('array not equal', len(testA), len(testB))
        return
    for i in range(len(a)):
        if (testA[i]) != (testB[i]):
            print("error")
    '''
    
def testMergeSort2d():
    import mergeSort2d
    import random
    A = []
    keyIndex = 0
    a = [random.randrange(1, 100, 1) for i in range(100)]
    b = [random.randrange(1, 100, 1) for i in range(100)]
    A.append(a)
    A.append(b)
    tA = mergeSort2d.MergeSort2d()
    tA.solve(A,keyIndex)
    
    from sorting_techniques import pysort
    sortObj = pysort.Sorting()
    testB = sortObj.mergeSort(A[keyIndex])
    if len(A[keyIndex]) != len(testB):
        print('array not equal', len(A[keyIndex]), len(testB))
        return
    for i in range(len(a)):
        if A[keyIndex][i] != testB[i]:
            print("error")

def testCountInversions():
    import countInversions
    import random
    a = []
    start, end = 1, 56
    for num in range(start, end + 1):
        if num % 2 != 0:
            a.append(num)
    for num in range(start, end + 1):
        if num % 2 == 0:
            a.append(num)
    #a = [1,3,5,7,2,4,6,8]
    #a = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16]
    #a = [1,2,3,4,5,6,7,8]
    a = random.sample(range(1, 10**18), 10**6)
    #print(a)
    tA = countInversions.CountInversions(a)
    testA = tA.solve()
    print(testA[1])
    def getInvCount(arr, n):
        inv_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] > arr[j]):
                    inv_count += 1
    
        return inv_count
    
    # Driver Code
    arr = a
    n = len(arr)
    print("Number of inversions are",
                getInvCount(arr, n))

def testMatrixMultNumpy():
    import matrixMultNumpy
    import numpy as np
    import random
    exponent = 7
    x = np.random.rand(2**exponent,2**exponent)
    y = np.random.rand(2**exponent,2**exponent)
    print('numpy',np.sum(np.matmul(x, y)))
    tA = matrixMultNumpy.MatrixMult(x,y)
    testA = tA.solve()
    print('testA',np.sum(testA))
    
def testMatrixMult():
    import matrixMult
    import numpy as np
    import random
    exponent = 7
    n = 2**exponent
    x = np.random.rand(2**exponent,2**exponent)
    y = np.random.rand(2**exponent,2**exponent)
    print('numpy',np.sum(np.matmul(x, y)))
    tA = matrixMult.MatrixMult(x.tolist(),y.tolist())
    testA = tA.solve()
    print('testA',np.sum(testA))

def testClostestDistance():
    import closestDistance
    import random
    import copy
    outcome = True
    while outcome == True:
        A = []
        a = random.sample(range(1, 10**18), 10**3)
        b = random.sample(range(1, 10**18), 10**3)
        a1 = copy.copy(a)
        b1 = copy.copy(b)
        a2 = copy.copy(a)
        b2 = copy.copy(b)
        a3 = copy.copy(a)
        b3 = copy.copy(b)
        #print(a)
        #print(b)
        print(2**13)
        import closestDistanceTest
        
        #a3 = [8, 50, 54, 52]

        #b3 = [41, 49, 34, 52]
        t2Result = None
        t3Result = None
        n = len(a3)
        start_time = time.time()
        P3 = [closestDistanceTest.Point(x, y) for x,y in zip(a3,b3)]
        t3 = closestDistanceTest.ClosestDistanceTest()
        t3Result = t3.bruteForce(P3, n)
        print("bruteForce smallest distance is",t3Result)
        print("--- %s seconds ---" % (time.time() - start_time))

        #a3 = [62, 41, 33, 61, 57, 63, 49, 46]
        #b3 = [1, 39, 31, 46, 58, 23, 38, 26]

        n = len(a2)
        start_time = time.time()
        P2 = [closestDistanceTest.Point(x, y) for x,y in zip(a2,b2)]
        t2 = closestDistanceTest.ClosestDistanceTest()
        t2Result = t2.closest(P2, n)
        print("baseline smallest distance is",t2Result)
        print("--- %s seconds ---" % (time.time() - start_time))

        #a1 = [8, 50, 54, 52]
        #b1 = [41, 49, 34, 52]

        #a1 = [62, 41, 33, 61, 57, 63, 49, 46]
        #b1 = [1, 39, 31, 46, 58, 23, 38, 26]

        P1 = [closestDistance.Point(x, y) for x,y in zip(a1,b1)]
        print('ClostestDistance started')
        
        start_time = time.time()
        t1 = closestDistance.ClosestDistance(P1)
        a, t1Result = t1.solve()
        print("--- %s seconds ---" % (time.time() - start_time))
        print("ClostestDistance smallest distance is",t1Result)
        outcome = False
        outcome = t1Result == t2Result == t3Result
        
        print(outcome)

#testMergeSort()
testClostestDistance()
