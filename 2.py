class Empleado(Persona):
    def __init__(self, nombre, edad, cargo, salario):
        super().__init__(nombre, edad)
        self.cargo = cargo
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.cargo}.")

    def recibir_salario(self):
        print(f"{self.nombre} ha recibido su salario de {self.salario}.")

# Crear una instancia de la clase derivada Empleado
empleado1 = Empleado(nombre="Ana", edad=28, cargo="Desarrollador", salario=50000)

# Utilizar métodos de la clase base y la clase derivada
empleado1.presentarse()
empleado1.trabajar()
empleado1.recibir_salario()
