#!/usr/bin/python3

# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:
#      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


coins = [1, 2, 5, 10, 20, 50, 100, 200]

# This recursion is to deep to solve in sensible time
# it will only work for small amount.
def create_ways(amount):
    ways = set()

    if amount in coins:
        ways.add((amount,))

    for coin in coins:
        previous_amount = amount - coin

        if previous_amount > 0:
            previous_ways = create_ways(previous_amount)
            new_ways = {tuple(sorted(way + (coin,))) for way in previous_ways}
            ways.update(new_ways)

    return ways


# Version with memoization still to slow
def create_ways_memo(amount, memo):
    if amount in memo:
        return memo[amount]

    ways = set()

    if amount in coins:
        ways.add((amount,))

    for coin in coins:
        previous_amount = amount - coin

        if previous_amount > 0:
            previous_ways = create_ways(previous_amount)
            new_ways = {tuple(sorted(way + (coin,))) for way in previous_ways}
            ways.update(new_ways)

    memo[amount] = ways
    return ways
 

# Non recursive version that test every solution.
# Still to slow
def create_ways_forward(amount):
    remaining_ways = [(0, tuple())]
    found_ways = set()

    while len(remaining_ways) > 0:
        way = remaining_ways.pop()
        for coin in coins:
            new_sum = way[0] + coin
            if new_sum < amount:
                new_decomposition = way[1] + (coin,)
                remaining_ways.append((new_sum, new_decomposition))
            elif new_sum == amount:
                new_decomposition = tuple(sorted(way[1] + (coin,)))
                found_ways.add(new_decomposition)
    
    return found_ways


# Non recursive version that test every solution.
# list coins must be sorted
def create_ways_increasing(amount):
    remaining_ways = [(c, (c,)) for c in coins]
    found_ways = []

    while len(remaining_ways) > 0:
        way = remaining_ways.pop()
        last_coin_idx = coins.index(way[1][-1])
        for i in range(last_coin_idx, len(coins)):
            new_sum = way[0] + coins[i]
            if new_sum < amount:
                new_decomposition = way[1] + (coins[i],)
                remaining_ways.append((new_sum, new_decomposition))
            elif new_sum == amount:
                new_decomposition = way[1] + (coins[i],)
                found_ways.append(new_decomposition)
    
    return found_ways


ways = create_ways_forward(6)
print(f"{len(ways)}: {ways}")

ways = create_ways_increasing(200)
print(f"{len(ways)}")
