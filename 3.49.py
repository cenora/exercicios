'''
Faça um programa que mostre os n termos da Série a seguir:
      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
      N=5 -> 3.393650793650793650
    Imprima no final a soma da série.
'''

valor = input("Digite o valor de N: ")
soma = 0
contador = 0
expressao = "S = "
n, m = 1, 1

while(contador < int(valor)):
    soma += float(n)/float(m)
    contador += 1
    expressao = expressao + f"+ {str(n)}/{str(m)}"
    n += 1
    m += 2
print(f"{expressao} ... {soma}")
