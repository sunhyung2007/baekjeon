import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sequence = []
check = [False] * n

def seq(ch,cnt):
    if ch == m:
        print(' '.join(map(str, sequence)))
        return

    for i in range(cnt, n):
        if not check[i]:
            sequence.append(i+1)
            seq(ch+1, i)
            sequence.pop()

seq(0, 0)
