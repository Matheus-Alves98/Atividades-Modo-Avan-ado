arrayNotas = [0,0,0,0,0]
soma = 0
cont = 0
tam = len(arrayNotas)
for x in range (tam):
    arrayNotas[x] = float(input("Digite uma nota:"))
for i in range(tam):
    soma = soma + arrayNotas[i]
media = soma/tam
for c in range(tam):
    if arrayNotas[c] > media:
        cont = cont + 1
print(f"A média da turma é {media} e {cont} alunos ficaram com nota acima da média")