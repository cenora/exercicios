# import json
# from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def get_content(camisa, nome):
    return f"[b]{nome[0]}[/b]\n[yellow]Camisa: {camisa}\n[b]Pos.:{nome[1]}[/b]"


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

console = Console()


user_renderables = [Panel(get_content(camisa, nome), expand=True)
                    for camisa, nome in time.items()]
console.print(Columns(user_renderables))
print("<< Escale a sua Seleção Brasileira >>")
time_oficial = {}
while len(time_oficial) < 11:
    escolha = input("Escolha um jogador pela camisa: ")
    time_oficial[escolha] = time.get(int(escolha))
user_renderables = [Panel(get_content(camisa, nome), expand=True)
                    for camisa, nome in time_oficial.items()]
console.print(Columns(user_renderables))
