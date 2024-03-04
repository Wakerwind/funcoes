from random import sample as s, randint

def maior(* num):
    cont = 0
    maior = 0

    print(f'Analisando os valores passados...')
    for valor in num:
        print(f'{valor}',end='')
        cont +=1

        if valor > maior:
            maior = valor
    print()
    print(f'Foram analisados {cont} números')
    print(f'O maior deles é {maior}')



maior(1,3,2,6)