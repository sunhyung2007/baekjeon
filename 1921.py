import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
len1 = len(num_list)
dp = [num_list[0]]
for i in range(len1-1):
    sum = max(dp[i]+num_list[i+1], num_list[i+1])
    dp.append(sum)
print(max(dp))