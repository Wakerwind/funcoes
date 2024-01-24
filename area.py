def area(largura, comprimento):

    print(f'A área do terreno {largura}X{comprimento} é: {largura*comprimento}m²')

largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do torreno (m): '))

area(largura,comprimento)


#Usando Lambda

'''largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do torreno (m): '))

# Atribuo a operação da lambda à variável boa, para chamarmos a função por ela
area = lambda l, c: l*c

# result recebe o resultado da lambda dentro de area, passando como parâmetro as variáveis largura e comprimento
result = area(largura,comprimento)
print(f'A área do terreno {largura}X{comprimento} é: {result}m²')'''