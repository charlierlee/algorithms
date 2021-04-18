
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
    a = [random.randrange(1, 100, 1) for i in range(100)]
    tA = mergeSort.MergeSort(a)
    testA = tA.solve()
    
    from sorting_techniques import pysort
    sortObj = pysort.Sorting()
    testB = sortObj.mergeSort(a)
    if len(testA) != len(testB):
        print('array not equal', len(testA), len(testB))
        return
    for i in range(len(a)):
        if (testA[i]) != (testB[i]):
            print("error")
    tA.printRecursiveCalls()

def testCountInversions():
    import countInversions
    import random
    a = []
    start, end = 1, 256
    for num in range(start, end + 1):
        if num % 2 != 0:
            a.append(num)
    for num in range(start, end + 1):
        if num % 2 == 0:
            a.append(num)
    #a = [random.randrange(1, 9, 1) for i in range(9)]
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

testCountInversions()