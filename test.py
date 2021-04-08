def testCoinchange():
    import coinchange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinchange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')

def testRecIntMult():
    import recintmult
    a = 1234
    b = 5678
    r = recintmult.RecIntMult(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

def testKaratsuba():
    import karatsuba
    a = 1234
    b = 5678
    r = karatsuba.Karatsuba(a,b)
    result = r.solve()
    print(result)
    r.printRecursiveCalls()

testRecIntMult()
testKaratsuba()
