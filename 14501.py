import sys

input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    tp = list(map(int, input().split()))
    graph.append(tp)

ti = graph[0][0]
pi = graph[0][1]


def dfs(n, p):
    global pi
    if pi < p:
        pi = p
        return

    for i in range(n, N):
        if n + graph[i][0] <= N:
            ta = i + graph[i][0]
            p += graph[i][1]
            print(ta, p)
            dfs(ta, p)
            p -= graph[i][1]


dfs(0, 0)
print(pi)