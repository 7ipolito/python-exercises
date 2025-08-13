nome = input("Digite o nome do jogador: ")
qtdPartidas = int(input("Digite a quantidade de partidas que ele jogou: "))
dictStats = {}
dictStats['jogador'] = nome
gols =[]
for c in range(0, qtdPartidas+1):
    golsPartida = int(input("Gols do {} na partida {}: ".format(nome,c)))
    gols.append(golsPartida)

dictStats['gols'] = gols
golsTotais = 0
for c, v in enumerate(gols):
    golsTotais += v

dictStats['total'] = golsTotais

print(dictStats)

for k,v in dictStats.items():
    print("O campo {} tem o valor {}".format(k, v))

print("O jogador {} jogou {} partidas".format(nome,qtdPartidas))

for c, v in enumerate(gols):
    print("Na partida {} fez {:.2f} gols.".format(c,v))
print("Foi um total de {} gols".format(golsTotais))