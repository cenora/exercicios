from colorama import Back, Style

s = ""
for faixa in range(23):
    if faixa % 2 == 0:
        s += Back.BLUE+"     "+Style.RESET_ALL
    else:
        s += Back.WHITE+"     "+Style.RESET_ALL
    # print(f"{s}\n")

for altura in range(30):
    print(s)
