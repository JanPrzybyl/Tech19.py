# funkcja ord() - zwraca kod ascii dla danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# # Funkcja chr() - zwraca znak dla danego kodu ascii

# print(chr(65))
# print(chr(75))
# print(chr(89))

#mozna laczyc
# print(chr(ord("C")))
# print(chr(ord("C")+1))

#napisz alfabet za pomocą petli for
#liter od 65 do 91 jest 26
# for i in range(65,91):
#   print(chr(i), end="")

#jak wydobyc literki z napisow
# napis = "POLSKA"
# print(len(napis))
# print(napis[0])
# print(napis[1])

#napisz petle wyciągająco z napisu literki 
# napis = input()
# napis = napis.replace(" ","") # zamienia spacje na pustaki
# for i in range(len(napis)):
#     print(napis[i])

#napisz petle wyciagająco kody ascii z napisow
# napis = input()
# for i in range(len(napis)):
#   print(ord(napis[i]))

# zaszyfruj nais cezarem w kluczu 3
napis = input()
szyfr = ""
for i in range(len(napis)):
  szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)