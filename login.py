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
            messagebox.showinfo("Inicio de sesión", "Bienvenido " + nombre)
            return True
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            return False
    else:
        messagebox.showerror("Error", "Usuario no encontrado")
        return False
