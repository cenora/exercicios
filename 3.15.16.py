# 0,1,1,2,3,5,8,13,21....
# P,S,
#  ,P,S
#    ,P,S
# 15 Até o N termo
# 16 Até o 500 número
primeiro = 0
segundo = 1
termo = 0
número = 0
contador = 0

termo = int(input("Digite o valor de N: "))
while(contador < termo or primeiro <= 500):
    primeiro, segundo = primeiro + segundo, primeiro
    # número = primeiro + segundo
    # segundo = primeiro
    # primeiro = número
    print(primeiro)
    contador += 1
