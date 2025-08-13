listaNumeros = []

while True:
    c = int(input('Insira um número (999 para parar): '))
    if c == 999:
        break
    if c not in listaNumeros:
        # Inserir no lugar certo para manter a ordem
        if not listaNumeros or c > listaNumeros[-1]:
            listaNumeros.append(c)
            print("Adicionado no final da lista")
        elif c < listaNumeros[0]:
            listaNumeros.insert(0, c)
            print("Adicionado no início da lista")
        else:
            # Inserção no meio
            for i in range(len(listaNumeros)):
                if listaNumeros[i] > c:
                    listaNumeros.insert(i, c)
                    print(f"Adicionado na posição {i} da lista")
                    break
    else:
        print("Valor já existe na lista, não será adicionado.")

print("Lista final:", listaNumeros)
