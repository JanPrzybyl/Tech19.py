#Anagram przez sortowanie
# a,b = input(), input()
# x, y = list(a), list(b)

# x.sort()
# y.sort()
# a, b = "".join(x), "".join(y)
# print(a,b)
# if a == b:
#   print("TAK")
# else:
#   print("NIE")
#Anagram prze tablice

a,b = input(), input()

X, Y = [0] * 150, [0] * 150
for i in range(len(a)):
  X[ord(a[i])] += 1
print(X)
if X==Y:  print("TAK")
else:     print("NIE")
