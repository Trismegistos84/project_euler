#!/usr/bin/python2
input_triangle = file('p067_triangle.txt').read()


def parse_triangle(input_triangle):
    toint = lambda xs: [int(x) for x in xs]
    lines = input_triangle.splitlines()
    triangle = [line.strip().split() for line in lines]
    return [toint(line) for line in triangle if len(line) > 0]    


def reduce_last_line(triangle):
    last = triangle.pop()
    before_last = triangle.pop()

    for i in range(len(before_last)):
        before_last[i] += max(last[i], last[i+1])

    triangle.append(before_last)


def reduce_triangle(triangle):
    for i in range(len(triangle) - 1):
        reduce_last_line(triangle)


triangle = parse_triangle(input_triangle)
reduce_triangle(triangle)
print triangle
