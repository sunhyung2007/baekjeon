import sys

input = sys.stdin.readline

S = []
num_list = []
check = []
k = 0


def dfs(ch, n):
    if ch == 6:
        for i in range(6):
            print(num_list[i], end=' ')
        print()
        return
    for j in range(n, k):
        if not check[j]:
            check[j] = True
            num_list.append(S[j])
            dfs(ch + 1, j + 1)
            check[j] = False
            num_list.pop()


while True:
    S = []
    num_list = []
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    k = S[0]
    S = S[1:]
    check = [False for _ in range(k)]
    dfs(0, 0)
    print()