import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
result = [-1 for _ in range(N)]
stack = [0]

i = 1
while i<N and stack:
    while stack and num_list[stack[-1]] < num_list[i]:
        result[stack[-1]] = num_list[i]
        stack.pop()
    stack.append(i)
    i += 1
for j in result:
    print(j)
