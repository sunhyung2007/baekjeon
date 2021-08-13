import sys

input = sys.stdin.readline

k = int(input())
op = input().split()
num_list = []
check = [False for _ in range(10)]
mi = 0
ma = 9
cnt = 0


def check_ud(i, j, sign):
    if sign == '<':
        return i < j
    elif sign == '>':
        return i > j


def max(ch):
    global mi, ma, cnt
    if ch == k + 1:
        cnt += 1
        if cnt == 1:
            mi = list(map(str, num_list))
        ma = list(map(str, num_list))

        return
    for i in range(10):
        if not check[i]:
            if ch == 0 or check_ud(num_list[-1], i, op[ch - 1]):
                num_list.append(i)
                check[i] = True
                max(ch + 1)
                check[i] = False
                num_list.pop()


max(0)
mi = "".join(mi)
ma = "".join(ma)
print(ma)
print(mi)
