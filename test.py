def testCoinchange():
    import coinchange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinchange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')

def testRecIntMult():
    import recintmult
    a = 11111111
    b = 11111111
    r = recintmult.RecIntMult()
    result = r.solve(a, b)
    print(result)

testRecIntMult()
