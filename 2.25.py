# by Pedro
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de
# 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
# preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota
# de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("valor do saque")
vs = int(input())
n1 = int(vs/100)
n2 = int((vs % 100)/50)
n3 = int(((vs % 100) % 50)/10)
n4 = int((((vs % 100) % 50) % 10)/5)
n5 = int(((((vs % 100) % 50) % 10) % 5)/1)

vs >= 10 and vs <= 600
# nota de 100

if n1 == 1:
    n1 = ("uma notas de 100")
if n1 == 2:
    n1 = ("duas notas de 100")
if n1 == 3:
    n1 = ("três notas de 100")
if n1 == 4:
    n1 = ("quatro notas de 100")
if n1 == 5:
    n1 = ("cinco notas de 100")
if n1 == 6:
    n1 = ("seis notas de 100")

# nota de 50

if n2 == 1:
    n2 = ('uma nota de 50')

# nota de 10

if n3 == 1:
    n3 = ("uma nota de 10")
if n3 == 2:
    n3 = ("duas notas de 10")
if n3 == 3:
    n3 = ("três notas de 10")
if n3 == 4:
    n3 = ("quatro notas de 10")

# nota de 5

if n4 == 1:
    n4 = ("uma nota de 5")

# nota 1

if n5 == 1:
    n5 = ("uma nota 1")
if n5 == 2:
    n5 = ("duas notas 1")
if n5 == 3:
    n5 = ("três notas 1")
if n5 == 4:
    n5 = ("quatro notas 1")

if vs <= 600 and vs >= 100:
    if n2 == 0 and n3 == 0 and n4 == 0 and n5 == 0:
        print(f"Para sacar a quantia de {vs} reais,o programa fornece {n1}")
    elif n3 == 0 and n4 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1} e {n2}")
    elif n2 == 0 and n4 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1} e {n3}")
    elif n2 == 0 and n3 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1} e {n4}")
    elif n2 == 0 and n3 == 0 and n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1} e {n5}")
    elif n4 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2} e {n3}")
    elif n3 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2} e {n4}")
    elif n3 == 0 and n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2} e {n5}")
    elif n2 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n3} e {n4}")
    elif n2 == 0 and n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n3} e {n5}")
    elif n2 == 0 and n3 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n4} e {n5}")
    elif n2 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n3}, {n4} e {n5}")
    elif n3 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2}, {n4} e {n5}")
    elif n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2}, {n3} e {n5}")
    elif n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece {n1}, {n2}, {n3} e {n4}")
    else:
        print(
            f"Para sacar a quantia de {vs} reais,o programa fornece,{n1}, {n2}, {n3}, {n4} e {n5}")
elif vs <= 99 and vs >= 50:
    if n3 == 0 and n4 == 0 and n5 == 0:
        print(f"Para sacar a quantia de {vs} reais, o programa fornece {n2}")
    elif n4 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2} e {n3}")
    elif n3 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2} e {n4}")
    elif n3 == 0 and n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2} e {n5}")
    elif n3 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2}, {n4} e {n5}")
    elif n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2}, {n3} e {n5}")
    elif n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n2}, {n3} e {n4}")
    else:
        (f"Para sacar a quantia de {vs} reais, o programa fornece {n2}, {n3}, {n4} e {n5}")
elif vs <= 49 and vs >= 10:
    if n4 == 0 and n5 == 0:
        print(
            f"Para sacar a quantia de {vs}  reais, o programa fornece e {n3}")
    elif n4 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n3} e {n5}")
    elif n5 == 0:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n3} e {n4}")
    else:
        print(
            f"Para sacar a quantia de {vs} reais, o programa fornece {n3},{n4} e {n5}")

elif vs <= 9 and vs >= 5:
    if n5 == 0:
        print(f"Para sacar a quantia de {vs}  reais, o programa fornece {n4}")
    else:
        print(
            f"Para sacar a quantia de {vs}  reais, o programa fornece {n4} e {n5}")
elif vs <= 4 and vs >= 1:
    print(f"Para sacar a quantia de {vs} reais, o programa fornece {n5}")
else:
    print("Informe numero maior que 600 e maior que 10")
