from pymongo import MongoClient
import pandas as pd
from collections import Counter
from bson import ObjectId
import re
import ast
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from login import login, CreateAccount

uri = "mongodb+srv://angel:angel123@cluster0.krfnzqa.mongodb.net"
client = MongoClient(uri)
db = client["restaurante"]
print("Conectado a la base de datos")
# print("Base de datos: ", db.name)
# print("Colecciones: ", db.list_collection_names())
restaurantes = db["restaurantes"]
combos = db["combos"]
productos = db["productos"]
resenias = db["resenias"]
ordenes = db["ordenes"]
usuarios = db["usuarios"]

global tipoCuenta
global tabs
tabs =[]


def CerrarSesion():
    global tabs
    for tab_id in tab.tabs(): 
        tab.forget(tab_id)
    
    tabs.clear()
    # tab.destroy()
    landingPage()

def landingPage(tipoCuenta=None):
    tabLanging = ttk.Frame(tab)
    tab.add(tabLanging, text="Crear cuenta")
    tabs.append(tabLanging)

    l4 = Label(tabLanging, text="Ingrese su nombre:", fg="#6c584c", font=("Arial", 12))
    l4.place(x=10, y=20)
    e4 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e4.place(x=190, y=20)

    l5 = Label(tabLanging, text="Ingrese su correo:", fg="#6c584c", font=("Arial", 12))
    l5.place(x=10, y=50)
    e5 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e5.place(x=190, y=50)

    l6 = Label(tabLanging, text="Ingrese su contraseña:", fg="#6c584c", font=("Arial", 12))
    l6.place(x=10, y=80)
    e6 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
    e6.place(x=190, y=80)


    # nombre = e4.get()
    # email = e5.get()
    # constrasena = e6.get()
    # tipoCuenta = None

    if tipoCuenta == "administrador":
        l7 = Label(tabLanging, text="Ingrese el tipo de cuenta:", fg="#6c584c", font=("Arial", 12))
        l7.place(x=10, y=110)
        e7 = Entry(tabLanging, width=30, font=("Arial", 12), bg="#f4f1e6")
        e7.place(x=190, y=110)

        tipoCuenta = e7.get()


    btn3 = Button(tabLanging, text="Crear cuenta", fg="#ffffff", font=("Arial", 12), bg="#78290f", 
              command=lambda: CreateAccount(usuarios, e4.get(), e5.get(), e6.get(), tipoCuenta))
    btn3.place(x=510, y=20, height=50)
    return tabLanging

def iniciarSesion(): 
    correo = e2.get()
    contrasena = e3.get()
    if correo == "" or contrasena == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos")
    else:
        #validar el correo y la contraseña
        tipoCuenta = login(usuarios, correo, contrasena)

        administrador = ["agregar/eliminar restaurante", "agregar/eliminar producto", "agregar/eliminar/editar menu", "agregar/eliminar usuarios de consultores"]
        consultor = ["obtener estadisticas", "reporte de resenias con ordenamiento arbitrario"]
        cliente = ["crear/eliminar cuenta", "editar informacion de la cuenta", "realizar una resena de un producto especifico", "realizar una resena de un combo"]
        mesero = ["crear orden", "ver orden", "cambiar el estado de la orden"]

        
        
        if tipoCuenta == "administrador":
            global tabs
            for tab_id in tabs: 
                tab.forget(tab_id)
                
            tabLanging = landingPage(tipoCuenta)
            tabs.append(tabLanging)
            
            for i in range(len(administrador)): 
                frame = ttk.Frame(tab)
                tab.add(frame, text=administrador[i])
                tabs.append(frame)
            
                

        elif tipoCuenta == "consultor":
            for i in consultor: 
                frame = ttk.Frame(tab)
                tab.add(frame, text=consultor[i])
                tabs.append(frame)

        elif tipoCuenta == "cliente":
            for i in cliente: 
                frame = ttk.Frame(tab)
                tab.add(frame, text=cliente[i])
                tabs.append(frame)

        elif tipoCuenta == "mesero":
            for i in mesero: 
                frame = ttk.Frame(tab)
                tab.add(frame, text=mesero[i])
                tabs.append(frame)

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
e2.insert(0, "hsolomon@example.org")

l3 = Label(v, text="Ingrese su contraseña:", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
l3.place(x=10, y=110)
e3 = Entry(v, width=30, font=("Arial", 12), bg="#f4f1e6")
e3.place(x=190, y=110)
e3.insert(0, "!*5OuIQsxg")

btn1 = Button(v, text="Iniciar sesión", fg="#6c584c", font=("Arial", 12), bg="#f4f1e6", command=iniciarSesion)
btn1.place(x=510, y=80, height=50)
btn2 = Button(v, text="Cerrar sesión", fg="#ffffff", font=("Arial", 12), bg="#78290f", command=CerrarSesion)
btn2.place(x=630, y=80, height=50)

#pestañas 
tab= ttk.Notebook(v)
tab.pack()
tab.config(width="800", height="500")
tab.place(x=10,y=150)

landingPage()


# v.resizable(0, 0)

v.mainloop()
