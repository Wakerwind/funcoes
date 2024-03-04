


def voto(nasc):
    # Quando fazemos uma importação dentro de uma função ele só funciona nela
    # Isso economiza memóri, porque seu uso se restringe à essa função
    from datetime import date

    nasc = date.today().year - nasc

    if nasc in [16,17] or nasc > 70:
        return 'Facultativo'
    elif nasc > 17:
        return 'Obrigatório'
    else: return 'Negado'

ano = int(input('Digite seu ano de nascimento: '))

situacao = voto(ano)

print(f'O seu voto é {situacao}')