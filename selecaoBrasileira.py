print("<< Escale a sua Seleção Brasileira >>")
jogadores = ["Alisson - 1", "Ederson - 23", "Weverton - 12", "Danilo - 2", "Alex Sandro - 6", "Daniel Alves - 13", "Alex Telles - 16", "Militão - 14", "Marquinhos - 4", "Thiago Silva - 3", "Bremer - 24", "Bruno Guimarães - 17", "Casemiro - 5",
             "Fabinho - 15", "Fred - 8", "Paquetá - 7", "Everton Ribeiro - 22", "Neymar - 10", "Vinicius Júnior - 20", "Antony - 19", "Rodrygo - 21", "Raphinha - 11", "Richarlison - 9", "Pedro - 25", "Gabriel Jesus - 18", "Gabriel Martinelli - 26"]

time = {
    1: ["Alisson", "GOL"],
    23: ["Ederson", "GOL"],
    12: ["Weverton", "GOL"],
    2: ["Danilo", "LD"],
    6: ["Alex Sandro", "LE"],
    13: ["Daniel Alves", "LD"],
    16: ["Alex Telles", "LE"],
    14: ["Militão", "ZC"],
    4: ["Marquinhos", "ZC"],
    3: ["Thiago Silva", "ZC"],
    24: ["Bremer", "ZC"],
    17: ["Bruno Guimarães", "MC"],
    5: ["Casemiro", "VOL"],
    15: ["Fabinho", "VOL"],
    8: ["Fred", "MC"],
    7: ["Paquetá", "MEI"],
    22: ["Everton Ribeiro", "MEI"],
    10: ["Neymar", "ATQ"],
    20: ["Vinicius Júnior", "ATQ"],
    19: ["Antony", "ATQ"],
    21: ["Rodrygo", "ATQ"],
    11: ["Raphinha", "ATQ"],
    9: ["Richarlison", "ATQ"],
    25: ["Pedro", "ATQ"],
    18: ["Gabriel Jesus", "ATQ"],
    26: ["Gabriel Martinelli", "ATQ"]
}
jogadores.sort()

print("Lista de Convocados: ")
for camisa, nome in time.items():
    print(camisa, nome[0], nome[1])


time_oficial = {}
while len(time_oficial) < 11:
    escolha = input("Escolha um jogador pela camisa: ")
    time_oficial[escolha] = time.get(int(escolha))
print(time_oficial)
