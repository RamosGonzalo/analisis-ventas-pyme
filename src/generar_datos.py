import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('es_AR')

random.seed(42)
fake.seed(42)

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

def generar_venta(id_venta):
    pass