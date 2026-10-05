import tkinter as tk
from random import randint as ran
a = tk.Tk()
a.title("Mir")
a.geometry("1000x800")
e = tk.Canvas(a, width=1000, height=10000)
e.pack()
e.create_line(100, 700, 900, 700)
e.create_line(100, 0, 100, 700)
e.create_line(900, 0, 900, 700)
r = 50
x, y = ran(100+r, 900-r), ran(r, 700-r)
x1, y1, x2, y2 = x-r , y-r, x+r, y+r
sx, sy = ran(-500, 500), ran(-100, 250)
d = e.create_oval(x1, y1, x2, y2)
sl = e.create_line(x1+r, y1+r, x1+r+sx, y1+r+sy)
g = 4
def ud():
    global x1, y1, x2, y2, sx, sy
    e.coords(d, x1, y1, x2, y2)
    e.coords(sl, x1+r, y1+r, x1+r+sx, y1+r+sy)
    x1 += sx; y1 += sy; x2 += sx; y2 += sy
    sy += g + 1.29 * -abs(sy) / 100 if y2 < 700 else 0
    if y2 >= 700:
        y_ = y2 - 700
        y1 = 600 - y_ * 0.8
        y2 = 700 - y_ * 0.8
        if sy > g: sy *= -0.7 if sy > g * 3.68 else -0.5
        if abs(sy) < g: sy = 0
    if sx > 0: sx -= 1.29 * sx / 100
    elif sx < 0: sx += 1.29 * abs(sx) / 100
    if x2 >= 900:
        x_ = x2 - 900
        x1 = 800 - x_ * 0.8
        x2 = 900 - x_ * 0.8
        if sx > 0: sx *= -0.8
    elif x1 <= 100:
        x_ = 100 - x1
        x1 = x_ * 0.8 + 100
        x2 = x_ * 0.8 + 200
        if sx < 0: sx *= -0.8
    a.after(25, ud)
ud()
a.mainloop()