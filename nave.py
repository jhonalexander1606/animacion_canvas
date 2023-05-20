#---------------------------------
# Desktop app -Estudiante 
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *   
import random
import tkinter as tk
from tkinter import messagebox

#variables globales
BASE=660
ALTURA=460

#def variables

def mover_objeto(x, y):
    reiniciar_circulos()
    xd,yd = c.coords(objeto)
    if xd < 0:
        x += 660
    elif xd > 660:
        x -= 660
    elif yd < 0:
        y += 460
    elif yd > 460:
        y -= 460
    c.move(objeto, x, y)

def reiniciar_circulos():
    c.delete("circulo") 
    for i in range(200):
        x_estrella = random.randint(0, BASE - 20)
        y_estrella = random.randint(0, ALTURA - 20)
        color = "#"
        for caracter in range(6):   
            color = color + random.choice("0123456789ABCDF")
            tamaño = random.randint(0,20)
        c.create_oval(x_estrella,y_estrella, x_estrella+tamaño, y_estrella+tamaño, fill = color, tags="circulo")

def mover_arriba(event=None):
    mover_objeto(0, -10)
    
def mover_abajo(event=None):
    mover_objeto(0, 10) 

def mover_izquierda(event=None):
    mover_objeto(-10, 0)  

def mover_derecha(event=None):
    mover_objeto(10, 0) 


def salir():
    messagebox.showinfo("Nave", "la app se cerrara")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------
# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()
# titulo de la ventana
ventana_principal.title("Graficas 2D - nave")
# tamaño de la ventana
ventana_principal.geometry("700x650")
# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="wheat3")

#--------------------------------
# frame graficacion
#--------------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=680, height=480)
frame_graficacion.place(x=10, y=10)

#canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.configure(bg="black")
c.place(x=10, y=10)

#objeto o balon 
image = PhotoImage(file="img/nave.png",)
objeto = c.create_image(100,200, image=image)

game = PhotoImage(file="img/game.png")

#frame de controles
frame_controles = Label(ventana_principal, image=game)
frame_controles.configure(bg="green2", width=680, height=140)
frame_controles.place(x=10, y = 500)


#boton arriva

up = PhotoImage(file="img/up.png")

bt_arriba = Button(frame_controles, image=up, command=mover_arriba)
bt_arriba.place(x=158, y=30)

#boton derecha

der = PhotoImage(file="img/der.png")

bt_arriba = Button(frame_controles, image=der, command=mover_derecha)
bt_arriba.place(x=190,y=60)

#boton izquierda

izq = PhotoImage(file="img/izq.png")

bt_arriba = Button(frame_controles, image=izq, command=mover_izquierda)
bt_arriba.place(x=130,y=60)

#boton abajo

down = PhotoImage(file="img/down.png")

bt_abajo = Button(frame_controles, image=down, command=mover_abajo)

bt_abajo.place(x=157,y=89)

# boton salir

over = PhotoImage(file ="img/over.png")

bt_salir= Button(frame_controles, image = over , comman = salir)
bt_salir.config(bg="navy")
bt_salir.place(x=300,y=15)


#teclas
ventana_principal.bind("<Up>", mover_arriba)
ventana_principal.bind("<Down>", mover_abajo)
ventana_principal.bind("<Left>", mover_izquierda)
ventana_principal.bind("<Right>", mover_derecha)



ventana_principal.mainloop()