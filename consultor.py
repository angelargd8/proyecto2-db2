from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient
from bson import ObjectId



# consultas 
def consultas(parent, ordenes, resenias, productos):
    l1 = Label(parent, text="Consultas:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)


    l10 = Label(parent, text="Mostrar calificaciones mayores a:", fg="#ffffff", 
                font=("Arial", 12), bg="#a98467")
    l10.place(x=10, y=90)
    e = Entry(parent, width=10)
    e.place(x=280, y = 90)
    btn1 = Button(parent, text="Generar", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
                  command=lambda: calificacion_mayor_a(resenias, e.get()  ))
    btn1.place(x=100, y=120, height=30, width=160)



    l2 = Label(parent, text="Calificaciones y Comentarios de:", fg="#ffffff", 
                font=("Arial", 12), bg="#a98467")
    l2.place(x=10, y=180)
    e2 = Entry(parent, width=10)
    e2.place(x=280, y = 180, width=100)
    btn2 = Button(parent, text="Generar", fg="#ffffff", font=("Arial", 12), bg="#78290f",  command=lambda: proyeccion(resenias, e2.get()) )
    btn2.place(x=100, y=210, height=30, width=160)

    l3 = Label(parent, text="Mejores 5 calificaciones de:", fg="#ffffff", 
                font=("Arial", 12), bg="#a98467")
    l3.place(x=10, y=270)
    e3 = Entry(parent, width=10)
    e3.place(x=280, y = 270, width=200)
    btn3 = Button(parent, text="Generar", fg="#ffffff", font=("Arial", 12), bg="#78290f",  command=lambda: limit(resenias, e3.get(), productos) )
    btn3.place(x=100, y=300, height=30, width=160)



    l4 = Label(parent, text="calicacion del producto (skip 1):", fg="#ffffff", 
                font=("Arial", 12), bg="#a98467")
    l4.place(x=10, y=360)
    e4 = Entry(parent, width=10)
    e4.place(x=280, y = 360, width=200)
    btn4 = Button(parent, text="Generar", fg="#ffffff", font=("Arial", 12), bg="#78290f",  command=lambda: skip(resenias, e4.get(), productos) )
    btn4.place(x=100, y=390, height=30, width=160)




def calificacion_mayor_a(resenias, numero ): # agregate 
    numero = float(numero)
    r = resenias.aggregate([
    { "$match": { "calificacion": { "$gte": numero } } },
    { "$sort": { "calificacion": 1 } },
    { "$lookup": {
        "from": "productos",
        "localField": "producto",
        "foreignField": "_id",
        "as": "productoInfo"
    }},
    { "$unwind": "$productoInfo" },
    { "$project": {
        "_id": 0,
        "nombreProducto": "$productoInfo.nombreProducto",
        "calificacion": 1,
        "comentario": 1
    }}
            ])
    ventana_resultados = Toplevel()
    ventana_resultados.title("Resultados de Reseñas")

    canvas = Canvas(ventana_resultados)
    scrollbar = Scrollbar(ventana_resultados, orient="vertical", command=canvas.yview)
    frame_resultados = Frame(canvas)

    frame_resultados.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mostrar resultados
    for doc in r:
        texto = (
            f"Producto: {doc.get('nombreProducto')}\n"
            f"Calificación: {doc.get('calificacion')}\n"
            f"Comentario: {doc.get('comentario')[:50]}"
        )
        Label(frame_resultados, text=texto, wraplength=500, justify="left").pack(
            anchor="w", padx=10, pady=5
        )


def proyeccion(resenias, id): # proyeccion 
    proyeccion = {"comentario": 1, "_id": 0 }
    resultados = resenias.find({ "nombreUsuario": ObjectId(id) }, proyeccion)


    ventana_resultados = Toplevel()
    ventana_resultados.title("Resultados de Reseñas")

    canvas = Canvas(ventana_resultados)
    scrollbar = Scrollbar(ventana_resultados, orient="vertical", command=canvas.yview)
    frame_resultados = Frame(canvas)

    frame_resultados.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

   # Mostrar resultados
    for doc in resultados:
        texto = f"Comentario: {doc.get('comentario')}"
        Label(frame_resultados, text=texto, wraplength=500, justify="left").pack(
            anchor="w", padx=10, pady=5
        )


def limit(resenias, producto, productos): # 
    nombre = productos.find_one({ "nombreProducto": producto })
    if nombre:
        producto_id = nombre["_id"]
        
        resultados = resenias.find(
            { "producto": producto_id },
            { "calificacion": 1, "comentario": 1, "_id": 0 }
        ).sort("calificacion", -1).limit(5)

        ventana_resultados = Toplevel()
        ventana_resultados.title("Resultados de Reseñas")

        canvas = Canvas(ventana_resultados)
        scrollbar = Scrollbar(ventana_resultados, orient="vertical", command=canvas.yview)
        frame_resultados = Frame(canvas)

        frame_resultados.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for doc in resultados:
            texto = (
                f"Producto: {producto}\n"  
                f"Calificación: {doc.get('calificacion')}\n"  
                f"Comentario: {doc.get('comentario')[:100]}"  
            )
            
            Label(frame_resultados, text=texto, wraplength=500, justify="left").pack(
                anchor="w", padx=10, pady=5
            )

    else:
        messagebox.showinfo("!", "Producto no encontrado")


def skip(resenias, producto, productos): 
    nombre = productos.find_one({ "nombreProducto": producto })
    if nombre:
        producto_id = nombre["_id"]
        total_reseñas = resenias.count_documents({ "producto": producto_id })

        
        resultados = resenias.find(
            { "producto": producto_id },
            { "calificacion": 1, "comentario": 1, "_id": 0 }
        ).sort("fecha", -1).skip(1)  
        ventana_resultados = Toplevel()
        ventana_resultados.title("Resultados de Reseñas")

        canvas = Canvas(ventana_resultados)
        scrollbar = Scrollbar(ventana_resultados, orient="vertical", command=canvas.yview)
        frame_resultados = Frame(canvas)

        frame_resultados.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")  
        # Mostrar las calificaciones
        for doc in resultados:
            calificacion = doc.get("calificacion")
            comentario = doc.get("comentario")

            texto = (
                f"Calificación: {calificacion}\n"
                f"Comentario: {comentario[:100]}"  # Muestra los primeros 100 caracteres
            )

            # Mostrar el resultado en una etiqueta
            Label(frame_resultados, text=texto, wraplength=500, justify="left").pack(
                anchor="w", padx=10, pady=5
            )
