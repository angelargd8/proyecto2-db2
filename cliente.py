from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId

def del_cuenta():
    pass

def mod_cuenta():
    pass


def add_resenia_producto(parent,  productos):

    l1 = Label(parent, text="Editar menu:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: delete_combo(combos, e5.get()))
    
    btn4.place(x=570, y=120, height=30, width=160)

    l9 = Label(parent, text="Agregar nuevo combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=190)

    l6 = Label(parent, text="Ingrese el nombre del combo:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=220)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=220)

    l7 = Label(parent, text="Ingrese los productos del combo :", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=250)

    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=250)


    l8 = Label(parent, text="Precio:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=360)

    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=360)

    l10 = Label(parent, text="Url de la imagen del combo:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=390)

    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=390)

    btn5 = Button(parent, text="Agregar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: add_combo(combos, e6.get(), text_items.get("1.0", "end-1c"), e8.get(), e9.get()))
    btn5.place(x=570, y=220, height=30, width=160)


def add_resenia_combo(parent, combos):
    l1 = Label(parent, text="Editar menu:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: delete_combo(combos, e5.get()))
    
    btn4.place(x=570, y=120, height=30, width=160)

    l9 = Label(parent, text="Agregar nuevo combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=190)

    l6 = Label(parent, text="Ingrese el nombre del combo:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=220)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=220)

    l7 = Label(parent, text="Ingrese los productos del combo :", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=250)

    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=250)


    l8 = Label(parent, text="Precio:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=360)

    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=360)

    l10 = Label(parent, text="Url de la imagen del combo:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=390)

    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=390)

    btn5 = Button(parent, text="Agregar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: add_combo(combos, e6.get(), text_items.get("1.0", "end-1c"), e8.get(), e9.get()))
    btn5.place(x=570, y=220, height=30, width=160)

