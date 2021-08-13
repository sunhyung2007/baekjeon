import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    cnt = 0
    a = input()
    T = list(a)
    for t in T:
        if t == '(':
            cnt += 1
        elif t == ')':
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")