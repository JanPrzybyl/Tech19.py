# x = list(range(5))
# for item in x:
#   print(item)

# for item2 in range(4):
#   print(item2)

# print(len(x))

# for i in range(len(x)):
#   print(x[i])

# deklaracja listy  i literacja po liście

# L = [3, 5, 8, 13, 17, 27]

# for elem in L:
#   print(elem, end="")

# print("\n")

# for i in range(len(L)):
#   print(L[i], end="")

#funkcje w liscie

K = [4,7,5,7,3,3,2,8,7]
print(K)

# K.append(3)
# print(K)

# print(K.count(7))

# print(K.index(2))

# K.insert(2,4)
# print(K)

# jak wstawic 4 na koniec listy
# K.insert(len(K),4)
# print(K)

# K.pop()
# print(K)

# K.reverse()
# print(K)

# K.sort()
# print(K)

# usuwanie 7 z tablicy wercja 1
for i in range(K.count(7)):
  K.remove(7)
print(K)

# usuwanie 7 z tablicy wercja 2
for i in range(K.count(7)):
  K.pop(K.index(7))
print(K)

# poszukaj maksa w tablicy

print(max(K))

# maks w tabicy 2

maks = K[0]
for i in range(len(K)):
  if K[i] > i:
    maks = K[i]
print(maks)
  