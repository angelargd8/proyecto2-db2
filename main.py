from pymongo import MongoClient
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from login import login, CreateAccount
from admin import *
from cliente import *
from mesero import *
from consultor import *

# uri = "mongodb+srv://angel:angel123@cluster0.krfnzqa.mongodb.net"
uri = "mongodb+srv://agu22243:cluster0123@cluster0.pq41dbr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
# db = client["restaurante"]
db = client["test"]
print("Conectado a la base de datos")

# print("Base de datos: ", db.name)
# print("Colecciones: ", db.list_collection_names())
restaurantes = db["restaurantes"]
combos = db["combos"]
productos = db["productos"]
resenias = db["resenias"]
ordenes = db["ordenes"]
usuarios = db["usuarios"]
#indices
#usuarios
usuarios.create_index([("email", 1)], unique=True)
usuarios.create_index([("tipoCuenta", 1), ("nombre", 1)])  #indice compuesto
usuarios.create_index([("historialPedidos", 1)])  # multikey 
#restaurantes
restaurantes.create_index([("ubicacion", "2dsphere")]) # geoespacial
restaurantes.create_index([("sucursal", "text")])
#ordenes
ordenes.create_index([("nombreCliente", 1), ("estado", 1)])
ordenes.create_index([("pedido.producto", 1)])  # multikey
#resenias
resenias.create_index([("producto", 1), ("nombreUsuario", 1)])
resenias.create_index([("comentario", "text")])
#productos
productos.create_index([("nombreProducto", "text"), ("descripcion", "text")])
productos.create_index([("tipoProducto", 1), ("precio", 1)])
#combos
combos.create_index([("items", 1)])  # multikey
combos.create_index([("nombreCombo", "text")])


global tipoCuenta
global tabs
global lrol2
tabs =[]


def CerrarSesion():
    global tabs
    global lrol2
    lrol2.config(text="")
    for tab_id in tab.tabs(): 
        tab.forget(tab_id)
    
    tabs.clear()
    landingPage()

def landingPage(tipoCuenta=None):
    tabLanging = ttk.Frame(tab)
    tab.add(tabLanging, text="Crear cuenta")
    tabs.append(tabLanging)

    l1 = Label(tabLanging, text="Registrate:", fg="#6c584c", font=("Arial", 24))
    l1.place(x=10, y=15)
    l4 = Label(tabLanging, text="Ingrese su nombre:", fg="#6c584c", font=("Arial", 12))
    l4.place(x=10, y=80)
    e4 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e4.place(x=190, y=80)

    l5 = Label(tabLanging, text="Ingrese su correo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=110)
    e5 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=190, y=110)

    l6 = Label(tabLanging, text="Ingrese su contraseña:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=140)
    e6 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=190, y=140)



    if tipoCuenta == "administrador":
        l7 = Label(tabLanging, text="Ingrese el tipo de cuenta:", fg="#6c584c", font=("Arial", 12))
        l7.place(x=10, y=170)
        e7 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
        e7.place(x=190, y=170)

        tipoCuenta = e7.get()


    btn3 = Button(tabLanging, text="Crear cuenta", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
              command=lambda: CreateAccount(usuarios, e4.get(), e5.get(), e6.get(), tipoCuenta))
    btn3.place(x=510, y=80, height=50)
    return tabLanging

def iniciarSesion(): 
    correo = e2.get()
    contrasena = e3.get()
    if correo == "" or contrasena == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos")
    else:
        #validar el correo y la contraseña
        tipoCuenta = login(usuarios, correo, contrasena)

        administrador = ["agregar/eliminar restaurante", "agregar/eliminar producto", "agregar/eliminar menu", "editar menu", "eliminar usuario"]
        consultor = ["obtener estadisticas", "reporte de resenias con ordenamiento arbitrario"]
        cliente = ["crear/eliminar cuenta", "editar informacion de la cuenta", "realizar una resena de un producto especifico", "realizar una resena de un combo"]
        mesero = ["crear orden", "ver orden", "cambiar el estado de la orden"]
    
        global lrol2
        lrol2.config(text=tipoCuenta)
        if tipoCuenta == "administrador":
            global tabs
            for tab_id in tabs: 
                tab.forget(tab_id)
                
            tabLanging = landingPage(tipoCuenta)
            tabs.append(tabLanging)

            
            for nombre in administrador:
                frame = ttk.Frame(tab)
                tab.add(frame, text=nombre)
                tabs.append(frame)

                if nombre == administrador[0]:
                    mod_restaurante(frame,restaurantes)
                elif nombre == administrador[1]:
                    mod_producto(frame, productos, combos)
                elif nombre == administrador[2]:
                    mod_menu(frame, combos)
                elif nombre == administrador[3]:
                    mod_combos(frame, combos)
                elif nombre == administrador[4]:
                    delete_usuario(frame, usuarios, ordenes)
            

        elif tipoCuenta == "consultor":
            for nombre in consultor:
                frame = ttk.Frame(tab)
                tab.add(frame, text=nombre)
                tabs.append(frame)

                if nombre == consultor[0]:
                    pass
                elif nombre == consultor[1]:
                    pass

        elif tipoCuenta == "cliente":
            for nombre in cliente:
                frame = ttk.Frame(tab)
                tab.add(frame, text=nombre)
                tabs.append(frame)
                
                if nombre == cliente[0]:
                    pass
                elif nombre == cliente[1]:
                    pass
                if nombre == cliente[2]:
                    pass
                elif nombre == cliente[3]:
                    pass
                

        elif tipoCuenta == "mesero":
            for nombre in mesero:
                frame = ttk.Frame(tab)
                tab.add(frame, text=nombre)
                tabs.append(frame)

                if nombre == mesero[0]:
                    pass
                elif nombre == mesero[1]:
                    pass
                if nombre == mesero[2]:
                    pass


v = Tk()
v.title("caféCITo ☕🍪")
v.geometry("800x800")
v.config(bg="#e3d5ca")
l1 = Label(v, text="CaféCITo ☕🍪", fg= "#6c584c" ,font=("Arial", 24), bg="#e3d5ca")
l1.pack(pady=20)
l2 = Label(v, text="Ingrese su correo:", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
l2.place(x=10, y=80)
e2 = Entry(v, width=30, font=("Arial", 12), bg="#f4f1e6")
e2.place(x=190, y=80)
e2.insert(0, "jacksonjuan@example.net")

l3 = Label(v, text="Ingrese su contraseña:", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
l3.place(x=10, y=110)
e3 = Entry(v, width=30, font=("Arial", 12), bg="#f4f1e6")
e3.place(x=190, y=110)
e3.insert(0, "^fgMG8Nm7U")

lrol = Label(v, text="Rol:", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
lrol.place(x=10, y=145)
lrol2 = Label(v, text="", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
lrol2.place(x=40, y=145)

btn1 = Button(v, text="Iniciar sesión", fg="#6c584c", font=("Arial", 12), bg="#f4f1e6", command=iniciarSesion)
btn1.place(x=510, y=80, height=50)
btn2 = Button(v, text="Cerrar sesión", fg="#ffffff", font=("Arial", 12), bg="#78290f", command=CerrarSesion)
btn2.place(x=630, y=80, height=50)

#pestañas 
tab= ttk.Notebook(v)
tab.pack()
tab.config(width="780", height="600")
tab.place(x=10,y=170)

landingPage()


v.mainloop()
