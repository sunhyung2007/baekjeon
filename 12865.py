import sys
input = sys.stdin.readline

N, K = map(int,input().split())
knap = [[0]*(K+1) for _ in range(N+1)]
weight = [0]
value = [0]
for i in range(N):
    W, V = map(int,input().split())
    weight.append(W)
    value.append(V)
for i in range(1,N+1):
    for j in range(1, K+1):
        if weight[i] > j:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(value[i] + knap[i-1][j-weight[i]], knap[i-1][j])
print(knap[-1][-1])
