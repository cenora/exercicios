def ValorPagamento(v, d):
    valor = float(v)*0.03+float(v)*(int(d)*0.001)+float(v)
    print(f"Valor à pagar: R${valor}")
    return valor


if __name__ == '__main__':
    d = 2
    q = 0
    v3 = 0
    while(int(d) > 0):
        v = input("Informe o valor da prestação: R$")
        d = input('Informe o número de dias em atraso: ')
        q += 1
        v3 += ValorPagamento(v, d)
    else:
        print(f"quantidade de prestações pagas: {q}")
        print(f"valor total de prestações pagas: R${v3}")
