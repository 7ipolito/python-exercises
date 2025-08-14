def maior(* num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print(maior)


maior(2, 4, 7, 6)