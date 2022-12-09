'''
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
Altere o programa anterior para que ele aceite apenas
números entre 0 e 1000.
'''
soma = 0
maior = -1
menor = 2000
conjunto = -1
resposta = True

while(resposta):
    while(conjunto < 0 or conjunto > 1000):
        conjunto = int(input("Informe um número entre 0 e 1000: "))

    soma += conjunto

    if conjunto > maior:
        maior = conjunto
    if conjunto < menor:
        menor = conjunto

    resposta = input("Deseja continuar? S/N \n")
    if(resposta != "S"):
        break

    conjunto = -1
print(f'''
MAIOR: {maior}
MENOR: {menor}
SOMA: {soma}
''')
