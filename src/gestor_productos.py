import json
import os
from productos import Producto
from movimientos import MovimientoStock

# Definir ruta absoluta al archivo productos.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO_PRODUCTOS = os.path.join(BASE_DIR, "data", "productos.json")
ARCHIVO_MOVIMIENTOS = os.path.join(BASE_DIR, "data", "movimientos.json")

### Cargar Produtos
def cargar_productos():
    """Carga los productos desde un archivo JSON, crea archivo si no existe."""
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as f:
            f.write("[]")  # Archivo vacío válido JSON

    with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
            return [Producto(**p) for p in datos]
        except json.JSONDecodeError:
            return []

def guardar_productos(productos):
    """Guarda los productos en un archivo JSON."""
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as f:
        json.dump([p.__dict__ for p in productos], f, indent=4, ensure_ascii=False)

def agregar_producto():
    """Solicita datos por consola y agrega un producto."""
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    costo = float(input("Costo: "))
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))

    nuevo = Producto(codigo, nombre, categoria, costo, precio, stock)

    productos = cargar_productos()
    productos.append(nuevo)
    guardar_productos(productos)
    print(f"✅ Producto '{nombre}' agregado con éxito.")

# Cargar Movimientos
def cargar_movimientos():
    if not os.path.exists(ARCHIVO_MOVIMIENTOS):
        with open(ARCHIVO_MOVIMIENTOS, "w", encoding="utf-8") as f:
            f.write("[]")
    with open(ARCHIVO_MOVIMIENTOS, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
            return [MovimientoStock(**m) for m in datos]
        except json.JSONDecodeError:
            return []

def guardar_movimientos(movimientos):
    with open(ARCHIVO_MOVIMIENTOS, "w", encoding="utf-8") as f:
        json.dump([m.__dict__ for m in movimientos], f, indent=4, ensure_ascii=False)

def registrar_ingreso_stock():
    print("\n🟢 Registrar ingreso de stock")
    codigo = input("Código producto: ")
    cantidad = int(input("Cantidad ingresada: "))
    proveedor = input("Proveedor: ")

    productos = cargar_productos()
    producto = next((p for p in productos if p.codigo == codigo), None)

    if producto is None:
        print("❌ Producto no encontrado.")
        return

    producto.actualizar_stock(cantidad)
    guardar_productos(productos)

    movimientos = cargar_movimientos()
    nuevo_movimiento = MovimientoStock(codigo, "ingreso", cantidad, proveedor)
    movimientos.append(nuevo_movimiento)
    guardar_movimientos(movimientos)

    print(f"✅ Ingreso de {cantidad} unidades al producto '{producto.nombre}' registrado con proveedor '{proveedor}'.")
