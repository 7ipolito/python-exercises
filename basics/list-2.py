galera = list()
dado = list()
totmaior = 0
totmenor = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print('{} é menor de idade'.format(p[0]))
        totmaior +=1
    else:
        print('{} é maior de idade'.format(p[0]))
        totmenor -=1
