def titulo(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'{msg:^{tam}}')
    print(f'~' * tam)

titulo('Cev')