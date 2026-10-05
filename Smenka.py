from random import randint as ran
a, t, ln = [], [], 10
for _ in range(ln): t.append(":ˉ ")
for _ in range(ln): a.append(t.copy())
x, y = ln//2, ln//2
g = [[x, y]]
a[g[0][1]][g[0][0]] = "[O]"
def mit(g):
    global a
    a[g[0][1]][g[0][0]] = "[O]"
    if len(g) == 1: return 0
    for i in range(1, len(g)):
        a[g[i][1]][g[i][0]] = f"[{i}" if len(str(i)) == 2 else f"[{i}]"
def prt():
    print("\n")
    for i in range(ln): print(*a[i], sep="")
def grt():
    global a
    f, d = 0, 0
    for iy in range(ln):
        for ix in range(ln):
            if a[iy][ix] == "[+]" or a[iy][ix] == ":+ˉ": f += 1
            elif a[iy][ix] == "[ ]" or a[iy][ix] == ":ˉ ": d += 1
    if d < 7: c = d
    else: c = 6
    if   f < 10: 0
    else: return 0
    if d != 0:
        for _ in range(ran(1, c)):
            while True:
                xa, ya = ran(0, ln-1), ran(0, ln-1)
                k = False
                for i in range(len(g)):
                    if g[i][0] == xa and g[i][1] == ya or a[ya][xa] == "[+]" or a[ya][xa] == ":+ˉ": k = True
                if k: 0
                else:
                    if a[ya][xa] == ":ˉ ": a[ya][xa] = ":+ˉ"
                    else:                  a[ya][xa] = "[+]"
                    break
def stn(g):
    for i in range(len(g)):
        if   g[i][0] ==   -1:
             g[i][0] =  ln-1
        elif g[i][0] == ln:
             g[i][0] =     0
        if   g[i][1] ==   -1:
             g[i][1] =  ln-1
        elif g[i][1] == ln:
             g[i][1] =     0
    return g
grt()
prt()
v, p = 0, "w"
print("Wasd")
while True:
    if len(g) == ln*ln:
        print("\nYou Wooon")
        break
    b = input(f" {v} Points: ")
    if b == "": b = p
    else:       p = b
    if   b == "w": ny = g[0][1] - 1
    elif b == "s": ny = g[0][1] + 1
    else:          ny = g[0][1]
    if   b == "a": nx = g[0][0] - 1
    elif b == "d": nx = g[0][0] + 1
    else:          nx = g[0][0]
    nx, ny = stn([[nx, ny]])[0][0], stn([[nx, ny]])[0][1]
    if a[ny][nx] == "[+]" or a[ny][nx] == ":+ˉ":
        v += 1
        grt()
        g.append([0, 0])
        h = 1
        if len(g)-1 == 1: g[1] = g[0].copy()
    else:
        a[g[-1][1]][g[-1][0]] = "[ ]"
        h = 0
    for i in range(-len(g), 0):
        g[abs(i+1)] = g[abs(i+1)-1].copy()
    g[0][1] = ny
    g[0][0] = nx
    g = stn(g)
    Ex = False
    for i_ in range(len(g)):
        for i in range(len(g)):
            if i_ == i: 0
            else:
                if g[i_] == g[i]:
                    Ex = True
                    print("\nYou're Dead.")
            if Ex: break
        if Ex: break
    if Ex: break
    mit(g)
    prt()
input()