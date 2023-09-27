# p, q = int(input()), int(input())
# if (1.3 p > q):
#   print("TAK")
# else:
#   print("NIE")

# print(list(range(10)))
# print(list(range(5)))
# print(list(range(2,10)))
# print(list(range(12,10)))
# print(list(range(12,10,-1)))

# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22): print(i, end=" ")
# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# for i in range(15,32,2): print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1): print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,99,1): print(109-i, end=" ")
# pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100,999,20): print(i, end=" ")

#zad 1
# n = int(input())
# for i in range(n):
#   print(i**3 + 3, end=" ")

# for i in range(10,22): print(i, end=" ")

# for i in range(15,32,2): print(i, end=" ")

#zad 2
# for i in range(105,1000,15): print(i, end=" ")

#zad 3

# n = int(input())
# for i in range(i,n+1):
#   if n % i ==0:
#     print(i, end=" ")

#zad 4
# suma= 0
# for i in range(10,100):
#   suma = suma + i
#   print(suma)

#zad 5
# n = int(input())
# suma = n*(n+1)//2

# for i in range(n-1):
#   x = int(input())
#   suma = suma - x
# print("NIE PODAŁEŚ:",suma)

#zad 6
n = int(input())
a = 0
b = 1 
print(a, end=" ")
print(b, end=" ")
for i in range(n-2):
  a,b = b, a+b
  print(b, end=" ")

