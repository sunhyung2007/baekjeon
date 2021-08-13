import sys
input = sys.stdin.readline

stack1 = []
stack2 = []
cnt = 0
while True:
    text = input()
    if text == '.':
        break
    for i in text:
        if i == '(':
            stack1.append(i)
        elif i == '[':
            stack2.append(i)
        if i == ')' and len(stack1) == 0:
            if len(stack1) > 0:
                del stack1[-1]
            break
        elif i == ']' and len(stack2) == 0:
            if len(stack2) > 0:
                del stack2[-1]
            break
        if i == ')':
            del stack1[-1]
        elif i == ']':
            del stack2[-1]
    if len(stack1) == 0 and len(stack2) == 0:
        print("yes")
    else:
        print("다 돌고 no")
    cnt += 1
    stack1.clear()
    stack2.clear()