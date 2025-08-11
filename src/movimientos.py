from datetime import datetime

class MovimientoStock:
    def __init__(self, codigo_producto, tipo, cantidad, proveedor=None, fecha=None):
        self.codigo_producto = codigo_producto  # Código del producto
        self.tipo = tipo  # "ingreso" o "salida"
        self.cantidad = int(cantidad)
        self.proveedor = proveedor if proveedor else "Desconocido"
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.fecha} | {self.tipo.upper()} | {self.codigo_producto} | Cantidad: {self.cantidad} | Proveedor: {self.proveedor}"
