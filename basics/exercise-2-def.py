def fatorial (n, show= True):
    f = 1 
    for c in range(n, 0, -1):
        f *= c
        if show:
            print('{} X {} = {}'.format(n, c, f))
    print('O fatorial de {} é {}'.format(n,f))


fatorial(5, True)