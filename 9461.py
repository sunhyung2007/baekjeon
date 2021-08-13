import sys
input = sys.stdin.readline

side_list = [0 for _ in range(101)]
side_list[1] = 1
side_list[2] = 1
side_list[3] = 1
for j in range(0,98):
    side_list[j + 3] = side_list[j] + side_list[j + 1]
N = int(input())

for i in range(0,N):
    T = int(input())
    print(side_list[T])