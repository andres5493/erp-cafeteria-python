from productos import Producto

def main():
    print("🟢 Probando creación de producto...\n")

    cafe = Producto(
        codigo="CAF001",
        nombre="Café de Colombia",
        categoria="Café en grano",
        costo=180,
        precio=350,
        stock=20
    )

    print(cafe)
    print(f"Ganancia por unidad: ${cafe.calcular_ganancia_unidad():.2f}")

    cafe.actualizar_stock(10)
    print(f"Nuevo stock: {cafe.stock}")

if __name__ == "__main__":
    main()

