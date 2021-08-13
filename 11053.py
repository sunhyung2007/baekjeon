import sys
input = sys.stdin.readline

count = 0
N = int(input())
num_list = list(map(int, input().split()))
check_list = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if check_list[j] < num_list[i]:
            check_list.append(num_list[i])
            count += 1
print(count)