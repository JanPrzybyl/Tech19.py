# zad 4
ilosc = 0
for i in range(10,100):
  jed = int(i % 10)
  dz = int(i / 10)
  if dz > jed * 2:
    ilosc += 1
print(ilosc)

# zad 5
ilosc = 0
suma = 0
for i in range(100,1000):
  jed = i % 10
  dz = (i % 100)/10
  set = i / 100
  if set > dz + jed:
    suma += i
    ilosc += 1
print(f"suma wynosi: {suma}, a ilosc wynosi: {ilosc}")

# zad 6
n = int(input("ile liczb mamy znalezc:"))
ilosc = 0
suma = 0
for i in range(10,100):
  if i % 19 == 0:
    suma += i
    ilosc += 1
  if n == ilosc:
    print(f"suma to: {suma}")
    break
  if i == 99:
    print("Out of range")

# zad 7
n = int(input("ile liczb mamy znalezc"))
suma = 0
ilosc = 0
for i in range(999,100,-1):
  if i % 37 == 0:
    suma += i
    ilosc += 1
  if n == ilosc:
    print(f"suma to: {suma}")
    break
  if i == 101:
    print("Out of range")

# zad 8
from math import fabs
n = int(input("podaj ilosc powtorzen ciagu:"))
suma = 0
rytm = 2
for i in range(n):
  if i % 2 == 0:
    rytm *= -1
    suma *= rytm
    fabs(rytm)
  else:
    suma += rytm
    rytm += 3
print(f"suma n elemntow wynosi: {suma} ")

# zad 9
from math import fabs
n = int(input("podaj ile powtorzen ma miec ciag:"))
iloczyn = 1
rytm = 2
for i in range(2, n+2):
  rytm *= 2
  if i % 2 == 0:
    rytm *= -1
    iloczyn *= rytm
    fabs(rytm)
  else:
    iloczyn += rytm
print(f"iloczyn n elementow wynosi: {iloczyn} ")
