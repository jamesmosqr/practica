class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando en el curso {self.curso}.")


# Crear instancias de las clases
persona1 = Persona(nombre="Juan", edad=25)

estudiante1 = Estudiante(nombre="Maria", edad=20, curso="Inglés")
estudiante2 = Estudiante(nombre="Ana", edad=20, curso="Matematicas")
estudiante3 = Estudiante(nombre="Allan", edad=20, curso="religion")


estudiante1.estudiar()     # Imprimirá "Ana está estudiando en el curso Inglés."
estudiante2.estudiar()     # Imprimirá "Ana está estudiando en el curso Inglés."
estudiante3.estudiar()     # Imprimirá "Ana está estudiando en el curso I"














# Acceder a atributos y métodos de las clases base y derivada
#persona1.presentarse()    # Imprimirá "Hola, soy Juan y tengo 25 años."
#estudiante1.presentarse()  # Imprimirá "Hola, soy Ana y tengo 20 años."
