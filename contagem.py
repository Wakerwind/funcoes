from time import sleep

def line():
    print('-='*40)

line()

def contReg(start, end, step):

    print(f'Contagem de {start} até {end} de {step} em {step}')

    for n in range(start, end, -step):
        print(f'{n} ',end="")
        sleep(0.3)
    print('FIM')

'''print('Contagem de 1 até 10 de 1 em 1')
for n in range(1,11):
    print(f'{n} ' ,end="")
    sleep(0.3)
print('FIM')
line()

print('Contagem de 10 até 0 de 2 em 2')
for n in range(10, -1,-2):
    print(f'{n} ',end="")
    sleep(0.3)
print('')'''
line()

print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

if start > end:
    contReg(start, end, step)

