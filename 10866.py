import sys

input = sys.stdin.readline


class deque:

    def __init__(self):
        self.queue = list()

    def push_front(self, x):
        self.queue.insert(0, x)

    def push_back(self, x):
        self.queue.append(x)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop(0)

    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.queue.pop()

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


arr = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'push_front':
        arr.push_front(int(command[1]))
    elif command[0] == 'push_back':
        arr.push_back(int(command[1]))
    elif command[0] == 'pop_front':
        print(arr.pop_front())
    elif command[0] == 'pop_back':
        print(arr.pop_back())
    elif command[0] == 'size':
        print(arr.size())
    elif command[0] == 'empty':
        print(arr.empty())
    elif command[0] == 'front':
        print(arr.front())
    elif command[0] == 'back':
        print(arr.back())