'''
Faça um Programa que leia um
vetor de 5 números inteiros e mostre-os.
'''

lista = []
a = 1
# Para cada num dentre os 0 a 4
for num in range(5):
    lista.append(input("Digite um número: "))

# mostra lista no formato lista
print(lista)
for n in lista:
    print(n)
