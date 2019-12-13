#!/usr/bin/python2
test_input_triangle = """
   3
  7 4
 2 4 6
8 5 9 3
"""

input_triangle = '''
              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

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
