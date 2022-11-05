from collections import Counter
from hashlib import new
from operator import le
import random
import fractions
import itertools as tool
from itertools import count, product
from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


# problem 1
print("Problem 1")
s = {'BB', 'BG', 'GB', 'GG'}

B = {i for i in s if 'B' in i}
A_B = {i for i in B if i.count('B') == 2}
P_A_with_B = P(A_B, s)/P(B, s)
print(P_A_with_B)

# problem 2


# ex1
# a


def Cats():
    Gen = {'M', 'F'}
    S = []
    Cat = [p for p in tool.product(Gen, repeat=3)]
    for i in Cat:
        S.append('{}{}{}'.format(i[0], i[1], i[2]))
    return S

# b


def Cat_Female(S):
    cat_M = []
    for cat in S:
        if 'F' in cat:
            cat_M.append(cat)
    return cat_M
# d


def Cat_AllFemale(S):
    cat_M = []
    for cat in S:
        if 'FFF' in cat:
            cat_M.append(cat)
    return cat_M


# e
def Cat_ThreeF(S):
    return P(set(Cat_AllFemale(s)), set(Cat_Female(s)))


print("--------")
print("Bai 1:")
print("a)")
s = Cats()
print('Space = {}'.format(s))
print('b)')
print('|Space| = {}'.format(len(s)))
print('c)')
print('B = {}'.format(Cat_Female(s)))
print('d)')
print('A = {}'.format(Cat_AllFemale(s)))
print('e)')
print('P(A|B) = {}'.format(Cat_ThreeF(s)))
# Bai 2
print("--------")
print("Bai 2:")
print("a)")
S = {('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
     ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')}


A = {student for student in S if 'Thanh' in student[0]}
B = {student for student in S if 'Nữ' == student[1]}
A_B = {student for student in S if 'Nữ' ==
       student[1] and 'Thanh' == student[0]}

P_A = P(A, S)
P_B = P(B, S)
P_A_B = P(A_B, S)
print('A = {}'.format(A))
print('B = {}'.format(B))
print('A_B = {}'.format(A_B))
print('P(A) = {}'.format(P_A))
print('P(B) = {}'.format(P_B))
print('P(A_B) = {}'.format(P_A_B))
print('P(A|B) = {}'.format(P_A_B/P_B))

# Bai 3

# a


def Cards():
    Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    Suits = {'♡', '♢', '♣', '♠'}
    Cards = list(tool.product(Ranks, Suits))
    S = []
    for i in Cards:
        S.append('{}{}'.format(i[0], i[1]))
    return set(S)


print("--------")
print("Bai 3:")
print("a)")
S = Cards()
print("Cards = {}".format(S))
print('b)')
B = set(tool.combinations(S, 3))
print('B = {}'.format(len(B)))
tmp = {a for a in B}
A1 = set({})
for i in tmp:
    if [i[0][0], i[1][0], i[2][0]].count('K') == 1 or [i[0][0], i[1][0], i[2][0]].count('K') == 2:
        A1.add(i)
print('A1 = {}'.format(len(A1)))

print('c)')
A2 = set({})
for i in tmp:
    if [i[0][0], i[1][0], i[2][0]].count('K') >= 1:
        A2.add(i)
print('A2 = {}'.format(len(A2)))

print('P(A1) = {}'.format(len(A1)/len(B)))
print('P(A2) = {}'.format(len(A2)/len(B)))
