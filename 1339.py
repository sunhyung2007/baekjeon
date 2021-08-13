N = int(input())
al_list = [0 for _ in range(26)]
seq = []

for _ in range(N):
    al = input()
    seq.append(al)

for s in seq:
    for i in range(len(s)):
        al_list[ord(s[i]) - 65] += 10 ** (len(s) - 1 - i)

"""
def find_location(seq):
    for i in range(len(seq)):
        al_list[ord(seq[i]) - 65] += (10 ** (len(seq)-1-i))
"""

al_list.sort(reverse=True)
al_list[0:10]
all = 0

for j in range(10):
    all += (9 - j) * al_list[j]

print(all)
