# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?


def succ(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1


def get(l, n):
    if n < len(l):
        return l[n]
    else:        
        new_length = n - len(l) + 1
        l += [-1] * new_length
        return -1


def collatz(n, lengths):
    l = get(lengths, n)
    if l == -1:
        lengths[n] = collatz(succ(n), lengths) + 1
        return lengths[n]
    else:
        return l


max_starting_number = 1000000

lengths = [-1] * max_starting_number
lengths[0] = 0
lengths[1] = 1


for i in range(2, max_starting_number):
    collatz(i, lengths)


max_index, max_value = max(enumerate(lengths), key=lambda p: p[1])
print max_index
print max_value