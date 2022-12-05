'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''

from rich.progress import track
from time import sleep


def scrape_data():
    sleep(0.1)


if __name__ == '__main__':
    nome = ""
    while len(nome) < 3:
        nome = input("Qual o seu nome? [Maior que 3]")

    idade = 0
    while idade > 0 and idade <= 100:
        idade = int(input("Quantos anos você têm? "))

    salario = 0
    while salario <= 0:
        salario = float(input("Quanto você ganha? "))

    sexo = input("Masculino - 'm' ou Feminino - 'f'")
    civil = input(
        "Solteiro - 's', Casado - 'c', Viúvo - 'v' ou Divorciado - 'd'")


#    for _ in track(range(50), description='[green]Loading'):
#        scrape_data()
