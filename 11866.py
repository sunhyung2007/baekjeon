import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
deque = deque([])
for i in range(1, N+1):
    deque.append(i)

print('<', end='')
while deque:
    for j in range(K-1):
        deque.append(deque[0])
        deque.popleft()
    print(deque.popleft(), end='')
    if deque:
        print(',', end='')
print('>')