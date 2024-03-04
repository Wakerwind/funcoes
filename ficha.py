def ficha(name = '<desconhecido>',gol = 0):

    print(f'O jogador {nome} fez {gols}!')

nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome,gols)