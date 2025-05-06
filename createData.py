from faker import Faker
from random import randint, choice, sample
from datetime import datetime, timedelta
from bson import ObjectId, json_util
import json

fake = Faker()
fake.unique.clear() 
NUM_DOCS = 500

def random_date(start_year=2018):
    start = datetime(start_year, 1, 1)
    return start + timedelta(days=randint(0, (datetime.now() - start).days))

def create_usuarios(ordenes_ids):
    
    return {
        "_id": ObjectId(),
        "nombre": fake.name(),
        "email": fake.unique.email(),
        "contrasena": fake.password(),
        "historialPedidos": sample(ordenes_ids, randint(0, min(5, len(ordenes_ids)))), #lista de ordenes, referenciado a la coleccion de ordenes
        "tipoCuenta": choice(["administrador", "consultor", "cliente", "mesero"]),   
    }

def create_restaurantes():
    lat = float(fake.latitude())
    lon = float(fake.longitude())
    return {
        "_id": ObjectId(),
        "sucursal": fake.company(),
        "numeroMesas": randint(1, 20),
        "ubicacion": {
            "type": "Point",
            "coordinates": [lon, lat]
        }
    }

def create_combo(productos_ids):

    nombresCombos = [
    "Capuccino con galletas",
    "Sandwich con Latte",
    "Brownie y Capuccino",
    "Panqueques y Chocolate Caliente",
    "Tostadas Francesas y Café negro",
    "Croissant y Chocolate Caliente",
    "Combo Desayuno Clásico",
    "Wrap Vegano con Té Helado",
    "Combo Almuerzo Ejecutivo",
    "Hamburguesa con Papas y Soda",
    "Bagel con Queso y Café Americano",
    "Pizza Personal con Horchata",
    "Panini y Espresso",
    "Muffin y Latte"
    "Tardes Dulces: Pastel y Cappuccino",
]
    
    return{
        "_id": ObjectId(),
        "nombreCombo": choice(nombresCombos),
        "items": sample(productos_ids, randint(1, 3)), #referenciado a la coleccion de platillos
        "precio": round(randint(1, 100) + randint(0, 99) / 100, 2),
        "imagenCombo": fake.image_url(),
    }

def create_productos():

    productos = [
    "Croissant de mantequilla",
    "Muffin de arándanos",
    "Brownie de chocolate",
    "Pan de banana",
    "Galletas con chispas de chocolate",
    "Rollito de canela",
    "Tarta de manzana",
    "Cheesecake clásico",
    "Cupcake de vainilla",
    "Café americano",
    "Espresso",
    "Capuccino",
    "Latte",
    "Latte vainilla",
    "Mocha",
    "Té chai latte",
    "Té negro",
    "Té verde",
    "Chocolate caliente",
    "Té helado de durazno",
    "Frapuccino de vainilla",
    "Smoothie de fresa y plátano",
]
    
    return{
        "_id": ObjectId(),
        "tipoProducto" : choice(["entrada", "plato fuerte", "postre", "bebida"]),
        "nombreProducto": choice(productos),
        "descripcion": fake.text(),
        "precio": round(randint(1, 100) + randint(0, 99) / 100, 2),
        "imagenProducto": fake.image_url(),
    }

def create_ordenes(productos_ids, usuario_id,productos_dict):
    pedido = []
    precio_total = 0
    for i in range(randint(1, 3)):
        producto_id = choice(productos_ids)
        cantidad = randint(1, 5)
        precio_unitario = productos_dict[producto_id]["precio"]
        precio_total += cantidad * precio_unitario
        pedido.append({
            "producto": producto_id,
            "cantidad": cantidad,
            "especificaciones": fake.sentence()
        })


    return{
        "_id": ObjectId(),
        "precioTotal": round(precio_total, 2),
        "nombreCliente": usuario_id, #referenciado a la coleccion de usuarios 
        "pedido": pedido, #referenciado a la coleccion de productos, cantidad, especificaciones
        "estado": choice([True, False]), #True = entregado, False = no entregado
        "fecha": random_date(),
        "metodoPago": choice(["efectivo", "tarjeta", "transferencia"]),
    }


def create_resenias(producto_o_combo_id, usuario_id):
    return{
        "_id": ObjectId(),
        "producto": producto_o_combo_id,#referenciado 
        "calificacion": round(randint(1, 5) + randint(0, 9) / 10, 1),
        "comentario": fake.text(),
        "nombreUsuario": usuario_id, #referenciado a la coleccion de usuarios
    }


def save_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_util.dumps(data, indent=4))


def main():
    # 1. crear productos
    productos = [create_productos() for _ in range(100)]
    productos_dict = {p["_id"]: p for p in productos}
    productos_ids = list(productos_dict.keys())

    # 2. crear combos referencian productos
    combos = [create_combo(productos_ids) for _ in range(30)]

    # 3. crear restaurantes con ubicacion geoespacia
    restaurantes = [create_restaurantes() for _ in range(20)]

    # 4. crear usuarios vacios, se llenarán con órdenes luego
    usuarios = []

    # 5. crear ordenes y asociarlas a usuarios
    ordenes = []
    for _ in range(500):
        usuario_id = ObjectId()
        orden_ids = []
        for _ in range(randint(1, 5)):
            orden = create_ordenes(productos_ids, usuario_id, productos_dict)
            ordenes.append(orden)
            orden_ids.append(orden["_id"])
        usuario = create_usuarios(orden_ids)
        usuario["_id"] = usuario_id
        usuarios.append(usuario)
    


    # 6. Crear reseñas
    resenias = []
    for _ in range(500):
        if choice([True, False]):
            ref_id = choice(productos_ids)
        else:
            ref_id = choice([combo["_id"] for combo in combos])
        usuario_id = choice([u["_id"] for u in usuarios])
        resenias.append(create_resenias(ref_id, usuario_id))



    # 7. Guardar todos en json
    save_to_json("./data/productos.json", productos)

    save_to_json("./data/combos.json", combos)
    save_to_json("./data/restaurantes.json", restaurantes)
    save_to_json("./data/usuarios.json", usuarios)
    save_to_json("./data/ordenes.json", ordenes)
    save_to_json("./data/resenias.json", resenias)

    print("se guardaron los datos")

main()