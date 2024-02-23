class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad en stock: {self.cantidad_en_stock}")


class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad_en_stock, marca):
        super().__init__(nombre, precio, cantidad_en_stock)
        self.marca = marca

    def mostrar_informacion_electronico(self):
        self.mostrar_informacion()
        print(f"Marca: {self.marca}")


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad_en_stock, talla):
        super().__init__(nombre, precio, cantidad_en_stock)
        self.talla = talla

    def mostrar_informacion_ropa(self):
        self.mostrar_informacion()
        print(f"Talla: {self.talla}")



electronico1 = Electronico("Laptop", 1200, 10, "HP")
ropa1 = Ropa("Camiseta", 20, 50, "M")

print("Información del producto electrónico:")
electronico1.mostrar_informacion_electronico()

print("\nInformación del producto de ropa:")
ropa1.mostrar_informacion_ropa()
