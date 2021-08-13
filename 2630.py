import sys

input = sys.stdin.readline

N = int(input())

blue = 0
white = 0

paper = [list(map(int, input().split())) for _ in range(N)]


def divide(x, y, n):
    global blue, white
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                n = n // 2
                divide(x, y, n)
                divide(x, y + n, n)
                divide(x + n, y, n)
                divide(x + n, y + n, n)
                return
    if paper[x][y] == 0:
        white += 1
    else:
        blue += 1


divide(0, 0, N)
print(white)
print(blue)
