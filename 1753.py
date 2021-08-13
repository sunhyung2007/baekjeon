import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

