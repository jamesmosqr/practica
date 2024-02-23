class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Clase derivada Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando en el curso {self.curso}.")

# Clase derivada Profesor que hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def enseñar(self):
        print(f"El profesor {self.nombre} enseña la asignatura de {self.asignatura}.")

# Crear instancias de las clases derivadas
estudiante1 = Estudiante(nombre="Juan", edad=20, curso="Matemáticas")
profesor1 = Profesor(nombre="Dra. Rodríguez", edad=35, asignatura="Física")

# Utilizar métodos de las clases base y derivadas
estudiante1.presentarse()
estudiante1.estudiar()

profesor1.presentarse()
profesor1.enseñar()


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




