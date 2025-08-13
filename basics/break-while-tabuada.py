c = n = 0
while True:
    if n < 0:
        break
    n = int(input("Qual numero voce quer a tabuada? "))
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, c * n))

