import pickle as pickle
class CoinChange:
    def memoize(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = pickle.dumps(args) + pickle.dumps(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

    @memoize
    def solve(self, coins, amount):
        if len(coins) == 0:
            return 0
        if len(coins) == 1: #if exact change remaining
            return 1 if amount % coins[0] == 0 else 0
        current_coins, remaining_coins = coins[0], coins[1:]
        i = 0
        ways = 0
        while amount - i * current_coins >= 0:
            ways+=self.solve(remaining_coins, amount - i * current_coins)
            i+=1
        return ways
    memoize = staticmethod( memoize )
