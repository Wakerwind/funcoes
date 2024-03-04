def fat(num, show = False):

    f = 1
    if show == False:

        for c in range(num, 0, -1):
            f *= c

    else:

        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c} = ',end="")
            else:
                print(f'{c} X ', end="")
            f *= c
    return f
valor = int(input('Digite um número: '))
print(fat(valor,False))