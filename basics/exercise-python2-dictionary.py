import random
from operator import itemgetter

print("Valores sorteados:")

listaValores=[]
dictJogadores={}
listaOrdenanada=[]
for c in range(0,5):
    numero=random.randint(0,100)
    print("O jogador {} tirou {}".format(c,numero))
    dictJogadores['jogador']='Jogador'+str(c)
    dictJogadores['numero']=numero
    listaValores.append(dictJogadores.copy())

print("Valores sorteados:")

for c,v in enumerate(listaValores):
    listaOrdenada = sorted(listaValores, key=itemgetter('numero'))

for c,v in enumerate(listaOrdenada):
    print("O jogador {} tirou {}".format(c,v['numero']))