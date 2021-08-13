import sys

input = sys.stdin.readline

n, m = map(int, input().split())
check = [False] * n
sequence = []


def seq(ch):
    if ch == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(n):
        if not check[i]:
            sequence.append(i + 1)
            seq(ch + 1)
            sequence.pop()

seq(0)
