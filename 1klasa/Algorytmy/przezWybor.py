#Sortowanie przez wybór
from random import randint
n = 17
T = [randint(1,100) for i in range(n)]
print(T)

for i in range(n):
  mi = i
  for j in range(i,n):
      if T[j] > T[mi]:
        mi = j
  T[i], T[mi] = T[mi], T[i]
print(T)
