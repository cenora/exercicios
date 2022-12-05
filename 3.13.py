base = int(input("Digite a base: "))  # 2
ex = int(input("Digite o expoente: "))  # 4
numero = 1
while(numero < ex):
    base *= base
    numero += 1

print(base)
