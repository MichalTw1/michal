name = input('Enter your name: ')
surname = input('Enter your surname: ')

def hello(x, y):
    hello = f'Cześć {name} {surname}!'
    return hello

print(hello(name, surname))