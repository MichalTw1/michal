dane = input('Wpisz kilka liczb (oddzielonych spacją): ')
lista = dane.split(' ')
liczba = int(input('Wpisz liczbe: '))

def szukam(x: list, y: int):
    if str(y) in x:
        return True
    else:
        return False

print(szukam(lista, liczba))