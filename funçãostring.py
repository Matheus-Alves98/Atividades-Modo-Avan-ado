def tratartexto (texto):
    cont = 0
    for x in texto:
        if x not in " !@#$%":
            cont+=1
    print(f"o texto tem {cont} letras")
    tam= len(texto)
    for z in range(tam-1,-1,-1):
        print(texto[z], end="")