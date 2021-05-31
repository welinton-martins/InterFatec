bar = open("cod_de_barras.txt", "rt")
lines = bar.read().split("\n");
for i in range(2):
    [D,N] = (list(lines[i].split(" ")))
    D = str(D)
    N = str(N)
    if 1 <= int(D) <= 9 and 1 <= int(N) <= 9999999:
        for x in N:
            if x == D:
                N = N.replace(x,"")
        V = int(N)
        print(V)
