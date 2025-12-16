liczba = int(input('Wpisz liczbę: '))


def l_parzysta(x):
    if x % 2 == 0:
        parzysta = True
        return parzysta
    else:
        parzysta = False
        return parzysta


l_parzysta(liczba)

if l_parzysta(liczba):
    print('Liczba parzysta')
else:
    print('Licza nieparzysta')
