from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
from collections import Counter
from bson import ObjectId
import re
import ast
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox


def login(usuarios, correo, contrasena):
    # Buscar el usuario en la base de datos
    usuario = usuarios.find_one({"email": correo})
    
    if usuario:
        # Verificar la contraseña
        if usuario["contrasena"] == contrasena:
            nombre = usuario["nombre"]
            tipoCuenta = usuario["tipoCuenta"]
            messagebox.showinfo("Inicio de sesión", "Bienvenido " + nombre)
            return tipoCuenta
            
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            
    else:
        messagebox.showerror("Error", "Usuario no encontrado")
        

def CreateAccount(usuarios, nombre, email, constrasena, tipoCuenta=None):
    usuario_id = ObjectId()
    #buscar que el email no exista
    val_email = usuarios.find_one({"email": email})

    if nombre and email and constrasena:
        if not val_email:
            # Crear un nuevo usuario
            nuevo_usuario = {
                "_id": usuario_id,
                "nombre": nombre,
                "email": email,
                "contrasena": constrasena,
                "historialPedidos": [], 
                "tipoCuenta": tipoCuenta,   
            }
            
            # Insertar nuevo usuario en la base de datos
            usuarios.insert_one(nuevo_usuario)
            messagebox.showinfo("Crear cuenta", "Usuario creado con éxito")
        else:
            messagebox.showerror("Error", "El correo ya existe")

    else:
        messagebox.showerror("Error", "Por favor complete todos los campos")
        return None

    return usuario_id

def CerrarSesion():
    pass
