print("Hello world")#to jest komentarz
'''
a
b
c
'''

zmienna=10
rzeczywista=10.4
tekst="hello world"
tekst2='Hello world'

print(zmienna,rzeczywista,tekst,tekst2)

print('wartosc zmiennej zmienna to:',zmienna)
print(f'wartosc zmiennej t {zmienna}')
print('wartosc zmiennej zmienna to'+ str(zmienna))

#liczba= 10.5
print('%.20f'% zmienna) #20 miejsc po przecinku

#imie=input('jak masz na imie?')
#print('czesc, ',imie)
#liczba2=int(input('ile masz lat?'))

suma=2+2
roznica=3-2
iloczyn=3*2
iloraz=4/2
reszta=5%2
potega=2**5

#print(random.randint(1,10))

'''
liczba=int(input('Podaj liczbe:'))

if liczba >0
print('liczba jest wieksza od 0)
elif liczba ==0
print('liczba jest rowna 0')
else:
print('liczba jest mniejsza od 0')

liczba2=int(input('podaj liczbe:'))
if liczba2%2==0:
print('liczba jest podzielna przez 2')
else:
print('liczba nie jest podzielna przez 2')

liczba3=int int(input('podaj liczbe:'))
if liczba3 <0
print(liczba3*-1)
else:
print(liczba3)
'''
#for i in range(5):
#print(i+1)

#for i in range( 1,100):
#print (i)

for i in range(1,101,2):#nieparzyste skok o 2
    print(i)
    for i in range( 100,0, -1):
        print (i)
for litera in 'string':
    if litera=='i':
        break
    print(litera)
    print("koniec")

    for litera in 'string':
        if litera =='i':
            continue
        print(litera)
        print('koniec')

        liczba1=0
        while liczba1 <10:
            print(f'liczba to: {liczba1}')
            liczba1+=1

            liczba2=int(input('Podaj liczbe:'))
            while liczba2 <=0:
                liczba2= int(input('podaj liczbe jeszcze raz:'))

                def powitanie():
                    print('ziomsonpl to koks')
                    powitanie()
                    def powitanie_imienne(imie):
                        print(f'ziomsonpl to koks {imie}')
                        powitanie_imienne('ziomsonpl')
                        def dzielenie (dzielna, dzielnik):
                            if dzielnik==0:
                                return
                            else:
                                return dzielna/dzielnik
                            
                            wynik=dzielenie(10,2)
                            print(wynik)












































































