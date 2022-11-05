# %%
import numpy as np
import math
import random

print("----Example----")
x = [random.randint(1, 6) for i in range(8000)]
X = set(x)
# print(x)
# print(X)


# %%
# Phân phối xác suất
P = [x.count(i)/len(x) for i in X]
print(P)


# %%
# phân phối tích lũy
FX = sum(P[:3])
print(FX)

# %%
# Ky vong
EX = 0
for x in X:
    EX = EX + (x*P[x-1])
print(EX)


# %%
# Phuong sai

VarX = 0
for x in X:
    VarX = VarX+(x-EX)*(x-EX)*P[x-1]
print(VarX)

# %%
# Do lech chuan
SD = math.sqrt(VarX)
print(SD)

# %%
# Exercise 6.1
print("----Exercise 6.1----")
x = np.random.choice([0, 1, 2, 3, 4, 5], 360, p=[
                     0.1, 0.2, 0.3, 0.2, 0.15, 0.05])
X = set(x)
print("X = {}".format(X))

P = [list(x).count(i)/len(x) for i in X]
print("P = {}".format(P))


EX = 0
for x in X:
    EX = EX + (x*P[x-1])
print("Expectation: {}".format(EX))

VarX = 0
for x in X:
    VarX = VarX+(x-EX)*(x-EX)*P[x-1]
print("Variance: {}".format(VarX))

SD = math.sqrt(VarX)
print("Standard deviation: {}".format(SD))

print("Probability of having 3 or more emergency: {}".format(sum(P[3:])))


# %%
# Exercise 6.2
print("----Exercise 6.2----")
x = np.random.choice([0, 1, 2], 10000)
X = set(x)
print("X = {}".format(X))

P = [list(x).count(i)/len(x) for i in X]
print("P = {}".format(P))

EX = 0
for x in X:
    EX = EX + (x*P[x-1])
print("Expectation: {}".format(EX))

VarX = 0
for x in X:
    VarX = VarX+(x-EX)*(x-EX)*P[x-1]
print("Variance: {}".format(VarX))

SD = math.sqrt(VarX)
print("Standard deviation: {}".format(SD))

print("Probability of having 3 or more emergency: {}".format(sum(P[1:])))
