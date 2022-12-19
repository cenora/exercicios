from colorama import *
from random import randint

largura = 25
altura = 25
total = 31

arvore = ''
for x in range(1, total, 2):
    s = ''
    centro = int((largura-1)/2)
    espacamento = centro - int((x-1)/2)
    print('\n', end='')

    if x == 1:
        print(' '*espacamento, end='')
        print(Fore.RED + '*', end='')
    elif x < altura:
        print(' '*espacamento, end='')
        for y in range(0, x):
            a = randint(0, largura)
            b = randint(0, largura)
            c = randint(0, largura)
            if y == a:
                print(Fore.YELLOW + 'o', end='')
            elif y == b:
                print(Fore.CYAN + '@', end='')
            elif y == c:
                print(Fore.RED + '+', end='')
            else:
                print(Fore.GREEN + '^', end='')
    elif x == total:
        print(' '*espacamento, end='')
        print(Fore.BLUE + '#'*largura, end='')
    elif x > altura and x < total:
        print(' '*centro, end='')
        print(Fore.MAGENTA + 'II', end='')
print('\n', end='')
print(("~"*largura))
print(Fore.RED + "        FELIZ NATAL      ")
print(Fore.RED + "            E            ")
print(Fore.RED + "     FELIZ ANO NOVO!     ")
print(("~"*largura))
