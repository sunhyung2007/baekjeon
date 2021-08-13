import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Map = [list(input().rstrip()) for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False] * M for i in range(N)] for _ in range(M)] for _ in range(N)]
queue = []

def init():
    rx,ry,bx,by = 0,0,0,0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 'R':
                rx, ry = i, j
            elif Map[i][j] == 'B':
                bx, by = i, j
    queue.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = True

def move(x,y,dx,dy):
    cnt = 0
    while Map[x+dx][y+dy] != '#' and Map[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def bfs_search():
    init()
    while queue:
        rx,ry,bx,by,depth = queue.pop(0)
        if depth>10:
            break
        for i in range(4):
            next_rx, next_ry, red_depth = move(rx,ry,dx[i],dy[i])
            next_bx, next_by, blue_depth = move(bx,by,dx[i],dy[i])
            if Map[next_bx][next_by] != 'O':
                if Map[next_rx][next_ry] == 'O':
                    print(depth)
                    return
                if next_rx == next_bx and next_ry == next_by:
                    if red_depth>blue_depth:
                        next_rx -= dx[i]
                        next_ry -= dy[i]
                    else:
                        next_bx -= dx[i]
                        next_by -= dy[i]
                if not visited[next_rx][next_ry][next_bx][next_by]:
                    visited[next_rx][next_ry][next_bx][next_by] = True
                    queue.append((next_rx,next_ry,next_bx,next_by,depth+1))
    print(-1)
bfs_search()