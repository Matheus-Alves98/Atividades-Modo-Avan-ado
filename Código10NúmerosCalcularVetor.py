num = [0]*10
tam = len(num)
cont = 0
for x in range (tam):
    num[x] = int(input("Digite um número: "))
print("------")
numeros = int(input("Digite um número qualquer:"))
for i in range (tam):
    if numeros == num[i]:
        cont = cont+1
print(cont)