import sys

input = sys.stdin.readline

R, C = map(int, input().split())
map = [list(input().rstrip()) for _ in range(R)]
num = [0 for _ in range(26)]
num[ord(map[0][0]) - 65] = 1
cnt = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(ch, x, y):
    global cnt
    if cnt < ch:
        cnt = ch
    for i in range(4):
        if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C and num[ord(map[x + dx[i]][y + dy[i]]) - 65] == 0:
            num[ord(map[x + dx[i]][y + dy[i]]) - 65] = 1
            dfs(ch + 1, x + dx[i], y + dy[i])
            num[ord(map[x + dx[i]][y + dy[i]]) - 65] = 0


dfs(1, 0, 0)
print(cnt)
