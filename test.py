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
    DoBruteForce = False
    while outcome == True:
        A = []
        #TODO: TEST THESE INPUTS
        #a = random.sample(range(1, 2**6), 2**4)
        #b = random.sample(range(1, 2**6), 2**4)
        
        unique_set = random.sample(range(1, 10**7), 10**6)
        a, b = unique_set[:len(unique_set)//2], unique_set[len(unique_set)//2:]

        #print(a)
        #print(b)
        a1 = copy.copy(a)
        b1 = copy.copy(b)
        a2 = copy.copy(a)
        b2 = copy.copy(b)
        a3 = copy.copy(a)
        b3 = copy.copy(b)
        print(len(a))
        print(len(b))

        baseLineResult = None
        bruteForceResult = None
        n = len(a3)
        if DoBruteForce:
            start_time = time.time()
            P3 = [closestDistanceTest.Point(x, y) for x,y in zip(a3,b3)]
            t3 = closestDistanceTest.ClosestDistanceTest()
            bruteForceResult = t3.bruteForce(P3, n)
            print("bruteForce smallest distance is",bruteForceResult)
            print("--- %s seconds ---" % (time.time() - start_time))

        n = len(a2)
        start_time = time.time()
        import closestDistanceTest
        #P2 = [closestDistanceTest.Point(x, y) for x,y in zip(a2,b2)]
        #t2 = closestDistanceTest.ClosestDistanceTest()
        baseLineResult = closestDistanceTest.find_closest_point(a2, b2)
        print("baseline smallest distance is",baseLineResult)
        print("--- %s seconds ---" % (time.time() - start_time))

        

        P1 = [closestDistance.Point(x, y) for x,y in zip(a1,b1)]
        print('ClostestDistance started') 
        start_time = time.time()
        t1 = closestDistance.ClosestDistance(P1)
        a, closestDistanceResult = t1.solve()
        print("--- %s seconds ---" % (time.time() - start_time))
        print("ClostestDistance smallest distance is",closestDistanceResult)
        outcome = False
        if DoBruteForce:
            outcome = bruteForceResult == baseLineResult
            #outcome = closestDistanceResult == bruteForceResult
        else:
            outcome = closestDistanceResult == baseLineResult
        print(outcome)

def testQuickSort():
    import quickSort
    import mergeSort
    import random
    import copy
    a = random.sample(range(1, 10**6+1), 10**6)
    #a = [3,8,2,5,1,4,7,6]
    a1 = copy.copy(a)
    b1 = copy.copy(a)
    print('quickSort started')
    tA = quickSort.QuickSort(a1)
    start_time = time.time()
    tA.solve()
    testA = a1
    #print(testA)
    print("quicksort done")
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print('mergeSort started')
    tB = mergeSort.MergeSort(b1)
    start_time = time.time()
    testB = tB.solve()
    #print(testB)
    print('mergeSort done')
    print("--- %s seconds ---" % (time.time() - start_time))
    
    if len(testA) != len(testB):
        print('array not equal', len(testA), len(testB))
        return
    for i in range(len(a)):
        if (testA[i]) != (testB[i]):
            print("error", testA[i], testB[i])

def testBirthdayProblem():
    import birthdayProblem
    import math
    n = 365
    t = birthdayProblem.BirthdayProblem(n, 1)
    result = t.solve()
    actual_value = result[0]
    dice_count = result[1]
    expected_value = result[2]
    combo_count = result[3]
    print('actual_value',actual_value)
    print('dice_count', dice_count)
    print('expected_value', expected_value)
    print('combo_count', combo_count)
    print('math.comb(n,k)(',dice_count,',',2,')',math.comb(dice_count,2))

testBirthdayProblem()
