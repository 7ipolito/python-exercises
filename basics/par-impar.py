from random import randint


vitorias_consecutivas = 0
while True:
    n = int(input("Voce quer jogar (1-par/2-impar)"))
    maquina = randint(1, 2)  # 1 ou 2
    if maquina != n:
        print("Voce perdeu")
        break
    print("Voce ganhou")
    vitorias_consecutivas += 1

if vitorias_consecutivas >= 1:
    print("Voce teve {} vitoria(s) consecutivas".format(vitorias_consecutivas))
