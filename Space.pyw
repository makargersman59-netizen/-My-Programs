import tkinter as tk

w = tk.Canvas(Wo, width=4000, height=2000, bg="black")
w.pack()


S = {
    "x1": 940, "y1": 520,
                
               "x2": 980, "y2": 560,
    "sx": 0, "sy": 0,
    "m": 1.98e30
}
So = w.create_oval(S["x1"], S["y1"], S["x2"], S["y2"], fill="orange", outline="yellow")

M = {
    "x1": 782, "y1": 537,
                
               "x2": 788, "y2": 543,
    "sx": 0, "sy": -2.58,
    "m": 3.3e23
}
Mo = w.create_oval(M["x1"], M["y1"], M["x2"], M["y2"], fill="#979385", outline="#979385")

V = {
    "x1": 639, "y1": 535,
                
               "x2": 649, "y2": 545,
    "sx": 0, "sy": -1.929,
    "m": 4.87e24
}
Vo = w.create_oval(V["x1"], V["y1"], V["x2"], V["y2"], fill="red", outline="orange")

E = {
    "x1": 505, "y1": 535,
                
               "x2": 515, "y2": 545,
    "sx": 0, "sy": -1.625,
    "m": 5.97e24
}
Eo = w.create_oval(E["x1"], E["y1"], E["x2"], E["y2"], fill="green", outline="blue")

L = {
    "x1": 531.45, "y1": 538,
                
               "x2": 535.45, "y2": 542,
    "sx": 0, "sy": -0.2,
    "m": 7.35e22
}
Lo = w.create_oval(L["x1"], L["y1"], L["x2"], L["y2"], fill="white", outline="white")


def Sup(sx, sy, m1, m2, cx1, cy1, cx2, cy2):
    x, y = abs( cx1 - cx2 ), abs( cy1 - cy2 )
    G = 6.6743 / 1e11
    r = ( ( cx1 - cx2 )**2 + ( cy1 - cy2 )**2 )**0.5
    if m2 == 7.35e22:
        if m1 == 1.980e30: u = 1e9 / 3
        else: u = 9e6 / 3
    else: u = 1e9 / 3
    g = ( m1 / ( r * u )**2 ) * G
    if cx1 - cx2 < 0: sx -= g * ( x / r )
    else: sx += g * ( x / r )
    if cy1 - cy2 < 0: sy -= g * ( y / r )
    else: sy += g * ( y / r )
    return sx, sy


def ud():
    global w, S, So, M, Mo, V, Vo, E, Eo, L, Lo
    cxS, cyS = S["x1"] + 20, S["y1"] + 20
    cxE, cyE = E["x1"] + 5, E["y1"] + 5
    cxL, cyL = L["x1"] + 2, L["y1"] + 2
    cxM, cyM = M["x1"] + 3, M["y1"] + 3
    cxV, cyV = V["x1"] + 5, V["y1"] + 5
    S["sx"], S["sy"] = Sup(S["sx"], S["sy"], E["m"], S["m"], cxE, cyE, cxS, cyS)
    E["sx"], E["sy"] = Sup(E["sx"], E["sy"], S["m"], E["m"], cxS, cyS, cxE, cyE)
    L["sx"], L["sy"] = Sup(L["sx"], L["sy"], E["m"], L["m"], cxE, cyE, cxL, cyL)
    S["sx"], S["sy"] = Sup(S["sx"], S["sy"], L["m"], S["m"], cxL, cyL, cxS, cyS)
    L["sx"], L["sy"] = Sup(L["sx"], L["sy"], S["m"], L["m"], cxS, cyS, cxL, cyL)
    M["sx"], M["sy"] = Sup(M["sx"], M["sy"], S["m"], M["m"], cxS, cyS, cxM, cyM)
    V["sx"], V["sy"] = Sup(V["sx"], V["sy"], S["m"], V["m"], cxS, cyS, cxV, cyV)
        #w.create_line(cxE, cyE, cxE + E["sx"], cyE + E["sy"], fill="lightblue")
        #w.create_line(cxL, cyL, cxL + L["sx"], cyL + L["sy"], fill="white")
        #w.create_line(cxM, cyM, cxM + M["sx"], cyM + M["sy"], fill="lightyellow")
        #w.create_line(cxV, cyV, cxV + V["sx"], cyV + V["sy"], fill="red")
    S["x1"] += S["sx"]; S["y1"] += S["sy"]; S["x2"] += S["sx"]; S["y2"] += S["sy"]
    E["x1"] += E["sx"]; E["y1"] += E["sy"]; E["x2"] += E["sx"]; E["y2"] += E["sy"]
    L["x1"] += L["sx"]; L["y1"] += L["sy"]; L["x2"] += L["sx"]; L["y2"] += L["sy"]
    M["x1"] += M["sx"]; M["y1"] += M["sy"]; M["x2"] += M["sx"]; M["y2"] += M["sy"]
    V["x1"] += V["sx"]; V["y1"] += V["sy"]; V["x2"] += V["sx"]; V["y2"] += V["sy"]
    w.coords(Eo, E["x1"], E["y1"], E["x2"], E["y2"])
    w.coords(So, S["x1"], S["y1"], S["x2"], S["y2"])
    w.coords(Lo, L["x1"], L["y1"], L["x2"], L["y2"])
    w.coords(Mo, M["x1"], M["y1"], M["x2"], M["y2"])
    w.coords(Vo, V["x1"], V["y1"], V["x2"], V["y2"])
    w.after(6, ud)

ud()
w.mainloop()