lista1 = input('Wpisz liczby oddzielone spacją: ')
lista1 = lista1.split(' ')
lista2 = input('Wpisz liczby oddzielone spacją: ')
lista2 = lista2.split(' ')
nowa_lista = []
potega_trzecia = []

def listy(x: list, y: list):
    for i in x:
        nowa_lista.append(i)

    for j in y:
        if not j in nowa_lista:
            nowa_lista.append(j)
        else:
            continue

    for k in nowa_lista:
        k = int(k)
        k = pow(k, 3)
        potega_trzecia.append(k)
    else:
        return potega_trzecia

print(listy(lista1, lista2))