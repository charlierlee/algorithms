
def testCoinchange():
    import coinChange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinChange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')


def testRecIntMult(a, b):
    import recIntMult
    r = recIntMult.RecIntMult(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

def testKaratsuba(a, b):
    import karatsuba
    r = karatsuba.Karatsuba(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

def testMergeSort():
    import mergeSort
    import random
    a = [random.randrange(1, 100, 1) for i in range(100)]
    print(len(a))
    tA = mergeSort.MergeSort(a)
    testA = tA.solve()
    
    from sorting_techniques import pysort
    sortObj = pysort.Sorting()
    testB = sortObj.mergeSort(a)
    if len(testA) != len(testB):
        print('array not equal', len(testA), len(testB))
        return
    for i in range(len(a)):
        print(testA[i], testB[i])
        if (testA[i]) != (testB[i]):
            print("error")
    tA.printRecursiveCalls()
    
testMergeSort()