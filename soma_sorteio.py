from random import sample as s, randint



def sorteia():
    numeros = []

    for n in range(5):
        numeros.append(randint(0,10))

    print(f'Números sorteados: {numeros}')
    somaPar(numeros)

def somaPar(numeros):

    soma = 0
    for val in numeros:

        if val % 2 == 0:
            soma += val
    print(f'Somando os valores pares de {numeros}, temos {soma}')
sorteia()