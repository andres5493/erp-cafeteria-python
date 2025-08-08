class Producto:
    def __init__(self, codigo, nombre, categoria, costo, precio, stock=0):
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre
        self.categoria = categoria
        self.costo = float(costo)
        self.precio = float(precio)
        self.stock = int(stock)

    def actualizar_stock(self, cantidad):
        self.stock += int(cantidad)

    def calcular_ganancia_unidad(self):
        return self.precio - self.costo

    def __str__(self):
        return f"{self.nombre} | ${self.precio:.2f} | Stock: {self.stock}"
