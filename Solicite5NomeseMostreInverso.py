nomes = [0]*5
tam = len(nomes)
for x in range (tam):
    nomes[x] = input("Digite seu nome:")
for i in range (tam-1,-1,-1):
    print(nomes[i],end=" ")