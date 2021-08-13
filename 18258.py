import sys

input = sys.stdin.readline


class queue:
    def __init__(self):
        self.queue = list()

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]


N = int(input())
arr = queue()

for _ in range(N):
    command = input().split()
    if command[0] == "push":
        arr.push(int(command[1]))
    elif command[0] == "pop":
        print(arr.pop())
    elif command[0] == "size":
        print(arr.size())
    elif command[0] == "empty":
        print(arr.empty())
    elif command[0] == "front":
        print(arr.front())
    elif command[0] == "back":
        print(arr.back())