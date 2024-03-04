#Função de título
def msg(msg):

    print('-'*40)
    print(f'{msg:^40}')
    print('-' * 40)

#Função de soma
def soma(a, b):

    print(a+b)

# Ao colocar um * ao lado do parametro de uma função, criamos uma função que recebe vários valores
# E os coloca em uma tupla
def contador(* num):
    print(f'Recebi os valores {num} e são {len(num)} números ao total')

def dobrar(lista):

    pos = 0

    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(f'Dentro da função: {lista}')

#programa principal

'''

msg('Sistema de Alunos')

msg(str(input('Digite sua mensagem: ')))

txt = str(input('Digite outra mensagem: '))
msg(txt)

'''
soma(2,1)

# Podemos criar funções que recebem um número indeterminado de parâmetros

contador(1,2,5,3)
contador(4,5,2)

# Quando vc altera uma lista em outra função ela também sofre a alteração na função principal

# Toda passagem de parâmetro em Python é por referência, não por valor

lista = [1,2,3,4,5,6,7,8,9]
dobrar(lista)
print(f'fora da função: {lista}')

# Map aplica a lambda em cada membro da lista
# Usamos o list para converter o resultado em uma lista
# x é um parametro, após dos dois pontos é a operação a ser realizado com ele

lista = list(map(lambda x: x*2, lista))
print(f'Após usar o lambda: {lista}')

# Parametros opcionais

def somar(a, b, c = 0):
    a = 8
    s = a + b + c
    print(f'Soma = {s}')
a = 5
somar(a,2)
print(a)
# Aatribuir 0 ao parametro da função dizemos que ele é opcional
# A variável a mesmo sendo global não muda de valor
# Isso porque o a da função somar é uma variável diferente não a mesma
# para usar o a global é só colocar a palavra global ao lado do a:

def soma2():
    global d
    d = 10

    print(f'd como global na função soma 2 {d}')

d = 6
print(f'd na main: {d}')
soma2()
print(f'd na main denovo {d}')