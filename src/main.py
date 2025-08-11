from productos import Producto
'''
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

from gestor_productos import agregar_producto, cargar_productos
def main():
    print("📦 Sistema de Gestión de Productos\n")
    while True:
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            productos = cargar_productos()
            if not productos:
                print("⚠ No hay productos registrados.")
            else:
                for p in productos:
                    print(p)
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
'''

from gestor_productos import agregar_producto, cargar_productos, registrar_ingreso_stock

def main():
    print("📦 Sistema de Gestión de Productos\n")
    while True:
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Registrar ingreso de stock")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            productos = cargar_productos()
            if not productos:
                print("⚠ No hay productos registrados.")
            else:
                for p in productos:
                    print(p)
        elif opcion == "3":
            registrar_ingreso_stock()
        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
