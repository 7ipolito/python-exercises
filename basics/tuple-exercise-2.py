vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input('Digite uma palavra: ')
for p in sorted(palavra):
    if p in vogais:
        print('Vogal encontrada {}'.format(p))