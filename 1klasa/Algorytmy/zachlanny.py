x = int(input())
nominaly = [50,20,10,5,2,1]
W = []
for i in nominaly:
  ilosc = x // i
  if ilosc > 0:
    x = x - ilosc * i
    for j in range(ilosc):
      W.append(i)
print(W)
  # print(f"nominal:{i} ilosc:{ilosc}")