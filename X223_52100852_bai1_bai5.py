
import itertools,random
from re import I
import collections

# Permutation
E = {1,2,3,4,5}
k= 3
n = len(E)
permute_k = list(itertools.permutations(E,k))
print("%i-permutations of %s: " %(k,E))
for i in permute_k:
  print(i)
print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), len(permute_k))

# Combination
E = {'a','b','c','d'}
k= 3

choose_k = list(itertools.combinations(E,k))
print("%i-combinations of %s: " %(k,E))
for i in choose_k:
  print(i)
print("Number of combinations = %i!/(%i!(%i-%i)!) = %i" %(n,k,n,k,len(choose_k)))

# URN
def cross(A, B):
  return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
U6 = list(itertools.combinations(urn, 6))
print(U6)

# Excerse 1
print('Excerse 1')
E = {'1','2','3','4','5'}
k= 3
permute_k = list(itertools.permutations(E,k))
num_3_digit = []
for i in permute_k:
  temp =''
  for j in i:
    temp = temp+j
  num_3_digit.append(int(temp))
num_length = len(num_3_digit)
print(num_3_digit)
print("Number length: %i" %num_length)

# Excerse 2
print('Excerse 2')
def cross(A, B):
  return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
print("a)")
U3 = list(itertools.combinations(urn, 3))
len_U3 = len(U3)
u = list(itertools.combinations(urn, 6))
print("U3: ")
print(U3)
print('Length U3: ', len_U3)
print("b)")
for i in U3:
   if(i[0][0] == i[1][0] or i[1][0] == i[2][0] or i[0][0] == i[2][0]):
      continue
   print(i)
print('c)')
for i in U3:
   if(i[0][0] == 'W' and  i[1][0] == 'R'):
    print(i)

# Excerse 3
print('Excerse 3')
def cross(A, B):
  return {a + b for a in A for b in B}
  

urn_M = cross('M','4321')
urn_P = cross('P', '321')
urn_C =  cross('C', '21')
urn_E = cross('E','1')
all = []
# 6912
urn = (urn_M,urn_P,urn_C,urn_E)
for m in list(itertools.permutations(urn_M,len(urn_M))):
  for p in list(itertools.permutations(urn_P,len(urn_P))):
    for c in list(itertools.permutations(urn_C,len(urn_C))):
      for e in list(itertools.permutations(urn_E,len(urn_E))):
        urn = (m,p,c,e)
        a = list(itertools.permutations(urn,len(urn)))
        for i in a:
          print(i)
          all. append(i)

print("Total: %i" %len(all))

# Excerse 4
print('Excerse 4')
Males = cross('M','987654321')
Females = cross('F', '654321')
for male in itertools.combinations(Males,3):
   for female in itertools.combinations(Females,2):
      print(male + female )

# Excerse 5
print('Excerse 5')
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(itertools.product(Ranks , Suits))
poker_5 = list(itertools.combinations(Cards,5))
len_poker_5 = len(poker_5)
three_of_a_kind = []
print("Poker_5: ")
for i in poker_5:
  print(i)
print("len_poker_5: %i" %len_poker_5)

for i in poker_5:
  arr = []
  flag = False
  for j in range(0,5):
    arr.append(i[j][0])
    if arr.count(i[j][0]) ==3 :
      flag = True
    if arr.count(i[j][0]) == 4:
      flag = False
  if len(collections.Counter(arr))!=3:
    flag = False 
  if flag:
    three_of_a_kind.append(i)
len_three_of_a_kind = len(three_of_a_kind)  

print('three_of_a_kind: ')
for i in three_of_a_kind:
  print(i)
print('len_three_of_a_kind: %i' %len_three_of_a_kind)