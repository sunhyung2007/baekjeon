import sys

input = sys.stdin.readline

N = int(input())
first = 1
second = 2
for i in range(2, N):
    temp = first
    first = second
    second += temp
if N == 1:
    print(first)
else:
    print(second)