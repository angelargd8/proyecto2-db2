from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId

def mod_restaurante(parent, restaurantes):

    l1 = Label(parent, text="Agregar/eliminar restaurante:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar restaurantes:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del restaurante:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar restaurante", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: delete_restaurante(restaurantes, e5.get()))
    btn4.place(x=570, y=120, height=30, width=160)

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

    l8 = Label(parent, text="Las coordenadas de la sucursal (long,lat):", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=280)

    e8 = Entry(parent, width=5, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=280)
    e9 = Entry(parent, width=5, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=330, y=280)

    btn5 = Button(parent, text="Agregar restaurante", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: add_restaurante(restaurantes, e6.get(), int(e7.get()), float(e8.get()), float(e9.get()) ))
    btn5.place(x=570, y=220, height=30, width=160)


#funcioens del boton de a;adir o borrar
def add_restaurante(restaurantes, sucursal, mesas, long, lat):
    #validar que hayan datos
    if not sucursal or not mesas or not long or not lat:
        messagebox.showerror("Error", "Por favor complete todos los campos")
        return
    else: 
        try: 
            if not (-180 <= long <= 180 and -90 <= lat <= 90):
                messagebox.showerror("Error", "Coordenadas fuera de rango")
            else: 
                #validar que la sucursal no exista
                sucursal = sucursal.strip()
                nombre = restaurantes.find_one({"sucursal": sucursal})

                if nombre:
                    messagebox.showerror("Error", "La sucursal ya existe")
                else:
                    nuevo_restaurante = {
                        "_id": ObjectId(),
                        "sucursal": sucursal,
                        "numeroMesas": mesas,
                        "ubicacion": {
                            "type": "Point",
                            "coordinates": [long, lat]
                        }
                    }
                    restaurantes.insert_one(nuevo_restaurante)
                    messagebox.showinfo("Agregar restaurante", "Restaurante agregado con éxito")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores validos")
            return

def delete_restaurante(restaurantes, id_restaurante):
    id_restaurante = ObjectId(id_restaurante.strip())
    restaurente = restaurantes.find_one({"_id": id_restaurante})
    if restaurente:
        restaurantes.delete_one({"_id": id_restaurante})
        messagebox.showinfo("Eliminar restaurante", "Restaurante eliminado con éxito")
    else:
        messagebox.showerror("Error", "Restaurante no encontrado")


def mod_producto(parent):
    l1 = Label(parent, text="Agregar/eliminar producto:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar producto:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del producto:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn4.place(x=570, y=120, height=30, width=160)

    l9 = Label(parent, text="Agregar nuevo producto:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=190)

    l6 = Label(parent, text="Ingrese nuevo nombre del producto:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=220)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=220)

    l7 = Label(parent, text="Descripcion:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=250)
    e7 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e7.place(x=280, y=250)

    l8 = Label(parent, text="Precio:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=280)

    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=280)

    l10 = Label(parent, text="Url de la imagen:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=310)

    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=310)

    btn5 = Button(parent, text="Agregar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn5.place(x=570, y=220, height=30, width=160)


def add_producto(parent):
    pass

def delete_producto(parent):
    pass


def mod_menu(parent):
    l1 = Label(parent, text="Editar menu:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f")
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

    btn5 = Button(parent, text="Agregar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn5.place(x=570, y=220, height=30, width=160)

def add_combo(parent):
    pass

def delete_combo(parent):
    pass


def mod_combos(parent):
    l1 = Label(parent, text="Editar Combo:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="Buscar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn4.place(x=570, y=90, height=30, width=160)

    l9 = Label(parent, text="Datos del combo:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=160)

    l6 = Label(parent, text="Ingrese el nombre del combo:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=190)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=190)

    l7 = Label(parent, text="Ingrese los productos del combo:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=220)

    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=220)


    l8 = Label(parent, text="Precio:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=330)

    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=330)

    l10 = Label(parent, text="Url de la imagen del combo:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=330)

    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=330)

    btn5 = Button(parent, text="Editar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn5.place(x=570, y=190, height=30, width=160)



def delete_usuario(parent):
    l1 = Label(parent, text="Borrar usuario:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l5 = Label(parent, text="Ingrese el id del usuario:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="Borrar usuario", fg="#ffffff", font=("Arial", 12), bg="#78290f")
    btn4.place(x=570, y=90, height=30, width=160)
