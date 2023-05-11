def kwa():
    a = int(input('Dlugosc boku kwadratu: '))
    if a <=0 :
        print("podaj liczbe wieksza od zera")
    else:
        return a*a


def pro():
    a = int(input('Dlugosc pierwszego boku prostokata: '))
    b = int(input('Dlugosc drugiego boku prostokata: '))
    if a<=0:
        print("Podaj liczbe wieksza od zera ziomek")
    else:
        return a*b
    if b<=0:
        print("podaj liczbe wieksza od zera")
    else:
        return a*b

def tra():
    a = int(input('Dlugosc pierwszej podstawy trapezu: '))
    b = int(input('Dlugosc drugiej podstawy trapezu: '))
    h = int(input('Wysokosc trapezu: '))
    if a<=0:
        print("Podaj liczbe wieksza od zera ziomek")
    else:
        return (a+b)*h/2

    if b<=0:
        print("podaj liczbe wieksza od zera")
    else:
        return (a+b)*h/2
    if h<=0:
        print("podaj liczbe wieksza od zera")
    else:
        return (a+b)*h/2

def rom():
    a = int(input('Dlugosc podstawy rombu: '))
    h = int(input('Wysokosc rombu: '))
    return a*h

while True:
    print('Program do liczenia powierzchni figur plaskich')
    print('\n')
    print('Wybierz figure:')
    print('[1] kwadrat')
    print('[2] prostokat')
    print('[3] trapez')
    print('[4] romb')
    print('[0] koniec')
    odp = int(input('Wybor: '))
    if(odp == 1):
        print('Pole:', kwa())
    elif(odp == 2):
        print('Pole:', pro())
    elif(odp == 3):
        print('Pole:', tra())
    elif(odp == 4):
        print('Pole:', rom())
    else:
        break
    print('---')
