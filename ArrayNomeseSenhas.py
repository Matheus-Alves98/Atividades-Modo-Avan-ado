nomes = [0]*5
senhas = [0]*5
tam = len(nomes)
for x in range(tam):
    nomes[x] = input("Informe seu nome: ")
    senhas[x] = int(input("Informe sua senha: "))
for j in range (tam):
    print(nomes[j],senhas[j],j)