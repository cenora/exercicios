'''
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula
entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101,
311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
centena = ""
dezena = ""
virgula = ""

numero = int(input("Digite um número menor que 1000: "))
if(numero > 100):
    centena = numero // 100
    numero = numero-centena*100
    if(centena == 1):
        centena = "1 centena"
    else:
        centena = f"{centena} centenas"

if(numero > 10):
    dezena = numero // 10
    numero = numero - dezena*10
    if(dezena == 1):
        dezena = "1 dezena"
    else:
        dezena = f"{dezena} dezenas"
    virgula = "" if centena == "" else ", "

if(numero > 1):
    numero = f"{numero} unidades"
elif(numero == 1):
    numero = "1 unidade"
else:
    numero = ""

e = ""
if(centena and numero != ""):
    e = " e "
elif(dezena):
    e = " e "
print(f"{centena}{virgula}{dezena}{e}{numero}")
