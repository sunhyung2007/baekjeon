import sys

input = sys.stdin.readline

N = int(input())
Map = [list(map(int, input().rstrip())) for i in range(N)]
visited_map = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
apart_list = []


def dfs(a, b, number):
    global apart_num
    visited_map[a][b] = number  #방문한 map을 해당 단지 번호로 바꿔줌
    apart_num += 1
    for i in range(4):
        next_x = a + dx[i]
        next_y = b + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N:
            if Map[next_x][next_y] == 1 and visited_map[next_x][next_y] == 0:
                dfs(next_x, next_y, number)


apart_number = 1
apart_num = 0
for x in range(N):
    for y in range(N):
        if Map[x][y] == 1 and visited_map[x][y] == 0:
            dfs(x, y, apart_number)
            apart_list.append((apart_number, apart_num)) #단지 번호에 아파트 갯수 저장
            apart_number += 1     #하나의 단지에서 아파트를 전부 찾은 후 단지 1증가, 아파트 수 0으로 초기화
            apart_num = 0
apart_list.sort(key = lambda apart_num:apart_num[1])
print(apart_list[-1][0])
for i in range(apart_list[-1][0]):
    print(apart_list[i][1])

