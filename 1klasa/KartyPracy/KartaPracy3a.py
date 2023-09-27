#zad 1
# n = int(input())
# for i in range(n):
#   print("*-|", end=" ")

#zad 2
# n = int(input())
# for i  in range(1, n+1):
#   print("*"*i, end=" ")
#   if i%2:
#     print("||", end=" ")
#   else:
#     print("--", end=" ")

#zad 3
# n = int(input())
# for i in range(1, n+1):
#   print("*", end="")
#   if i%2 ==1:
#     print("|"*i, end="")
#   else:
#     print("-"*i, end="")

#PRE-Tabliczka Mnożenia
# for i in range(1,11):
#   for j in range(1,11):
#    print(i*j, end="\t")
#   print()

# *
# **
# ***
# ****
# *****

# *****
# ****
# ***
# **
# *

#     *
#    **
#   ***
#  ****
# *****

# *****
#  ****
#   ***
#    **
#     *
#PRE NA 2 PETLE
# n = int(input())

# for i in range(n):
#   for j in range(i+1):
#     print("*", end="")
#   print()

# print()
# print()

# for i in range(n):
#     for j in range(n - i):
#       print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for k in range(n - i - 1,n):
#         print("*", end="")
#     print()

# print()
# print()

# for i in range(n):
#   for j in range(i):
#       print(" ", end="")
#   for k in range(i, n):
#       print("*", end="")
#   print()

n = int(input())

for i in range(n):
  for j in range(n):
    if i + j <= n - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()

for i in range(n):
  for j in range(n):
    if i >= n - j - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()

