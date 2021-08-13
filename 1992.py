import sys

input = sys.stdin.readline

N = int(input())
incode = [list(map(int, input().rstrip())) for _ in range(N)]

zero = 0
one = 0


def incoding(x, y, n):
    global zero, one
    for i in range(x, x + n):
        for j in range(y, y + n):
            if incode[x][y] != incode[i][j]:
                n = n // 2
                print('(', end='')
                incoding(x, y, n)
                incoding(x, y + n, n)
                incoding(x + n, y, n)
                incoding(x + n, y + n, n)
                print(')', end='')
                return
    if incode[x][y] == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return


incoding(0, 0, N)
