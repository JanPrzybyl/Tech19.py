#zad1
# a = int(input())
# b = int(input())
# if (a + b) % 2 == 0: print("TAK, parzysta")
# else: print("NIE, nieparzysta")

#zad2
# from math import sqrt
# a = float(input())
# g = float(input())
# if (a + g) / 2 > sqrt(a * g) : print("TAK srednia arytmetyczna jest wieksza od srednie geometrycznej")
# else : print("NIE, srednia arytmetyczna nie jest wieksza od sredniej geometrycznej")

#zad3
# k = int(input())
# l = int(input())
# m = int(input())
# if k == l or k == m or l == m : 
#     print("TAK, przynajmniej dwie liczby sa rowne")
#     if k == l and k == m and l == m : print("Wszystkie liczby sa rowne")
#     elif k == l : print("jest to: Liczba1 i Liczba2")
#     elif k == m : print("jest to: Liczba1 i Liczba3")
#     elif l == m : print("jest to: Liczba2 i Liczba3")
# else : print("NIE, nie ma rownych")

#zad4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a < b and a < c and a < d: print("Najmniejsza liczba to a")
# elif b < a and b < c and b < d : print("Najmniejsza liczba to b")
# elif c < a and c < b and c < d : print("Najmniejsza liczba to c")
# elif d < a and d < b and d < c : print("Najmniejsza liczba to d")
# else : print("Sa dwie najmniejsze liczby rowne sobie")

#zad5
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b>c and b+c>a and a+c>b:
#   print("TAK, liczby spelniaja nierownosc trojkata")
# else : print("NIE, liczby nie spelnia nierownosci trojkata")

#zad6
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b>c and b+c>a and a+c>b:
#     print("TAK, trojkat powstanie")
# if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2: print("prostokatny")
#     elif a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or c**2 + a**2 > b**2: print("ostrokatny")
#     elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2: print("rozwartokatny")
# else:
#     print("NIE, trojkat nie powstanie")