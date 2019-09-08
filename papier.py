print('wybierz papier kamien lub nozyczki')
from random import randint
player = input('papier (p) kamien (k) nazyczki (n)? ')
print('komputer vs player')

liczba_wylosowana = randint(1,3)

#1 = papier 2 = kamien 3 = nozyczki
if liczba_wylosowana == 1:
    komputer = 'p'
if liczba_wylosowana == 2:
    komputer = 'k'
if liczba_wylosowana == 3:
    komputer = 'n'


print('Komputer wybral %s a gracz wybral %s' % (komputer, player))

#jesili są takie same jest remis papier owija kamien kamien tempi nozyczki nozyczk tną papier
if player == komputer :
    print('Remis')
elif player == 'p' and komputer == 'k':
    print ('gratulacje wygrałeś')
elif player == 'k' and komputer == 'n':
    print ('gratulacje wygrałeś')
elif player == 'n' and komputer == 'p':
    print ('gratulacje wygrałeś')
elif player == 'p' and komputer == 'n':
    print ('przegrałeś')
elif player == 'k' and komputer == 'p':
    print('przegrałeś')
elif player == 'n'and komputer == 'k':
    print('przegrałeś')
