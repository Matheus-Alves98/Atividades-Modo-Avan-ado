def listaunica(a):
    nova_lista=[]
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)
