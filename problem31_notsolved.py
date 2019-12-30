#!/usr/bin/python3

# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:
#      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


coins = [1, 2, 5, 10, 20, 50, 100, 200]
#ways = [1] + [0] * 200

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
            


print(create_ways(5))
