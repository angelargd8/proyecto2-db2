from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def mod_restaurante(parent):

    l1 = Label(parent, text="Agregar/eliminar restaurante:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=10)

    l10 = Label(parent, text="Eliminar restaurantes:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=70)

    l5 = Label(parent, text="Ingrese el id del restaurante:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=100)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=100)

    l9 = Label(parent, text="Agregar nueva sucursal:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=190)

    l6 = Label(parent, text="Ingrese nuevo nombre de la sucursal:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=220)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=220)

    l7 = Label(parent, text="La cantidad de mesas:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=250)
    e7 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e7.place(x=280, y=250)

    l8 = Label(parent, text="Las coordenadas de la sucursal (x,y):", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=280)

    e8 = Entry(parent, width=5, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=280)
    e9 = Entry(parent, width=5, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=330, y=280)



#funcioens del boton de a;adir o borrar
def add_restaurante(parent):
    pass

def delete_restaurante(parent):
    pass


def mod_producto(parent):
    pass
def add_producto(parent):
    pass

def delete_producto(parent):
    pass


def mod_menu(parent):
    pass

def delete_usuario(parent):
    l4 = Label(parent, text="Ingrese el id del usuario a borrar:", fg="#6c584c", font=("Arial", 12))
    l4.place(x=10, y=20)
    e4 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e4.place(x=190, y=20)
