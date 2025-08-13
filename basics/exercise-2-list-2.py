import random
lista = []
for n in range(0, 8):
    numeroUsuario = random.randint(1, 100)
    lista.append(numeroUsuario)
listaPares=[]
listaImpares=[]
for numero in lista:
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

print(listaPares)
print(listaImpares)