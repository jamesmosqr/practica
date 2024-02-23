class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=25)
persona2 = Persona(nombre="Ana", edad= 95)
persona3 = Persona(nombre="carlos", edad=9)


# Acceder a atributos y llamar a un método
#print(persona1.nombre)   # Imprimirá "Juan"
#print(persona1.edad)      # Imprimirá 25
persona1.presentarse()    # Imprimirá "Hola, soy Juan y tengo 25 años."

#print(persona2.nombre) # Imprimirá
#print(persona2.edad)    # Imprimirá
persona2.presentarse()  # Imprimirá
persona3.presentarse()