import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queue = [i for i in range(1, N + 1)]

num_list = list(map(int, input().split()))
cnt = 0
while num_list:
    find = queue.index(num_list[0])
    if num_list[0] == queue[0]:
        del queue[0]
        del num_list[0]

    elif find + 1 <= len(queue) // 2:
        while find + 1 != 1:
            queue.append(queue[0])
            del queue[0]
            find -= 1
            cnt += 1
        del queue[0]
        del num_list[0]

    elif find + 1 > len(queue) // 2:
        if len(queue[:find]) < len(queue[find:]):
            while find + 1 != 1:
                queue.append(queue[0])
                del queue[0]
                find -= 1
                cnt += 1
            del queue[0]
            del num_list[0]
        else:
            while find != len(queue):
                queue.insert(0, queue[-1])
                del queue[-1]
                find += 1
                cnt += 1
            del queue[0]
            del num_list[0]
print(cnt)