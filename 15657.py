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

def seq(ch,cnt):
    if ch == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(cnt, n):
        if not check[i]:
            sequence.append(num[i])
            seq(ch + 1, i)
            sequence.pop()
seq(0,0)