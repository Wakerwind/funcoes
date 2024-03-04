def notas(* notas, sit = False):

    ficha = dict()

    ficha['total'] = len(notas)
    ficha['maior'] = max(notas)
    ficha['menor'] = min(notas)
    ficha['média'] = sum(notas) / len(notas)

    if sit == True:
        if ficha['média'] > 7:
            ficha['situação'] ='Boa'
        elif ficha >= 6:
            ficha['situação'] = 'Razoável'
        else:
            ficha['situação'] = 'Ruim'
    return ficha

resp = notas(5.5,6.7,9.5,sit=True)
print(resp)