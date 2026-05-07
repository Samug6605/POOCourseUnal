class Persona:
    """
    Crear una clase Persona con los siguientes 
    atributos: nombre, apellido, número de documento de identidad y año de nacimiento. 
    Luego, crear un método que muestre por pantalla los datos personales de la persona.
    """

    def __init__(self, nombre, apellido, numero_documento, año_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.año_nacimiento = año_nacimiento

    def datos_personales(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Número de documento de identidad = {self.numero_documento}")
        print(f"Año de nacimiento = {self.año_nacimiento}")


print("--- Persona 1 ---")
nombre = input("Ingrese el nombre:")
apellido = input("Ingrese el apellido:")
numero_documento = input("Ingrese el numero de documento de identidad:")
año_nacimiento = int(input("Ingrese el año de nacimiento:"))
persona1 = Persona(nombre, apellido, numero_documento, año_nacimiento)

print("--- Persona 2 ---")
nombre = input("Ingrese el nombre:")
apellido = input("Ingrese el apellido:")
numero_documento = input("Ingrese el numero de documento de identidad:")
año_nacimiento = int(input("Ingrese el año de nacimiento:"))
persona2 = Persona(nombre, apellido, numero_documento, año_nacimiento)

persona1.datos_personales()
persona2.datos_personales()
