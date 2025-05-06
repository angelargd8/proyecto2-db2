from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId


# contar ordenes simples y entregadas / agregacion simple

def crear_orden(parent, ordenes, productos, combos):
    l1 = Label(parent, text="Ver orden:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    # l10 = Label(parent, text="ver orden:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    # l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id de la orden:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="ver orden", fg="#ffffff", font=("Arial", 12), bg="#78290f")#, 
                #    command=lambda: ver_detalles_orden(ordenes, e5.get()))
    btn4.place(x=570, y=90, height=30, width=160)

    l6 = Label(parent, text="orden:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=130)


def ver_orden(parent, ordenes):
    l1 = Label(parent, text="Ver orden:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    # l10 = Label(parent, text="ver orden:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    # l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id de la orden:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="ver orden", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                   command=lambda: ver_detalles_orden(ordenes, e5.get()))
    btn4.place(x=570, y=90, height=30, width=160)

    l6 = Label(parent, text="orden:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=130)

    text_items = Text(parent, width=60, height=20, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=10, y=170)


    def ver_detalles_orden(ordenes,  orden_id):
        if not orden_id:
            messagebox.showerror("Error", "Ingrese un id de orden")
        else: 
            orden = ordenes.find_one({"_id": ObjectId(orden_id)})
            if orden:
                try: 
                    # ver detalles expandidos de la orden con unwind y lookup /agracion cde documentos embebidos
                    pipeline = [
                        { "$match": { "_id": ObjectId(orden_id.strip()) } },
                        { "$unwind": "$pedido" },
                        { "$lookup": {
                            "from": "productos",
                            "localField": "pedido.producto",
                            "foreignField": "_id",
                            "as": "producto_detalle"
                        }},
                        { "$unwind": "$producto_detalle" },
                        { "$project": {
                            "_id": 0,
                            "producto": "$producto_detalle.nombreProducto",
                            "cantidad": "$pedido.cantidad",
                            "especificaciones": "$pedido.especificaciones"
                        }}
                    ]
                    detalles = list(ordenes.aggregate(pipeline))

                    if detalles:
                        text_items.delete("1.0", "end")
                        text_items.insert("end", "🍪 Detalles del pedido: 🍪\n")
                        text_items.insert("end", "-"*100 + "\n")

                        for d in detalles:
                            text_items.insert("end", f"Producto: {d['producto']}\n")
                            text_items.insert("end", f"Cantidad: {d['cantidad']}\n")
                            text_items.insert("end", f"Especificaciones: {d['especificaciones']}\n")
                            text_items.insert("end", "-"*100 + "\n")
                    else:
                        messagebox.showinfo("Info", "No se encontraron detalles de esa orden")
                except Exception as e:
                    messagebox.showerror("Error", f"error :\n{e}")


def cambiar_estado_orden(parent, ordenes):
    l1 = Label(parent, text="Cambiar el estado de la orden:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    l5 = Label(parent, text="Ingrese el id de la orden:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    btn4 = Button(parent, text="cambiar estado", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                    command=lambda: change_state(ordenes, e5.get()))
    btn4.place(x=570, y=90, height=30, width=160)

    l10 = Label(parent, text="ver cantidad de ordenes entregadas:",  fg="#6c584c", font=("Arial", 12))#  fg="#ffffff", font=("Arial", 12), bg="#a98467") 
    l10.place(x=10, y=150)

    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.config(state="readonly")
    e6.place(x=280, y=150)

    btn5 = Button(parent, text="ver cantidad", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                        command=lambda: ver_cantidad_ordenes(ordenes))
    btn5.place(x=570, y=150, height=30, width=160)

    def ver_cantidad_ordenes(ordenes):
        pipeline = [
            { "$match": { "estado": True } },
            { "$group": {
                "_id": None,
                "totalEntregadas": { "$sum": 1 }
            }}
        ]

        resultado = list(ordenes.aggregate(pipeline))

        if resultado:
            total = resultado[0]["totalEntregadas"]
            e6.config(state="normal")
            e6.delete(0, "end")
            e6.insert(0, str(total))
            e6.config(state="readonly")

        else:
            messagebox.showinfo("ordenes Entregadas", "No hay ordenes entregadas registradas.")

    def change_state(ordenes, orden_id):
        if not orden_id:
            messagebox.showerror("Error", "Ingrese un id de orden")
        else: 
            orden = ordenes.find_one({"_id": ObjectId(orden_id)})
            if orden:
                try: 
                    # cambiar el estado de la orden
                    nuevo_estado = not orden["estado"]
                    ordenes.update_one({"_id": ObjectId(orden_id)}, {"$set": {"estado": nuevo_estado}})

                    if nuevo_estado:
                        messagebox.showinfo("Info", "Estado de la orden actualizado a Orden entregada" )
                    else:
                        messagebox.showinfo("Info", "Estado de la orden actualizado a Orden no entregada" )


                    
                except Exception as e:
                    messagebox.showerror("Error", f"error :\n{e}")
            else:
                messagebox.showerror("Error", "Orden no encontrada")

