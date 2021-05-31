



le True:
  x1 = int(input("Digite a quantidade de lançamentos:"))
  if (2 <= x1 <= 100):
    break

dados = input("Digite a sequencia de valores obtidos:")
lines = dados.split(" ")
  
while (verif != x1):
    if(1 <= int(lines[j]) <= 6):
      verif += 1
    j += 1

for l in range(x1):
  x2 = str(lines[l])
  x2 = int(x2) 

  if ((l+1) % 2 != 0):
    p1 += x2
  else:
    if (x2 == 6):
      p1 += x2
    else:
      p2 += x2
  
if (p1 > p2):
  print(f"LUIZA {p1}")
  print(f"ANTONIO {p2}")
elif (p2 > p1):
  print(f"ANTONIO {p2}")
  print(f"LUIZA {p1}")
else:
  print(f"EMPATE {p1, p2}")
