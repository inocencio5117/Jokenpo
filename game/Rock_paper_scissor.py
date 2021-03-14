from random import randint


def linhas():
    print(70 * '-')


# cores:
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
fecha_cor = '\33[m'


opcoes = ['Pedra', 'Papel', 'Tesoura']
vitorias_comp = 0
vitorias_pl = 0

linhas()
print('JOKENPÔ!'.center(70))
linhas()
print('Digite o número correspondente a sua opção')

player_choice = None
while True:
    while True:
        player_choice = input('Pedra [0], Papel [1] ou tesoura [2]? [Para sair digite 99] ').strip()
        if player_choice.isalpha() is False and int(player_choice) in range(0, 3):
            break
        elif player_choice.isalpha() is False and int(player_choice) == 99:
            print(70 * '-')
            print('Jogo finalizado\nAté a próxima!')
            quit()

    computador = randint(0, 2)
    x = int(player_choice)
    print(70 * '~')

    print(f'Você jogou {opcoes[int(player_choice)]} e o computador jogou {opcoes[computador]}'.center(70))

    if opcoes[int(player_choice)] == opcoes[computador]:
        print(f'{amarelo}FOI UM EMPATE{fecha_cor}'.center(70))
    elif x == 0 and computador == 1:
        print(f'{vermelho}VOCÊ PERDEU{fecha_cor}'.center(70))
        vitorias_comp += 1
    elif x == 1 and computador == 2:
        print(f'{vermelho}VOCÊ PERDEU{fecha_cor}'.center(70))
        vitorias_comp += 1
    elif x == 2 and computador == 0:
        print(f'{vermelho}VOCÊ PERDEU{fecha_cor}'.center(70))
        vitorias_comp += 1
    elif x == 0 and computador == 2:
        print(f'{verde}VOCÊ GANHOU!{fecha_cor}'.center(70))
        vitorias_pl += 1
    elif x == 1 and computador == 0:
        print(f'{verde}VOCÊ GANHOU!{fecha_cor}'.center(70))
        vitorias_pl += 1
    elif x == 2 and computador == 1:
        print(f'{verde}VOCÊ GANHOU!{fecha_cor}'.center(70))
        vitorias_pl += 1
    print(f'''
Placar:
    Computador = {vitorias_comp}
    Você = {vitorias_pl}''')
    print(70 * '~')
