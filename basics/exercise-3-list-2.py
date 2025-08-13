lista = []

for l in range(4):
    lista.append([])

for l in range(0,4):
    for a in range(0, 4):
        valor = input('Digite um valor para [{},{}]: '.format(l,a))
        lista[l].append(valor)

for l in range(0,4):
    for a in range(0, 4):
        print(lista[l][a])
