'''
Faça um programa que calcule
o mostre a média aritmética de N notas.
'''
soma = 0
numeros = 0
contador = 0
resposta = True

while(resposta):
    numeros = int(input("Informe um número: "))
    contador += 1
    soma += numeros
    resposta = input("Deseja continuar? S/N \n")
    if(resposta != "S"):
        break
print(f'MÉDIA: {soma/contador}')
