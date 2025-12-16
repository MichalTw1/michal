num1 = int(input('Podaj liczbę: '))
num2 = int(input('Podaj liczbę: '))
num3 = int(input('Podaj liczbę: '))


def czy_wieksza(x, y, z):
    if x + y >= z:
        return True
    else:
        return False


print(czy_wieksza(num1, num2, num3))
