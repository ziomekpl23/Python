'''
Konwerter jednostek: mile i kilometry
'''
def print_menu():
 print('1. Kilometry na mile')
 print('2. Mile na kilometry')
def km_miles():
 km = float(input('Wpisz odległość wyrażoną w kilometrach: '))
 miles = km / 1.609

 print('Odległość wyrażona w milach: {0}'.format(miles))

def miles_km():
 miles = float(input('Wpisz odległość wyrażoną w milach: '))
 km = miles * 1.609

 print('Odległość wyrażona w kilometrach: {0}'.format(km))
if __name__ == '__main__':
 print_menu() 
 choice = input('Wybierz rodzaj konwersji, którą chcesz wykonać: ') 
 if choice == '1':
    km_miles()

 if choice == '2':
    miles_km() 