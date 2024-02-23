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


# Pilas aqui se captura toda la información por teclado
nombre_electronico = input("Ingrese el nombre del producto electrónico: ")
precio_electronico = float(input("Ingrese el precio del producto electrónico: "))
stock_electronico = int(input("Ingrese la cantidad en stock del producto electrónico: "))
marca_electronico = input("Ingrese la marca del producto electrónico: ")

nombre_ropa = input("\nIngrese el nombre del producto de ropa: ")
precio_ropa = float(input("Ingrese el precio del producto de ropa: "))
stock_ropa = int(input("Ingrese la cantidad en stock del producto de ropa: "))
talla_ropa = input("Ingrese la talla del producto de ropa: ")

# Crear instancias de las clases derivadas
electronico1 = Electronico(nombre_electronico, precio_electronico, stock_electronico, marca_electronico)
ropa1 = Ropa(nombre_ropa, precio_ropa, stock_ropa, talla_ropa)

# Mostrar información de los productos
print("\nInformación del producto electrónico:")
electronico1.mostrar_informacion_electronico()

print("\nInformación del producto de ropa:")
ropa1.mostrar_informacion_ropa()
