'''
Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
'''

inferior = int(input("Digite o primeiro número: "))
superior = int(input("Digite o último número: "))

# cabe validar se inferior é menor que superior
soma = 0
while inferior < superior:
    inferior += 1
    if inferior == superior:
        break
    soma += inferior
    print(inferior)
print(f"Soma: {soma}")
