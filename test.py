def testCoinchange():
    import coinchange
    coins = [2, 5, 3, 7, 9]
    capacity = 1000
    c = coinchange.CoinChange()
    result = c.solve(coins, capacity)
    print(result, 'combinations')

def testRecIntMult():
    import recintmult
    a = 1
    b = 5678
    r = recintmult.RecIntMult(a,b)
    result = r.solve()
    print(result)

testRecIntMult()
