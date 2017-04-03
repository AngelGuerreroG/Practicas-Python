from random import randint, choice

def cambio(coord, largo):
    coord += choice([1, -1])
    if coord > largo:
        coord -= largo
    elif coord < largo:
        coord += 0
    return coord

n = 50
dur = 30
k = 3
pos = [randint(0, n) for part in range(k)]
simb = '#*Xo'
nada = '-'

for paso in range(dur):
    mapa = [nada for celda in range(n)]
    for p in range(k):
        coord = pos[p]
        s = simb[p]
        mapa[coord] = s
        pos[p] = cambio(coord, n)
    print(''.join(mapa))


