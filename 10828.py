import sys

input = sys.stdin.readline

stack = [-1]
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
        print(stack)
    elif cmd[0] == "pop":
        print(stack[-1])
        if len(stack) != 1:
            del stack[-1]
    elif cmd[0] == "size":
        print(len(stack) - 1)
    elif cmd[0] == "empty":
        if len(stack) == 1:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        print(stack[-1])
    print("i = %d"%i)
