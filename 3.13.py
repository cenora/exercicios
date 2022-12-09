base = int(input("Digite a base: "))  # 2
ex = int(input("Digite o expoente: "))  # 4
resultado = 1
for contador in range(ex):
    resultado *= base
print(resultado)
