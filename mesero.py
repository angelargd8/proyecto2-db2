from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# contar ordenes simples y entregadas / agregacion simple

def crear_orden(parent, ordenes, productos, combos):
    l1 = Label(parent, text="Crear orden:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)

    # l10 = Label(parent, text="ver orden:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    # l10.place(x=10, y=90)

    l5 = Label(parent, text="Ingrese el id del cliente: ", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=90)
    e5 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=280, y=90)

    

    l9 = Label(parent, text="Datos de la orden:", fg="#ffffff", font=("Arial", 12), bg="#a98467")
    l9.place(x=10, y=160)

    l6 = Label(parent, text="Fecha:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=190)
    e6 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=280, y=190)

    l8 = Label(parent, text="metodo de pago:", fg="#6c584c", font=("Arial", 12))
    l8.place(x=10, y=220)
    e8 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e8.place(x=280, y=220)

    l7 = Label(parent, text="Ingrese (ID producto, cantidad, especificaciones):", fg="#6c584c", font=("Arial", 12))
    l7.place(x=10, y=250)

    text_items = Text(parent, width=60, height=5, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=10, y=280)

    l9 = Label(parent, text="Id orden:", fg="#6c584c", font=("Arial", 12))
    l9.place(x=10, y=380)
    e9 = Entry(parent, width=30, font=("Arial", 12), bg="#f4f1e6")
    e9.place(x=280, y=380)
    e9.config(state="readonly")


    def guardar_orden():
        cliente_id = e5.get().strip()
        fecha = e6.get().strip()
        metodo = e8.get().strip()
        pedido_texto = text_items.get("1.0", "end-1c")

        if not cliente_id or not fecha or not metodo or not pedido_texto:
            messagebox.showerror("Error", "Complete todos los campos")
            return

        try:
            fecha_dt = datetime.strptime(fecha, "%d-%m-%Y")
            pedido = []
            total = 0.0

            for linea in pedido_texto.strip().splitlines():
                partes = linea.split(",")
                if len(partes) != 3:
                    raise ValueError("Cada línea debe tener: ID, cantidad, especificaciones")

                producto_id = ObjectId(partes[0].strip())
                cantidad = int(partes[1].strip())
                especificaciones = partes[2].strip()

                producto = productos.find_one({ "_id": producto_id })
                if not producto:
                    raise ValueError(f"Producto no encontrado: {producto_id}")

                precio_unitario = float(producto["precio"])
                total += cantidad * precio_unitario

                pedido.append({
                    "producto": producto_id,
                    "cantidad": cantidad,
                    "especificaciones": especificaciones
                })

            orden = {
                "_id": ObjectId(),
                "nombreCliente": ObjectId(cliente_id),
                "pedido": pedido,
                "precioTotal": round(total, 2),
                "estado": False,
                "fecha": fecha_dt,
                "metodoPago": metodo
            }

            ordenes.insert_one(orden)
            e9.config(state="normal")
            e9.delete(0, "end")
            e9.insert(0, str(orden["_id"]))
            e9.config(state="readonly")
            messagebox.showinfo("Orden creada", "La orden fue registrada con éxito")
            
            # messagebox.showinfo("Orden creada", f"ID de la orden: {orden['_id']}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

    btn4 = Button(parent, text="Crear orden", fg="#ffffff", font=("Arial", 12), bg="#78290f",
                  command=guardar_orden)
    btn4.place(x=570, y=90, height=70, width=160)



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

    l10 = Label(parent, text="cambiar varias ordenes:",  fg="#ffffff", font=("Arial", 12), bg="#a98467") 
    l10.place(x=10, y=190)

    l6 = Label(parent, text="id ordenes:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=220)

    text_items = Text(parent, width=60, height=10, font=("Arial", 12), bg="#f4f1e6")
    text_items.place(x=10, y=250)

    btn6 = Button(parent, text="cambiar estado", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                    command=lambda: cambiar_estados(ordenes, text_items.get("1.0", "end-1c")))
    btn6.place(x=570, y=220, height=30, width=160)

    def cambiar_estados(ordenes, items):
        texto = items.strip()
        if not texto:
            messagebox.showerror("Error", "Ingrese al menos un id de orden")
            return
        try:
            #convertir en ObjectId
            ids = [
                ObjectId(line.strip())
                for line in texto.splitlines()
                if ObjectId.is_valid(line.strip())
            ]

            if not ids:
                messagebox.showerror("Error", "No se ingresaron IDs vslidos")
                return

            #buscar ordenes delos ids
            ordenes_encontradas = list(ordenes.find({"_id": {"$in": ids}}))

            if not ordenes_encontradas:
                messagebox.showerror("Error", "No se encontraron órdenes con los IDs dados")
                return

            #determinar el estado actual y cambiarlo por el contrario
            estado_actual = ordenes_encontradas[0]["estado"]
            nuevo_estado = not estado_actual

            #actualizar todas las ordenes encontradas
            resultado = ordenes.update_many(
                {"_id": {"$in": ids}},
                {"$set": {"estado": nuevo_estado}}
            )

            messagebox.showinfo("Actualizacion exitosa", f"Se actualizaron {resultado.modified_count} órdenes a estado {'entregada' if nuevo_estado else 'no entregada'}.")

        except Exception as e:
            messagebox.showerror("Error", f"eror:\n{e}")
        

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

