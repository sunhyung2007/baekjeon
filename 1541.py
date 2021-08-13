import sys
input = sys.stdin.readline
a = "15-14+17"
b = a.split('-')
if b == a:
    b = list(map(int, a.split('+')))
    sum = sum(b)
else:
    c = b.split('+')
    sum = sum(c[1:])
print(sum)