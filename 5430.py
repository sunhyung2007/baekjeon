import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command = input()
    n = int(input())
    command = command.replace("RR", "")
    num = input().rstrip()[1:-1].split(',')
    front = 0
    rear = 0
    R = 0

    for c in command:
        if c == 'R':
            R += 1
        elif c == 'D':
            if R % 2 == 0:
                front += 1
            else:
                rear += 1
    if front + rear <= n:
        num = num[front: n-rear]
        if R % 2 != 0:
            print('[' + ','.join(num[::-1]) + ']')
        else:
            print('[' + ','.join(num) + ']')
    else:
        print('error')
