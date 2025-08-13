pessoas = []

for pessoa in range(0,3):
    nome = input('Insira o nome de uma pessoa: ')
    peso = input('Insira o peso da pessoa: ')
    pessoas.append([nome,peso])

print('Foram inseridas {} pessoas'.format(len(pessoas)))
pessoas_ordenadas = sorted(pessoas)

for pessoa in pessoas_ordenadas:
    print(pessoa[0])
# Ordenar do mais pesado para o mais leve
pessoas_ordenadas_desc = sorted(pessoas, reverse=True)
print('Pessoas mais pesadas:', [p[0] for p in pessoas_ordenadas_desc])