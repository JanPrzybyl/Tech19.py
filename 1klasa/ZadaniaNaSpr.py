#zad 1 Oblicz wspólny mianownik trzech wpisanych przez użytkownika ułamków
def nww(a,b):
  iloczyn = a * b
  while b > 0:
    a, b = b, a % b
  return iloczyn // a

licznik = []
mianownik = []
for i in range(0,3):
  licznik.append(int(input()))
  print("-")
  mianownik.append(int(input()))
  print()

licz1 = mianownik[1] * licznik[0]
print(licz1)
mian = nww(mianownik[0],mianownik[1])
print(mian)
licz2 = mianownik[0] * licznik[1]
print(licz2)
print()
print(mian)
print()
mian = nww(mian,mianownik[2])
sumalicz = licz1 + licz2
licz3 = mianownik[2] * sumalicz
print(licz3)
print("-")
print(mian)

#zad 2 Jeżeli suma dzielników właściwych liczby naturalnej a wynosi b i analogicznie suma
#dzielników liczby naturalnej b wynosi a to te dwie liczby nazywamy zaprzyjaźnionymi
for a in range(1,5000):

  suma = 0
  for i in range(1, a//2 + 1):
    if a % i == 0:
        suma += i

  b = suma
  suma = 0
  for i in range(1, b//2 + 1):
    if b % i == 0:
        suma += i

  if a == suma:
    print(a)

# UŁAMKI Z CAŁOŚCIĄ
def nwd(a,b):
  while b > 0:
    a, b = b, a % b
  return a

a = int(input("LICZNIK:"))
b = int(input("MIANOWNIK:"))

calosci = a // b
reszta = a % b
dzielnik = nwd(reszta, b)
skroconaReszta = reszta/dzielnik
skroconyLicznik = b/dzielnik
print(f"calosc:{calosci} i {skroconaReszta}/{skroconyLicznik}")
    
# HUFMANN
W = "AABCCCDDDDDEFGGGHHIJJ"
H = ""
for i in range(len(W) - 1):
  if W[i] == W[i + 1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
  ilosc = 1
if ilosc > 1:
  H += str(ilosc)
H += W[len(W) - 1]
print(W)
print(H)

# CEZAR
napis = input()
szyfr = ""
for i in range(len(napis)):
  szyfr += chr(65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis,szyfr)

# LICZBY PIERWSZE
def czy_pierwsza(n):
  for i in range(2, n):
    if n % i == 0:
      return False
    else:
      return True

# NWD MODULO
def nwd_mod(a,b):
  while b > 0:
    a, b = b, a % b
  return a

# NWW MODULO
def nww_mod(a,b):
  iloczyn = a * b
  while b > 0:
    a, b = b, a % b
  return iloczyn // a

# NWD ODEJMOWANIE
def nwd_odej(a,b):
  while a != b:
    if  a > b : a -= b
    if  b > a : b -= a
  return a

# NWW ODEJMOWANIE
def nww_odej(a,b):
  iloczyn = a * b
  while a != b:
    if a > b : a -= b
    if b > a : b -= a
  return iloczyn // a

# WYTŁUMACZENIE RSA
1. Wybór 2 duzych liczb pierwszych
2. Stworzenie funkcji F = (p-1) * (q-1) i znalezienie n = p * q
3. Znalezienie klucza publicznego: e: NWD(F,e) = 1
4. Wygenerowanie klucza prywatnego: d * e % n = 1
5. Przykład działania kodowania znaku x:
c = x**e n (szyfrogrogram)
t = c**d % n (na tekst jawny)

# LICZBY PRAWIE PIERWSZE
for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:
            if czy_pierwsza(j) and czy_pierwsza(i // j):
                print(i)
                break
                
# Liczby BLIŹNIACZE
n = int(input())
ile1 = 0
ile2 = 0
for i in range(n - 2):
    if n % i == 0:
        ile1 += 1

for j in range(n + 2):
    if n % j == 0:
        ile2 += 1

if ile1 < 3 and ile2 < 3:
    print(f"Liczby blizniacze liczby {n} to {n - 2} i {n + 2}")
elif ile1 < 3 and ile2 > 2:
    print(f"Liczby blizniacze liczby {n} to tylko liczba {n - 2}")
elif ile1 > 2 and ile2 < 3:
    print(f"Liczby blizniacze liczby {n} to tylko liczba {n + 2}")
else:
    print("Liczba nie ma blizniakow")
