from random import randint as ran
d, lnx, lny = [], 200, 100
f = { 0: "#", 1: "@", 2: "%", 3: "&", 4: "$", 5: "№", 6: " ", 7: " ", 8: " ", 9: " " }
for i in range(lny):
    t = []
    for _ in range(lnx): t.append(f[ran(0, len(f)-5)])
    d.append(t.copy())
a, g, h = [[lnx//2, lny//2, ran(2, 8), ran(0, len(f)-1)]], 30, 24
for i__ in range(h):
    b = len(a)
    for i_ in range( h-1 - i__ ):
        for i in range(ran(h//2-i__, h-i__)): a.append([a[i][0]+ran(-g, g), a[i][1]+ran(-g, g), ran(2, 8), ran(0, len(f)-1)])
for i in range(len(a)):
    for y in range(lny):
        for x in range(lnx):
            if ( ( a[i][0] - x )**2 + ( a[i][1] - y )**2 )**0.5 <= a[i][2]:d[y][x] = f[a[i][3]]
for i in range(lny): print(*d[i], sep="")
input()