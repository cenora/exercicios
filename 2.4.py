'''
Faça um Programa que verifique se uma
letra digitada é vogal ou consoante.
'''

letra = input("Digite um letra: ")
if(letra == "a" or letra == "e" or letra == "i"
   or letra == "o" or letra == "u"):
    print(f"{letra} é vogal")
else:
    print(f"{letra} é consoante")

# outra forma
letra = "C"
lista = ["a", "e", "i", "o", "u"]
vogal = False
for letter in lista:
    if(letra == letter):
        vogal = True
if(vogal):
    print(f"{letra} é vogal")
else:
    print(f"{letra} é consoante")


# outra forma
letra = "c"
vogal = ("a", "e", "i", "o", "u")
if(letra in vogal):
    print(f"{letra} é vogal")
else:
    print(f"{letra} é consoante")
