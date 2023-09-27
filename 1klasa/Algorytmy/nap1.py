# s = input()
# for x in s:
#   print(x)

# for i in range(len(s)):
#   print(s[i])

# L = [7, 4, 5, 7]

# L.sort

# print(s, L)

# L = list(s)
# print(L)
# L.sort()
# print(L)
# w = "".join(L)
# print(w)

# sprawdź czy wpisane słowo jest palindromem
#s = input()
#L = list(s)
#R = L.copy()
#R.reverse()
#if L == R:
#  print("jest palindromem")
#else:
#  print("Nie jest palindromem")

#sprawdzanie palindroma za pomoca listy
# s = input()
# for i in range(len(s)//2):
#   if s[i] == s[len(s)-1-i]:
#     exit("NIE")
# exit("TAK")


L = [ i for i in range(1,10)]
print(L)
print(L[:4])
print(L[::2])
print(L[1::2])
print(L[::-1])
print(L[1:6:2])
print(L[1:6:-2]) #to jest zle
print(L[6:1:-2])
print(L[:1:-2])
