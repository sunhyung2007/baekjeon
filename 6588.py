import sys

input = sys.stdin.readline

number = [True for _ in range(1000001)]

number[0] = False
number[1] = False
number[2] = False
for i in range(2, 1000001):
    if number[i]:
        cnt = i*i
        while cnt < 1000001:
            number[cnt] = False
            cnt += i

while(True):
    a = int(input())
    if a == 0:
        break
    n = a // 2
    for i in range(3, n + 1, 2):
        check = False
        if (number[i]) and (number[a - i]):
            print("%d = %d + %d" % (a, i, a - i))
            check = True
            break
    if check == False:
        print("Goldbach's conjecture is wrong\n")