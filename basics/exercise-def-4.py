def ficha(nome='Jogador', gols= 0):
    if gols == 0:
        return('O jogador {} não tem numeros'.format(nome))
    else:
        return('O jogador {} tem {} na carreira'.format(nome, gols)) 

print(ficha(nome="Allan", gols=10))