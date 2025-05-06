import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId

def del_cuenta(parent, usuarios, correo):
    l1 = Label(parent, text="Eliminar cuenta:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    bt = Button(parent, text="Eliminar", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: del_cuenta(correo, usuarios))
    bt.place(x=280, y=80, height=30, width=160)

def del_correo(correo, usuarios):
    correo_usuario = "usuario@ejemplo.com"
    resultado = usuarios.delete_one({ "correo": correo_usuario })
    if resultado.deleted_count == 1:
        messagebox.showinfo("!", "Borrado exitosamente")
    else:
        messagebox.showerror("!", "Error")


def add_resenia_producto(parent, resenia, productos, correo, usuarios):

    l1 = Label(parent, text="Agregar reseña:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    

    l5 = Label(parent, text="Ingrese el id del producto:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)


    l6 = Label(parent, text="Ingrese calificacion:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=150)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=150)

    l7 = Label(parent, text="Ingrese comentario:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=180)

    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=180)


    

    bt = Button(parent, text="Agregar", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: resenia_fun(resenia,correo, e5.get(), e6.get(), text_items.get("1.0", "end-1c"), usuarios))
    bt.place(x=280, y=300, height=30, width=160)



def resenia_fun(resenias, correo, id, calif, coment, usuarios):
    usuario = usuarios.find_one({ "email": correo })
    id_user = usuario["_id"]

    nueva_resena = {
    "producto": ObjectId(id),  
    "calificacion": calif,
    "comentario": coment,
    "nombreUsuario": ObjectId(id_user),
    "fecha": time.time()
        }
    r = resenias.insert_one(nueva_resena)
    print(r)
    messagebox.showinfo("!", "Ingresada correctamente")


def add_resenia_combo(parent, resenia, combos, correo, usuarios):
    l1 = Label(parent, text="Agregar reseña:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)


    l6 = Label(parent, text="Ingrese calificacion:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=150)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=150)

    l7 = Label(parent, text="Ingrese comentario:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=180)

    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=180)


    

    bt = Button(parent, text="Agregar", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: resenia_fun(resenia,correo, e5.get(), e6.get(), text_items.get("1.0", "end-1c"), usuarios))
    bt.place(x=280, y=300, height=30, width=160)



