def numeroPrimo(numero):
    if numero == 1:
        print("não é primo")
    elif numero == 2:
        print("é primo")
    elif numero % 2 == 0:
        print("não é primo: ")

    elif numero % 1 ==0 and numero % numero == 0:
        print("é primo")