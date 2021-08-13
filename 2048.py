import sys

N = int(sys.stdin.readline())
Board = [list(sys.stdin.readline().split()) for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_num = 0
stack = []

def move(x,y,dx,dy):
    while Board[x+dx][y+dy] == 0 and (0 < x + dx < N + 1) and (0 < y + dy < N + 1):
        Board[x][y] = 0
        x += dx
        y += dy

    if Board[x][y] == Board[x+dx][x+dy]:
        Board[x+dx][y+dy] *= 2

        return x, y
def find_max(x,y,max,cnt):
    while x < N and y < N and cnt <= 5:
        if Board[x][y] > max:
            max = Board[x][y]
            max.append((max, x, y))
        else:
            x += 1
            if x > N:
                x = 0
                y += 1

