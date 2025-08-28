def aumentar(m):
    return m + 1

def diminuir(m):
    return m - 1

def dobro(m):
    return m * 2

def metade(m):
    return m /2

def formatMoeda(m, toFormat=True):
    if toFormat:    
        return 'R$'+ m
    else:
        return m
