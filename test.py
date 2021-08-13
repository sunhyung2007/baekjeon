import sys

input = sys.stdin.readline

array_n = [1,2,1,2]
for i in range(1, len(array_n)):
    j = i
    key = array_n[i]
    while j > 0 and array_n[j - 1] > array_n[i]:
        array_n[j] = array_n[j - 1]
        j -= 1
    array_n[j] = key

print(array_n)