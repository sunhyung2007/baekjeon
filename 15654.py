import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sequence = []
check = [False] * n

for i in range(1, n):
    key = num[i]
    j = i
    while j > 0 and num[j - 1] > key:
        num[j] = num[j - 1]
        j -= 1
    num[j] = key

def seq(ch):
    if ch == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(n):
        if not check[i]:
            check[i] = True
            sequence.append(num[i])
            seq(ch + 1)
            check[i] = False
            sequence.pop()

seq(0)