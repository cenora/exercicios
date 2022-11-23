import math

repetir = True

while(repetir):
    popA = -1
    while(popA < 0 or popA == ""):
        popA = int(input("Qual o tamanho da população A? \n"))
    popB = -1
    while(popB < 0):
        popB = int(input("Qual o tamanho da população B? \n"))
    taxA = -1
    while(taxA < 0):
        taxA = float(input("Qual a taxa de crescimento de A? \n"))
    taxB = -1
    while(taxB < 0):
        taxB = float(input("Qual a taxa de crescimento de B? \n"))
    anos = 0
    while(popB > popA):
        popA = math.ceil(popA * (1 + taxA/100))
        popB = math.ceil(popB * (1 + taxB/100))
        anos += 1
    print(f"""
    A população A {popA} cresce {taxA}%/por ano.
    A população B {popB} cresce {taxB}%/por ano.
    Levará {anos} anos para A ultrapassar B.

    Deseja repetir? S/N
    """)

    repetir = input()
    if(repetir == "N"):
        break
