import sys
input = sys.stdin.readline

num = []
cnt = 9

for k in range(cnt):
    n = int(input())
    num.append(n)

for i in range(1, cnt):
    j = i - 1
    min = num[i]
    while j != -1:
        if min < num[j]:
            num[j+1] = num[j]
            num[j] = min
            j -= 1
        else:
            break
all = sum(num)
for a in range(8):
    for b in range(a+1, 9):
        if all - (num[a] + num[b]) == 100:
            liar1 = num[a]
            liar2 = num[b]

num.remove(liar1)
num.remove(liar2)
for x in num:
    print(x)
