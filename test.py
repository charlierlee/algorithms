def testCoinchange():
    import coinchange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinchange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')


def testRecIntMult(a, b):
    import recintmult
    r = recintmult.RecIntMult(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

def testKaratsuba(a, b):
    import karatsuba
    r = karatsuba.Karatsuba(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

a, b = 1234, 5678
testRecIntMult(a, b)
testKaratsuba(a, b)
