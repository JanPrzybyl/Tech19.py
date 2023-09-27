# Zad 1
# n = int(input())
# suma = 0
# while n > 0:
#   suma = suma + n % 10
#   n = n // 10
# print(suma)

# Zad 2
# a = int(input())
# for i in range(2, a):
#     if a % i == 0:
#         print("Tak, liczba nie jest pierwsza")
#         exit(0)
# print("Nie,liczba jest pierwsza")

# Zad 3
# n = int(input())
# suma = 0
# for i in range(1,n):
#   if n % i ==0:
#     suma = suma + i
# if suma ==n:
#     print("liczba jest doskonala")
# else:
#     print("liczba ne jest doskonala")

# Zad 4
# x = int(input())
# y = int(input())
# while y > 0:
#   x, y = y, x % y
# nwd = 0
# if nwd ==1:
#   print("Liczby są względem siebie pierwsze")
# else:
#   print("Liczby nie są względem siebie pierwze")

# Zad 5
# n = int(input())

# for i in range(10,20):
#   x = n
#   y = i
#   while y > 0:
#     x , y = y, x % y
#   nwd = x
#   if x == 1:
#     print(f"Mamy parkę: {n}, {i}")

# Zad 6
# a = int(input())
# b = int(input())
# a = x
# b = y
# while y > 0:
#   x, y = y, x % y
# c = a//x
# d = a//x
#   print(f"{a}/{b} = {c}/{d}")

# Zad 7

# Zad 8
# T = []
# for i in range(2,10000):
#   suma1 = 0
#   for j in range(1, i):
#     if i % j ==0:
#       suma1 += j
#   T.append(suma1)
#   suma2 = 0
#   for k in range(1,suma1):
#     if suma1 % k ==0:
#       suma2 += k
#   if i == suma2 and suma1 != suma2 and suma2 not in T:
#     print(f"({suma1},{suma2})")

#zad 9
def czy_pierwsza(n):
  for i in range(2, n):
    if n % i ==0:
        return False
    return True

for i in range(10,100):
  for j in range(2,i):
    if i % j == 0:
      if czy_pierwsza(j) and czy_pierwsza(i // j):
        print(i, end=" ")
        break