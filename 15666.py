import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sequence = []
check = [False] * n
num_list = []

for i in range(1, n):
    key = num[i]
    j = i
    while j > 0 and num[j - 1] > key:
        num[j] = num[j - 1]
        j -= 1
    num[j] = key

make = []
def seq(ch):
    if ch == m:
        print(sequence)

        "m개의 리스트가 만들어지면 이를 카피하여 정렬한 후 중복 제거"
        make.append(sequence.copy())

        for i in range(1, m):
            "여기서 list out of range 오류 발생"
            temp = make[i]
            j = i
            while j > 0 and make[j - 1] > temp:
                make[j] = make[j - 1]
                j -= 1
            make[j] = temp

        print(make)
        make.clear()
        num_list.append(sequence.copy())
        return
    for i in range(n):
        if not check[i]:
            sequence.append(num[i])
            seq(ch + 1)
            sequence.pop()


seq(0)
re_list = list(set(map(tuple, num_list)))
re_list.sort()
"""
for a in range(len(re_list)):
    print(' '.join(map(str, re_list[a])))
"""