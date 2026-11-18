def segundo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    for i in lista:
        if maior in lista:
            lista.remove(maior)
    maior = lista[0]
    print(lista)
    for i in lista:
        if i > maior:
            maior = i
    return maior
print(segundo([1,4,2,6,7,8,8,7]))