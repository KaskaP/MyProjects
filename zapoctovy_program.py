import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from tkinter import *
from matplotlib.animation import FuncAnimation

m = []
n = 0
g = 1
start_pos = ""
start_velocity = ""
timeinterval = 0

#okénko pro vstup
root = Tk()
root.title("Vstup")
root.geometry("500x280")
souradnice = []

#náhled na zadávane body
fig = plt.figure
ax = plt.axes(projection="3d")
ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
plt.title("Simulace n hmotných bodů")
ax.set_xlabel('X-axis', fontweight='bold')
ax.set_ylabel('Y-axis', fontweight='bold')
ax.set_zlabel('Z-axis', fontweight='bold')

#funkce pro tlačítka
pocitadlo = 0
def vykresleni():
    global pocitadlo
    poloha = vstupP.get()
    if len(poloha.split()) == 3:
        if pocitadlo > 0:
            souradnice.pop()
            ax.clear()
            ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
            plt.title("Simulace n hmotných bodů")
            ax.set_xlabel('X-axis', fontweight='bold')
            ax.set_ylabel('Y-axis', fontweight='bold')
            ax.set_zlabel('Z-axis', fontweight='bold')
        souradnice.append([float(eval(poloha.split()[0])), float(eval(poloha.split()[1])), float(eval(poloha.split()[2]))])
        souradniceX = [element[0] for element in souradnice]
        souradniceY = [element[1] for element in souradnice]
        souradniceZ = [element[2] for element in souradnice]

        sctt = ax.scatter3D(souradniceX, souradniceY, souradniceZ,
                        alpha=0.8,
                        c='r',
                        marker='o')
    else:
        print("není vyplněna tabulka")
    pocitadlo += 1
    plt.show()

#pomocná funkce, na identifikaci čísel
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def dalsiPlaneta():
    global m
    global n
    global start_pos
    global start_velocity
    global timeinterval
    global rychlost_simulace
    global polohafinal
    global rychlostfinal
    global pocitadlo
    global g

    polohafinal = vstupP.get()
    rychlostfinal = vstupR.get()
    hmotnost = vstupH.get()
    zkouskapoloha = [eval(x) for x in polohafinal.split()]
    zkouskarychlost = [eval(x) for x in rychlostfinal.split()]
    if len(polohafinal.split()) == 3 and len(rychlostfinal.split()) == 3 and is_float(eval(hmotnost)) and all([is_float(_) for _ in zkouskapoloha]) and all([is_float(_) for _ in zkouskarychlost]):
        m.append(float(eval(hmotnost)))
        n += 1
        start_pos += " " + polohafinal
        start_velocity += " " + rychlostfinal
        g = float(eval(vstupG.get()))
        timeinterval = float(eval(vstupT.get()))
        rychlost_simulace = float(eval(vstupS.get()))

        vstupH.delete(0, END)
        vstupP.delete(0, END)
        vstupR.delete(0, END)

        if pocitadlo > 0:
            souradnice.pop()
            ax.clear()
            ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
            plt.title("Simulace n hmotných bodů")
            ax.set_xlabel('X-axis', fontweight='bold')
            ax.set_ylabel('Y-axis', fontweight='bold')
            ax.set_zlabel('Z-axis', fontweight='bold')

        souradnice.append([float(eval(polohafinal.split()[0])), float(eval(polohafinal.split()[1])), float(eval(polohafinal.split()[2]))])
        souradniceX = [element[0] for element in souradnice]
        souradniceY = [element[1] for element in souradnice]
        souradniceZ = [element[2] for element in souradnice]

        sctt = ax.scatter3D(souradniceX, souradniceY, souradniceZ,
                        alpha=0.8,
                        c='r',
                        marker='o')
    # show plot
    else:
        print("tabulka není správně vyplněna")
    pocitadlo = 0
    plt.show()


def predchoziPlaneta():
    global m
    global n
    global start_pos
    global start_velocity
    global polohafinal
    global rychlostfinal

    if n >= 1:
        m.pop()
        n -= 1
        start_pos = start_pos.rstrip(polohafinal)
        start_velocity = start_velocity.rstrip(rychlostfinal)
        souradnice.pop()

        ax.clear()
        ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
        plt.title("Simulace n hmotných bodů")
        ax.set_xlabel('X-axis', fontweight='bold')
        ax.set_ylabel('Y-axis', fontweight='bold')
        ax.set_zlabel('Z-axis', fontweight='bold')

        souradniceX = [element[0] for element in souradnice]
        souradniceY = [element[1] for element in souradnice]
        souradniceZ = [element[2] for element in souradnice]
        sctt = ax.scatter3D(souradniceX, souradniceY, souradniceZ,
                        alpha=0.8,
                        c='r',
                        marker='o')
    else:
        print("neni co rusit")

    plt.show()


def spustProgram():
    if n >= 1:
        root.destroy()
        plt.close()
    else:
        print("neni co pouštět")

# popisky okének pro vstup
popisH = Label(root, text="Hmotnost", font=("Arial", 15))
popisP = Label(root, text="Poloha", font=("Arial", 15))
popisR = Label(root, text="Rychlost", font=("Arial", 15))
popisG = Label(root, text="Grav. konst.", font=("Arial", 15))
popisT = Label(root, text="Čas simulace", font=("Arial", 15))
popisS = Label(root, text="Interval v animaci", font=("Arial", 15))

# vytvoreni vstupu
vstupH = Entry(root, width=30, font=("Arial", 15))
vstupP = Entry(root, width=30, font=("Arial", 15))
vstupR = Entry(root, width=30, font=("Arial", 15))
vstupG = Entry(root, width=30,  font=("Arial", 15))
vstupG.insert(0, "1")
vstupT = Entry(root, width=30, font=("Arial", 15))
vstupT.insert(0, "10")
vstupS = Entry(root, width=30, font=("Arial", 15))
vstupS.insert(0, "10")

# vytvoreni tlacitek
dalsiT = Button(root, text="Další", command=dalsiPlaneta, font=("Arial",15))
predchoziT = Button(root, text="Zrušit", command=predchoziPlaneta, font=("Arial",15))
nahledT = Button(root, text="Náhled", command=vykresleni, font=("Arial", 15))
spustitT = Button(root, text="Spustit", command=spustProgram, font=("Arial", 15))

# vlozeni na obrazovku
popisH.grid(row=0, column=0)
popisP.grid(row=1, column=0)
popisR.grid(row=2, column=0)
popisG.grid(row=3, column=0)
popisT.grid(row=4, column=0)
popisS.grid(row=5, column=0)

vstupH.grid(row=0, column=1)
vstupP.grid(row=1, column=1)
vstupR.grid(row=2, column=1)
vstupG.grid(row=3, column=1)
vstupT.grid(row=4, column=1)
vstupS.grid(row=5, column=1)

dalsiT.grid(row=6, column=0)
predchoziT.grid(row=6, column=1)
nahledT.grid(row=7, column=0)
spustitT.grid(row=7, column=1)

root.mainloop()

#ziskani pocatecni pozice a rychlosti jako list cisel
x0 = [float(eval(x)) for x in start_pos.split()]
v0 = [float(eval(x)) for x in start_velocity.split()]

#def srazka(t, y):
#    threshold = 1e-3

#    vzdalenosti = [[1] * n for _ in range(n)]
#    for i in range(n):
#        for j in range(n):
#            if i != j:  # Avoid computing distance for the same point
#                vzdalenosti[i][j] = (np.linalg.norm(
#                    [(y[3 * i] - y[3 * j]), (y[3 * i + 1] - y[3 * j + 1]), (y[3 * i + 2] - y[3 * j + 2])]))
#    flattened = [item for sublist in vzdalenosti for item in sublist]
#    condition = [dist < threshold for dist in flattened]
#    print(flattened)
#    print(condition)
#    return np.any(condition)
#
#srazka.terminal = True  # Stop integration when the event occurs

#zadefinovani soustavy rovnic pro pohyb n teles
def rovnice(t,y):
    rychlosti = [y[x] for x in range(3 * n, 6 * n)]
    sily = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                sily[i][j] = g*m[j] / ((np.linalg.norm(
                    [(y[3 * i] - y[3 * j]), (y[3 * i + 1] - y[3 * j + 1]), (y[3 * i + 2] - y[3 * j + 2])])) ** 3)
    zrycleni = [0] * 3 * n
    for i in range(n):
        mezisoucetx = 0
        mezisoucety = 0
        mezisoucetz = 0
        for j in range(n):
            mezisoucetx += (y[3 * j] - y[3 * i]) * sily[i][j]
        zrycleni[3 * i] = mezisoucetx
        for j in range(n):
            mezisoucety += (y[3 * j + 1] - y[3 * i + 1]) * sily[i][j]
        zrycleni[3 * i + 1] = mezisoucety
        for j in range(n):
            mezisoucetz += (y[3 * j + 2] - y[3 * i + 2]) * sily[i][j]
        zrycleni[3 * i + 2] = mezisoucetz

    dydt = rychlosti + zrycleni
    return dydt

#reseni pomoci funkce solve_ivp z knihovny scipy metoda Explicit Runge-Kutta řádu 8
poc_podm = x0+v0
sol = solve_ivp(rovnice, [0, timeinterval], poc_podm,dense_output=True, method='DOP853')
hladkost = 500

#print(sol.t_events[0])
#if sol.t_events[0] is not []:
#    t_event = sol.t_events[0][0]
#    t = np.linspace(0, t_event, round(hladkost*t_event/timeinterval))
#else:

#graficka interpretace vysledku
t = np.linspace(0, timeinterval, hladkost)
reseni = sol.sol(t)

#nejdrive projekce do jednotlivych smeru
fig, axs = plt.subplots(3, 1, figsize=(8, 6))

for i in range(n):
    axs[0].plot(reseni[3*i], reseni[3*i + 1], label ="Bod "+ str(i))
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')


for i in range(n):
    axs[1].plot(reseni[3*i], reseni[3*i + 2], label ="Bod "+str(i))
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')


for i in range(n):
    axs[2].plot(reseni[3*i + 1], reseni[3*i + 2], label ="Bod "+str(i))
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')

fig.suptitle("Projekce do jednotlivých směrů")

#a nyni 3D animace
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
num_frames = len(reseni[0])-1

rozmer = 1
for i in range(3):
    for j in range(len(reseni[0]-1)):
        if abs(reseni[i][j]) >= rozmer:
            rozmer = abs(reseni[i][j])

def update(frame):
    ax.cla()
    ax.set_xlim3d([-1*rozmer, rozmer])
    ax.set_ylim3d([-1*rozmer, rozmer])
    ax.set_zlim3d([-1*rozmer, rozmer])
    ax.set_xlabel('X-axis', fontweight='bold')
    ax.set_ylabel('Y-axis', fontweight='bold')
    ax.set_zlabel('Z-axis', fontweight='bold')
    ax.grid(visible=True, color='grey', linestyle='-.', linewidth=0.3, alpha=0.2)
    plt.title("Simulace n hmotných bodů")

    # vykresleni pozice pro jednotlive snimky
    for i in range(n):
        ax.scatter(reseni[3*i][frame], reseni[3*i +1][frame], reseni[3*i + 2][frame], c='r', marker='o')

animation = FuncAnimation(fig, update, frames=num_frames , interval=rychlost_simulace)
plt.show()