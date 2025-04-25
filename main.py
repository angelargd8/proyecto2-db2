from pymongo import MongoClient
import pandas as pd
from collections import Counter
from bson import ObjectId
import re
import ast
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from login import login

uri = "mongodb+srv://angelargd8:TsTwymNjqBo7MysP@cluster0.wic81.mongodb.net"
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

def iniciarSesion(): 
    correo = e2.get()
    contrasena = e3.get()
    if correo == "" or contrasena == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos")
    else:
        #validar el correo y la contraseña
        tipoCuenta = login(usuarios, correo, contrasena)
        
        if tipoCuenta == "administrador":
            
            tab1= ttk.Frame(tab)
            tab.add(tab1, text="agregar/eliminar restaurante")
            tab2= ttk.Frame(tab)
            tab.add(tab2, text="agregar/eliminar producto")
            tab3= ttk.Frame(tab)
            tab.add(tab3, text="agregar/eliminar/editar menu")
            tab4= ttk.Frame(tab)
            tab.add(tab4, text="agregar/eliminar usuarios de consultores")

        elif tipoCuenta == "consultor":
            pass
        elif tipoCuenta == "cliente":
            pass
        elif tipoCuenta == "mesero":
            tab1= ttk.Frame(tab)
            tab.add(tab1, text="ingreso de orden")
            tab2= ttk.Frame(tab)
            tab.add(tab2, text="consulta general")
            tab3= ttk.Frame(tab)
            tab.add(tab3, text="consulta individual")
            tab4= ttk.Frame(tab)
            tab.add(tab4, text="modificacion de datos")


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

l3 = Label(v, text="Ingrese su contraseña:", fg= "#6c584c" , font=("Arial", 12),bg="#e3d5ca")
l3.place(x=10, y=110)
e3 = Entry(v, width=30, font=("Arial", 12), bg="#f4f1e6")
e3.place(x=190, y=110)

btn1 = Button(v, text="Iniciar sesión", fg="#6c584c", font=("Arial", 12), bg="#f4f1e6", command=iniciarSesion)
btn1.place(x=510, y=80, height=50)


#pestañas 
tab= ttk.Notebook(v)
tab.pack()
tab.config(width="800", height="500")
tab.place(x=10,y=150)



# v.resizable(0, 0)

v.mainloop()
