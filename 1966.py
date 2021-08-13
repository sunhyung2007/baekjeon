import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    point = list(map(int, input().split()))
    grade = [0 for _ in range(N)]
    grade[M] = 1
    cnt = 1
    print(point[0])
    while True:
        if point[0] == max(point):
            if grade[0] == 1:
                break
            else:
                del grade[0]
                del point[0]
            cnt += 1
        else:
            point.append(point[0])
            del point[0]
            grade.append(grade[0])
            del grade[0]
    print(cnt)