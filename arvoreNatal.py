# To change font colors (https://github.com/tartley/colorama)
from colorama import *
from random import randint

largura = 25  # Tree largura
altura = 25  # Height without stand
total = 31  # Total height

tree = ''
for x in range(1, total, 2):
    s = ''
    center = int((largura-1)/2)
    padding = center-int((x-1)/2)

    print('\n', end='')

    if x == 1:
        print(' '*padding, end='')
        print(Fore.RED + '*', end='')
    elif x < altura:
        print(' '*padding, end='')
        for y in range(0, x):
            b = randint(0, largura)  # Location to add random decoration 1
            a = randint(0, largura)  # Add random decoration 2
            c = randint(0, largura)  # Add random decoration 3
            if y == b:
                print(Fore.YELLOW + 'o', end='')
            elif y == a:
                print(Fore.CYAN + '@', end='')
            elif y == c:
                print(Fore.RED + '+', end='')
            else:
                print(Fore.GREEN + '^', end='')

    elif x == altura:
        print(' '*padding, end='')
        print(Fore.BLUE + '#'*largura, end='')
    elif x > altura and x < total:
        print(' '*center, end='')
        print(Fore.MAGENTA + 'II', end='')

print('\n', end='')
print(("~"*largura))
print(Fore.RED + "     MERRY CHRISTMAS     ")
print(Fore.RED + "           AND           ")
print(Fore.RED + "     HAPPY HOLIDAYS !    ")
print(("~"*largura))
