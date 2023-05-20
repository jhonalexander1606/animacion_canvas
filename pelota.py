from tkinter import *
import tkinter as tk
from random import randint

# Variables Globales
BASE = 600
ALTURA = 310

ventana_principal = tk.Tk()
ventana_principal.title("GRÁFICAS 2D - CANCHA DE FÚTBOL")
ventana_principal.resizable(False, False)
ventana_principal.geometry("640x500")   
ventana_principal.config(bg = "black")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=620, height=480)
frame_graficacion.place(x=10, y=10)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)
c.config(bg="yellow green")


imagen = tk.PhotoImage(file="img/fondo_cancha (3).png")

c.create_image(0,0, ancho="nw" , image= imagen)


# # Líneas
# linea1 = c.create_line(10,10, BASE-10, 10, fill="white", width=3)
# linea2 = c.create_line(BASE-10,10, BASE-10, ALTURA-10, fill="white", width=3)
# linea3 = c.create_line(BASE-10,ALTURA-10, 10, ALTURA-10, fill="white", width=3)
# linea4 = c.create_line(10,ALTURA-10, 10,10, fill="white", width=3)


# #circulo central
# elipse1 = c.create_oval((BASE/2)-45.75, (ALTURA/2)-45.75, (BASE/2)+45.15, (ALTURA/2)+45.75, fill ="yellow green", outline="white", width=3)


# # Línea intermedia
# linea5 = c.create_line(BASE/2,10, BASE/2, ALTURA-10, fill="white", width=3)
# #circulo central
# elipse1 = c.create_oval((BASE/2)-5, (ALTURA/2)-5, (BASE/2)+5, (ALTURA/2)+5, fill ="white", outline="white", width=1)

# # BOMBA EXTERNA
# linea6 = c.create_line(BASE/5,ALTURA*2/9, BASE/5,ALTURA*7/9, fill="white", width=3)
# linea7 = c.create_line(10,ALTURA*2/9, BASE/5,ALTURA*2/9, fill="white", width=3)
# linea8 = c.create_line(10,ALTURA*7/9, BASE/5,ALTURA*7/9, fill="white", width=3)

# linea9 = c.create_line(BASE-BASE/5,ALTURA*2/9, BASE-BASE/5,ALTURA*7/9, fill="white", width=3)
# linea10 = c.create_line(BASE-10,ALTURA*2/9, BASE-BASE/5,ALTURA*2/9, fill="white", width=3)
# linea11 = c.create_line(BASE-10,ALTURA*7/9, BASE-BASE/5,ALTURA*7/9, fill="white", width=3)

# # BOMBA INTERNA

# linea6 = c.create_line(BASE/10,ALTURA*4/11, BASE/10,ALTURA*7/11, fill="white", width=3)
# linea7 = c.create_line(10,ALTURA*4/11, BASE/10,ALTURA*4/11, fill="white", width=3)
# linea8 = c.create_line(10,ALTURA*7/11, BASE/10,ALTURA*7/11, fill="white", width=3)

# linea6 = c.create_line(BASE-BASE/10,ALTURA*4/11, BASE-BASE/10,ALTURA*7/11, fill="white", width=3)
# linea7 = c.create_line(BASE-10,ALTURA*4/11, BASE-BASE/10,ALTURA*4/11, fill="white", width=3)
# linea8 = c.create_line(BASE-10,ALTURA*7/11, BASE-BASE/10,ALTURA*7/11, fill="white", width=3)

# # ESQUINAS
# esquina1 = c.create_arc(10-10, 10-10, 10+10, 10+10, start=270, extent=90, fill="yellow green",outline="white", width=3)
# esquina2 = c.create_arc(10-10, (ALTURA-10)-10, 10+10, (ALTURA-10)+10, start=0, extent=90, fill="yellow green",outline="white", width=3)
# esquina3 = c.create_arc(BASE-10-10, 10-10, BASE-10+10, 10+10, start=180, extent=90, fill="yellow green",outline="white", width=3)
# esquina4 = c.create_arc(BASE-10-10, ALTURA-10-10, BASE-10+10, ALTURA-10+10, start=90, extent=90, fill="yellow green",outline="white", width=3)

radio=8
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = randint(radio, BASE)
centro_y = randint(radio, ALTURA)

def mueve_pelota():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(pelota)
    if x0 < 0 or x1 > BASE: desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: desplazamiento_y = -desplazamiento_y
    c.move(pelota, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mueve_pelota)

pelota = c.create_oval(centro_x-radio, centro_y-radio, centro_x+radio, centro_y+radio, fill="white", outline="black")


boton = Button(frame_graficacion)
boton.config(bg="green", width=30, height=5, text="Mover Pelota", command=mueve_pelota)
boton.place(x=BASE/3, y=ALTURA+ALTURA/6)

ventana_principal.mainloop()