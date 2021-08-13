import sys
input = sys.stdin.readline

first = input().strip().upper()
second = input().strip().upper()

check_list = [[0]*(len(second)+1) for _ in range(len(first)+1)]
for i in range(1,len(first)+1):
    for j in range(1,len(second)+1):
        if first[i-1] == second[j-1]:
            check_list[i][j] = check_list[i-1][j-1] + 1
        else:
            check_list[i][j] = max(check_list[i][j-1], check_list[i-1][j])
print(check_list[-1][-1])