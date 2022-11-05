from collections import Counter
import random
import fractions
import itertools
from itertools import count, product
from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


def cross(A, B):
    return {a + b for a in A for b in B}


def combos(items, n):
    return {' ' .join(combo) for combo in itertools. combinations(items, n)}


# EXCERSE
print("Tung 2 con xuc sac n lan.")


def simualtor_dice1(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 % 2 == 0 and die2 % 2 == 0:
            count += 1
    return count/n


def simualtor_dice2(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if (die1 % 2 != 0 and die2 % 2 == 0) or (die1 % 2 == 0 and die2 % 2 != 0):
            count += 1
    return count/n


def simualtor_dice3(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == die2:
            count += 1
    return count/n


def simualtor_dice4(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if (die1 == 1 and die2 == 6) or (die1 == 6 and die2 == 1):
            count += 1
    return count/n


def simualtor_dice5(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if (die1 + die2 > 6):
            count += 1
    return count/n


def simualtor_poker1(n):
    count = 0
    for i in range(n):
        indexs = random.sample(range(52), 5)
        flag = True
        for index in indexs:
            if Cards[index][1] != '♡':
                flag = False
                break
        if flag:
            count += 1
    return count/n


def simualtor_poker2(n):
    count = 0
    for i in range(n):
        indexs = random.sample(range(52), 4)
        type = [Cards[index][1] for index in indexs]
        if len(Counter(type)) == 4:
            count += 1
    return count/n


def probability():
    urn = cross('W', '12345678') | cross(
        'B', '123456') | cross('R', '123456789')

    U6 = combos(urn, 6)
    # print(random.sample(U6, 6))
    w2b2r2 = {s for s in U6 if s.count('B') == 2 and s.count(
        'W') == 2 and s.count('R') == 2}

    return P(w2b2r2, U6)


print('Bai 1: Xac suat de 2 con xuc sac deu chan: ', simualtor_dice1(1000000))
print('Bai 2: Xac suat de 1 con chan 1 con le: ', simualtor_dice2(1000000))
print('Bai 3: Xac suat de 2 con bang nhau: ', simualtor_dice3(1000000))
print('Bai 4: Xac suat de co 1 con 1 va 6: ', simualtor_dice4(1000000))
print('Bai 5: Xac suat de 2 con xuc sac co tong lon hon 6: ',
      simualtor_dice5(1000000))


print("Bai 6: Chon 5 la trong 52 la bai")
Ranks = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks, Suits))
print('Xac suat de chon duoc 5 la ♡:', simualtor_poker1(1000000))

print("Bai 7: Chon 4 la trong 52 la bai")
print('Xac suat de chon duoc 4 la khac loai:', simualtor_poker2(1000000))

print("Bai 8: Xac xuat de chon duoc 2 trang, 2 xanh va 2 do: ", probability())
