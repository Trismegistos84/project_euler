#!/usr/bin/python2
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?


def succ(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1


def collatz(n, lengths):
    l = lengths.get(n, -1)
    if l == -1:
        lengths[n] = collatz(succ(n), lengths) + 1
        return lengths[n]
    else:
        return l


max_starting_number = 1000000 - 1
lengths = {1:1}

for i in range(2, max_starting_number + 1):
    collatz(i, lengths)

max_index, max_value = max(lengths.items(), key=lambda a: a[1])
print "index:", max_index
print "value:", max_value
print "number of times collats function was evaluated:", len(lengths)
