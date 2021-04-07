import coinchange
coins = [2, 5, 3, 7, 9]
capacity = 1000
c = coinchange.CoinChange()
result = c.solve(coins, capacity)
print(result, 'combinations')
