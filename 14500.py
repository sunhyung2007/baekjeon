import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().split(' '))) for _ in range(n)]
check = [[False] * m for _ in range(n)]
num_list = []
sum_list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

""" 길이가 4인 dfs 탐색 """
def tech_dfs(ch, x, y):
    if ch == 4:
        sum_list.append(sum(num_list))
        return
    """ 위 아래 왼쪽 오른쪽 탐색"""
    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and not check[x + dx[i]][y + dy[i]]:
            num_list.append(map[x + dx[i]][y + dy[i]])
            check[x + dx[i]][y + dy[i]] = True
            tech_dfs(ch + 1, x + dx[i], y + dy[i])
            check[x + dx[i]][y + dy[i]] = False
            num_list.pop()


""" 모양이 다른 테크노미콘 """
def other_tech(x, y):
    """ x, y 기준 양 대각 끅지점 좌표 """
    x1 = x - 1
    y1 = y - 1
    x2 = x + 1
    y2 = y + 1

    """ x, y 기준 왼쪽 위 꼭지점 기준 테크노미콘 검사 """
    if 0 <= x1 and 0 <= y1:
        """ ㅏ 모양 테크노미콘 검사 """
        if x1 + 2 < n:
            sum_list.append(map[x1][y1] + map[x1 + 1][y1] + map[x1 + 2][y1] + map[x][y])
        """ ㅜ 모양 테크노미콘 검사 """
        if y1 + 2 < m:
            sum_list.append(map[x1][y1] + map[x1][y1 + 1] + map[x1][y1 + 2] + map[x][y])

    """ x, y 기준 오른쪽 밑 꼭지점 기준 테크노미콘 검사 """
    if x2 < n and y2 < m:
        """ ㅓ 모양 테크노미콘 검사 """
        if 0 <= x2 - 2:
            sum_list.append(map[x2][y2] + map[x2 - 1][y2] + map[x2 - 2][y2] + map[x][y])
        """ ㅗ 모양 테크노미콘 검사 """
        if 0 <= y2 - 2:
            sum_list.append(map[x2][y2] + map[x2][y2 - 1] + map[x2][y2 - 2] + map[x][y])


for i in range(n):
    for j in range(m):
        tech_dfs(0, i, j)
        num_list = []
        other_tech(i, j)
print(max(sum_list))