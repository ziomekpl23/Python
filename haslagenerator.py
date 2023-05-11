import random
print("Siema uczniu/nauczycielu nie umiesz hasla ulozyc wiec ci pomoge")
znaki = 'abcdefghijklmnopqrstuvwxyzABCDEFGH'

dlugosc = input('Podaj dlugosc hasla:')
dlugosc = int(dlugosc)
haslo = ''
for z in range (dlugosc):
    haslo+= random.choice(znaki)

print(haslo)