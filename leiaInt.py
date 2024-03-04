def leiaInt(msg):
    n = input(f'{msg} ')
    while n.isdigit() == False:
        n = input('ERRO Digite um número inteiro! ')
    return n

n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número: {n}')