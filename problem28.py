#!/usr/bin/python3
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# sum([21, 7, 1, 3, 13, 25, 9, 5, 17]) == 101

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# spirala zrobiona jest z koncentrycznych pierścieni numerwanych od 0
# lp(n) -- ilość liczb w pierścienu
# lp(0) = 1
# lp(n) = 8n
# o(n) -- ostatnia liczba w pierścieniu n (n >= 0)
# o(0) = 1
# o(n) = o(n - 1) + lp(n) = 1 + 8 * nchoosek(n + 1, n - 1) = 1 + 4*n*(n + 1)

def last_number_in_ring(ring_number):
    if ring_number == 0:
        return 1
    return 1 + 4*ring_number*(ring_number+1)

def sum_of_ring_corners(ring_number):
    if ring_number == 0:
        return 1
    
    last = last_number_in_ring(ring_number)    
    ring_width = 2*ring_number + 1
        
    return 4*last - 6*ring_width + 6

width = 1001
ring_count = (width - 1) // 2 + 1

s = 0
for ring_number in range(ring_count):
    s += sum_of_ring_corners(ring_number)
    
print(s)


