from pymongo import MongoClient
import pandas as pd
from collections import Counter
from bson import ObjectId
import re
import ast

uri = "mongodb+srv://angelargd8:TsTwymNjqBo7MysP@cluster0.wic81.mongodb.net"
client = MongoClient(uri)
db = client["restaurante"]

#ordenes y productos
ordenes = list(db["ordenes"].find())
productos = list(db["productos"].find())
productos_dict = {p["_id"]: p["nombreProducto"] for p in productos}

df_ordenes = pd.DataFrame(ordenes)

# KPI 1 : total de ventas
total_ventas = df_ordenes["precioTotal"].sum()
print("KPI 1: Total de ventas")
print("Total de ventas: "+ str(total_ventas))


# KPI 2: producto más vendido
#esta funcion es para limpiar el campo pedido de las ordenes, ya que en la base de datos se guardan como ObjectId y no como string
def limpiar_objectid(texto):
    return re.sub(r"ObjectId\('([a-fA-F0-9]{24})'\)", r"'\1'", texto)

ordenes =list(db["ordenes"].find())
productos= list(db["productos"].find())
productos_dict = {str(p["_id"]): p["nombreProducto"] for p in productos}

#conteo productos
conteo_productos = Counter()

for orden in ordenes:
    pedido_raw = orden.get("pedido", [])

    if isinstance(pedido_raw, str):
        try:
            pedido_limpio = limpiar_objectid(pedido_raw)
            pedido = ast.literal_eval(pedido_limpio)
        except:
            print("error al parsear pedido como lista:", pedido_raw)
            continue
    else:
        pedido = pedido_raw

    for item in pedido:
        if not isinstance(item, dict):
            continue
        if "producto" not in item or "cantidad" not in item:
            continue
        producto_id = str(item["producto"])
        conteo_productos[producto_id] += item["cantidad"]

# Top productos
top5 = conteo_productos.most_common(5)
top5_productos = [
    {"producto": productos_dict.get(pid, "Desconocido"), "cantidad": cantidad}
    for pid, cantidad in top5
]

print(f"Total de ventas: ${total_ventas}")
print("Top productos más vendidos:")
for p in top5_productos:
    print(f"- {p['producto']}: {p['cantidad']} unidades")

#cantidad de ordenes por metodo de pago
metodos_pago = df_ordenes["metodoPago"].value_counts().to_dict()

db.metricas.delete_many({})  # limpiar anteriores
db.metricas.insert_one({
    "totalVentas": total_ventas,
    "ordenesPorMetodoPago": metodos_pago,
    "top5Productos": top5_productos
})

print("Metricas insertadas")
