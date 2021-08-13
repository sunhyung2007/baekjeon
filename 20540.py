import sys

input = sys.stdin.readline

user = input()
mbti = list(user)
my_type = []

if mbti[0] == 'E':
    my_type.append('I')
else:
    my_type.append('E')
if mbti[1] == 'S':
    my_type.append('N')
else:
    my_type.append('S')
if mbti[2] == 'T':
    my_type.append('F')
else:
    my_type.append('T')
if mbti[3] == 'J':
    my_type.append('P')
else:
    my_type.append('J')

print(''.join(my_type))