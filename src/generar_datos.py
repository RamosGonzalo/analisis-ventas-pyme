import os
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

os.makedirs('data/raw', exist_ok=True)
ruta_salida = 'data/raw/ventas_generadas.csv'

fake = Faker('es_AR')

random.seed(42)
fake.seed_instance(42)

PRODUCTOS = [
    {"nombre": "Auriculares Bluetooth", "categoria": "Electrónica", "precio": 18000},
    {"nombre": "Cargador USB-C", "categoria": "Electrónica", "precio": 6500},
    {"nombre": "Parlante Portátil", "categoria": "Electrónica", "precio": 25000},
    {"nombre": "Juego de Sábanas", "categoria": "Hogar", "precio": 15000},
    {"nombre": "Set de Vasos", "categoria": "Hogar", "precio": 8000},
    {"nombre": "Remera Básica", "categoria": "Indumentaria", "precio": 9000},
    {"nombre": "Campera de Abrigo", "categoria": "Indumentaria", "precio": 32000},
    {"nombre": "Pelota de Fútbol", "categoria": "Deportes", "precio": 12000},
    {"nombre": "Botella Térmica", "categoria": "Deportes", "precio": 10000},
]
SUCURSALES = ["Palermo", "Belgrano", "Nuñez"]
FECHA_INICIO = datetime(2024, 1, 1)
FECHA_FIN = datetime(2025, 12, 31)
CANTIDAD_VENTAS = 3000

def generar_fecha(inicio, fin):
    dias_totales = (fin - inicio).days
    while True:
        dia_random = random.randint(0, dias_totales)
        fecha = inicio + timedelta(days=dia_random)
        if fecha.weekday() in [4, 5, 6]:
            if random.random() < 0.7:
                return fecha
        else:
            if random.random() < 0.3:
                return fecha     

def generar_venta(id_venta):
    producto = random.choice(PRODUCTOS)
    sucursal = random.choice(SUCURSALES)
    fecha = generar_fecha(FECHA_INICIO, FECHA_FIN)
    
    cantidad = random.randint(1, 5)
    
    precio_unitario = round(producto['precio'] * random.uniform(0.95, 1.05), 2)
    
    monto_total = round(cantidad * precio_unitario, 2)
    
    return {
        "id_venta": id_venta,
        "fecha": fecha.strftime("%Y-%m-%d"),
        "sucursal": sucursal,
        "producto": producto['nombre'],
        "categoria": producto['categoria'],
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "monto_total": monto_total,
        "cliente": fake.name()
    }

ventas = [generar_venta(i) for i in range(1, CANTIDAD_VENTAS + 1)]

df = pd.DataFrame(ventas)

df = df.sort_values("fecha").reset_index(drop=True)
df.to_csv(ruta_salida, index=False, encoding="utf-8-sig")

print(f"\nArchivo guardado en: {ruta_salida}")