'''
Faça um Programa que leia 2 números e em seguida
pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
escolha = int(input('''
1   ->  Adição
2   ->  Divisão
3   ->  Multiplicação
4   ->  Subtração
Escolha um número:
'''))

resultado = 0
expressao = ""

if(escolha == 1):
    resultado = a + b
if(escolha == 2):
    resultado = a / b
if(escolha == 3):
    resultado = a * b
if(escolha == 4):
    resultado = a - b

if resultado % 2 == 0:
    expressao += f"{resultado} é par, "
else:
    expressao += f"{resultado} é ímpar, "

if resultado >= 0:
    expressao += "positivo, "
else:
    expressao += "negativo, "

if isinstance(resultado, int):
    expressao += "e inteiro."
else:
    expressao += "e decimal."

print(expressao)
