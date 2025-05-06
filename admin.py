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

    l8 = Label(parent, text="Las coordenadas de la sucursal:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=280)

    l8_1 = Label(parent, text="(longitud , latitude)", fg="#6c584c", font=("Arial", 12))
    l8_1.place(x=10, y=300)

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


def mod_producto(parent, productos, combos):
    l1 = Label(parent, text="Agregar/eliminar producto:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar producto:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del producto:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=120)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=120)

    btn4 = Button(parent, text="Borrar producto", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: delete_producto(productos, combos, e5.get()))
    btn4.place(x=570, y=120, height=30, width=160)

    l9 = Label(parent, text="Agregar nuevo producto:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=190)

    l10 = Label(parent, text="Ingrese el tipo de producto:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=220)
    e10 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e10.place(x=280, y=220)

    l6 = Label(parent, text="Ingrese nuevo nombre del producto:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=250)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=250)

    l7 = Label(parent, text="Descripcion:", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=280)
    e7 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e7.place(x=280, y=280)

    l8 = Label(parent, text="Precio:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=310)

    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=310)

    l10 = Label(parent, text="Url de la imagen:", fg="#6c584c", font=("Arial", 12))
    l10.place(x=10, y=340)

    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=340)

    btn5 = Button(parent, text="Agregar Producto", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: add_producto(productos, e10.get(), e6.get(), e7.get(), e8.get(), e9.get()))
    btn5.place(x=570, y=220, height=30, width=160)
    btn6 = Button(parent, text="Agregar Otro", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: agregar_cola(productos, e10.get(), e6.get(), e7.get(), e8.get(), e9.get()) )
    btn6.place(x=570, y=260, height=30, width=160)
    btn7 = Button(parent, text="Agregar Todos", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: add_variosP(productos) )
    btn7.place(x=570, y=310, height=30, width=160)

global lista_productos
lista_productos = []
# esta funcion es para agregar a varios productos
def agregar_cola(productos, tipoProducto, nombre, descripcion, precio, url):
    global lista_productos
    if not nombre or not descripcion or not precio or not url or not tipoProducto:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
    else:
        precio = float(precio)
        nuevo_producto = {
                    "_id": ObjectId(),
                    "tipoProducto": tipoProducto,
                    "nombreProducto": nombre,
                    "descripcion": descripcion,
                    "precio": precio,
                    "imagenProducto": url
                }
        lista_productos.append(nuevo_producto)
        messagebox.showinfo("!", "Agregado a la cola")

def add_variosP(productos):
    if len(lista_productos) > 0:
        r = productos.insert_many(lista_productos)
        print("Insertados:", r)
        messagebox.showinfo("!", "Productos agregados")
    else:
        messagebox.showerror("Error", "No hay productos para agregar")

def add_producto(productos, tipoProducto, nombre, descripcion, precio, url):
    
    if not nombre or not descripcion or not precio or not url or not tipoProducto:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
    else: 
        nombre_exist = productos.find_one({"nombreProducto": nombre})
        if nombre_exist:
            messagebox.showerror("Error", "El producto ya existe")
        else:
            try:
                precio = float(precio)
                nuevo_producto = {
                    "_id": ObjectId(),
                    "tipoProducto": tipoProducto,
                    "nombreProducto": nombre,
                    "descripcion": descripcion,
                    "precio": precio,
                    "imagenProducto": url
                }
                productos.insert_one(nuevo_producto)
                messagebox.showinfo("Agregar producto", "Producto agregado con éxito")
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número")

def delete_producto(productos, combos, id_producto):
    id_producto = ObjectId(id_producto.strip())
    producto = productos.find_one({"_id": id_producto})
    # print(producto)
    if producto:

        # Verificar si el producto esta dentro de algun combo 
        #el pipeline cumple con la agregacion de manejo de arrays con in y complejas por el match
        pipeline = [
            {
                "$match": {
                    "$expr": {
                        "$in": [id_producto, "$items"]
                    }
                }
            },
            { "$limit": 1 }  #porque solo necesitamos saber si existe
        ]

        usado = list(combos.aggregate(pipeline))

        if usado:
            messagebox.showerror("Error", "El producto no se puede eliminar porque está dentro de un combo")
        else:
            productos.delete_one({"_id": id_producto})
            messagebox.showinfo("Eliminar producto", "Producto eliminado con éxito")

    else:
        messagebox.showerror("Error", "Producto no encontrado")
    


def mod_menu(parent, combos):
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

def add_combo(combos, nombreCombo, items, precio, imagenCombo):
    #validar que hayan datos
    if not nombreCombo or not items or not precio or not imagenCombo:
        messagebox.showerror("Error", "Por favor complete todos los campos")
        return
    else: 
        try: 
            combo = combos.find_one({"nombreCombo": nombreCombo})
            if combo:
                messagebox.showerror("Error", "El combo ya existe")
            else:
                #print(items)
                # convertir texto multilinea en lista de ObjectId
                ids = [
                    ObjectId(line.strip())
                    for line in items.strip().splitlines()
                    if ObjectId.is_valid(line.strip())
                ]

                if not ids:
                    messagebox.showerror("Error", "Debe ingresar al menos un ID válido de producto")

                precio = float(precio)
                nuevo_combo = {
                    "_id": ObjectId(),
                    "nombreCombo": nombreCombo,
                    "items": ids,
                    "precio": precio,
                    "imagenCombo": imagenCombo
                }

                combos.insert_one(nuevo_combo)
                messagebox.showinfo("Agregar combo", "Combo agregado con éxito")

        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido")
        except SyntaxError:
            messagebox.showerror("Error", "Formato de productos incorrecto")


def delete_combo(combos, id_combo):
    id_combo = ObjectId(id_combo.strip())
    combo = combos.find_one({"_id": id_combo})
    if combo:
        combos.delete_one({"_id": id_combo})
        messagebox.showinfo("Eliminar combo", "Combo eliminado con éxito")
    else:
        messagebox.showerror("Error", "Combo no encontrado")
    


def mod_combos(parent, combos):
    l1 = Label(parent, text="Editar y buscar Combo:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l5 = Label(parent, text="Ingrese el id del combo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="Buscar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: find_combo(combos, e5.get()))
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

    btn5 = Button(parent, text="Editar combo", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: update_combo(combos, e5.get(), e6.get(), text_items.get("1.0", "end-1c"), e8.get(), e9.get()))
    btn5.place(x=570, y=190, height=30, width=160)


    def find_combo(combos, id_combo):
        if not id_combo:
            messagebox.showerror("Error", "Por favor ingrese un ID de combo")
        else: 
            id_combo = ObjectId(id_combo.strip())
            combo = combos.find_one({"_id": id_combo})
            if combo:
                e6.delete(0, "end")
                e6.insert(0, combo["nombreCombo"])
                text_items.delete("1.0", "end")
                text_items.insert("1.0", combo["items"])
                e8.delete(0, "end")
                e8.insert(0, combo["precio"])
                e9.delete(0, "end")
                e9.insert(0, combo["imagenCombo"])
            else:
                messagebox.showerror("Error", "Combo no encontrado")
                

def update_combo(combos, id_combo, nombreCombo, items, precio, imagenCombo):
    if not id_combo or not nombreCombo or not items or not precio or not imagenCombo:
        messagebox.showerror("Error", "Por favor complete todos los campos")
    else:
        combo = combos.find_one({"_id": ObjectId(id_combo.strip())})
        if combo:
            try:
                # Convertir texto multilinea en lista de ObjectId
                ids = [
                    ObjectId(line.strip())
                    for line in items.strip().splitlines()
                    if ObjectId.is_valid(line.strip())
                ]

                if not ids:
                    messagebox.showerror("Error", "Debe ingresar al menos un ID válido de producto")
                    return

                precio = float(precio)
                nuevo_combo = {
                    "_id": ObjectId(id_combo.strip()),
                    "nombreCombo": nombreCombo,
                    "items": ids,
                    "precio": precio,
                    "imagenCombo": imagenCombo
                }

                combos.update_one({"_id": ObjectId(id_combo.strip())}, {"$set": nuevo_combo})
                messagebox.showinfo("Editar combo", "Combo editado con éxito")

            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido")
            except SyntaxError:
                messagebox.showerror("Error", "Formato de productos incorrecto")


def delete_usuario(parent, usuarios, ordenes):
    l1 = Label(parent, text="Borrar usuario:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l10 = Label(parent, text="Eliminar:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese los ids de los usuarios:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    text_items = Text(parent, width=30, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=280, y=90)

    btn4 = Button(parent, text="Borrar usuario(s)", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=lambda: del_usuarios(usuarios, ordenes, text_items.get("1.0", "end-1c")))
    btn4.place(x=570, y=90, height=30, width=160)


def del_usuarios(usuarios, ordenes, items):
    #poner agregacioens de ver si tiene ordenes asociadas antes de eliminar
    if not items:
        messagebox.showerror("Error", "Por favor ingrese al menos un ID de usuario")
    else:
        # convertir texto multilinea en lista de ObjectId
        ids = [
            ObjectId(line.strip())
            for line in items.strip().splitlines()
            if ObjectId.is_valid(line.strip())
        ]

        eliminables = []

        for id_usuario in ids:
            # Verificar si el usuario tiene ordenes asociadas
            usuario = usuarios.find_one({"_id": id_usuario})
            if not usuario: 
                messagebox.showwarning("Warning", f"el usuario con ID {id_usuario} no encontrado")
                continue
            # verificar ordenes asociadas con argeragacioens
            pipeline = [
                { "$match": { "nombreCliente": id_usuario } },
                { "$limit": 1 }
            ]
            tiene_ordenes = list(ordenes.aggregate(pipeline))

            if tiene_ordenes:
                messagebox.showwarning("Aviso", f"Usuario {usuario['nombre']} no se puede eliminar: tiene órdenes asociadas")
            else:
                eliminables.append(id_usuario)

        if eliminables:
            result = usuarios.delete_many({ "_id": { "$in": eliminables } })
            messagebox.showinfo("Resultado", f"{result.deleted_count} usuario(s) eliminados con éxito")
        else:
            messagebox.showinfo("Resultado", "No se eliminaron usuarios")