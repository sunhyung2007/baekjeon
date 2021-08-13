import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while len(deque) != 1:
    deque.popleft()
    next = deque.popleft()
    deque.append(next)
print(deque[0])
