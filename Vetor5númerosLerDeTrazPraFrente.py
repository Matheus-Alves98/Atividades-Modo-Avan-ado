num =[0]*5
tam = len(num)
for x in range (tam):
    num[x] = int(input("Digite um número:"))

for i in range (tam-1,-1,-1):
    print(num[i], end=" ")
