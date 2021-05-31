# "Welinton"
x1 = 0
x2 = []
verif = 0

while True:
  x1 = int(input())
  if (2 <= x1 <= 100):
    break

while True:
  dados = input()
  lines = dados.split(" ")
  
  for j in range(x1):
    if(1 <= int(lines[j]) <= 6):
      verif += 1
    if(verif == x1):
        break

for k in range(2):
  if (k == 0):
    x1 = int(lines[k])
  else:
    for l in range(x1):
      x2 = str(lines[l])
      print(x2)
    i
