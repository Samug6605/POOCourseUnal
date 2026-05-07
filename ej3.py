from enum import Enum

# Enumeraciones
class TipoCombustible(Enum):
    GASOLINA = "gasolina"
    BIOETANOL = "bioetanol"
    DIESEL = "diésel"
    BIODIESEL = "biodiésel"
    GAS_NATURAL = "gas natural"

class TipoAutomovil(Enum):
    CIUDAD = "carro de ciudad"
    SUBCOMPACTO = "subcompacto"
    COMPACTO = "compacto"
    FAMILIAR = "familiar"
    EJECUTIVO = "ejecutivo"
    SUV = "suv"

class Color(Enum):
    BLANCO = "blanco"
    NEGRO = "negro"
    ROJO = "rojo"
    NARANJA = "naranja"
    AMARILLO = "amarillo"
    VERDE = "verde"
    AZUL = "azul"
    VIOLETA = "violeta"


# Clase Automóvil
class Automovil:

    def __init__(self, marca, modelo, motor, tipo_combustible,
                tipo_automovil, num_puertas, num_asientos,
                velocidad_maxima, color):
        
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0  # inicia en 0

    # Métodos get y set
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def get_num_puertas(self):
        return self.num_puertas

    def set_num_puertas(self, num_puertas):
        self.num_puertas = num_puertas

    def get_num_asientos(self):
        return self.num_asientos

    def set_num_asientos(self, num_asientos):
        self.num_asientos = num_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad):
        if 0 <= velocidad <= self.velocidad_maxima:
            self.velocidad_actual = velocidad
        else:
            print("Velocidad no válida")

    # Métodos de comportamiento
    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print("No se puede superar la velocidad máxima")
        else:
            self.velocidad_actual += incremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            print("No se puede tener velocidad negativa")
        else:
            self.velocidad_actual -= decremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self):
        self.velocidad_actual = 0
        print("El automóvil se ha detenido. Velocidad actual: 0 km/h")

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual > 0:
            tiempo = distancia / self.velocidad_actual
            return tiempo
        else:
            print("El vehículo está detenido, no se puede calcular el tiempo")
            return None

    def mostrar_info(self):
        print("\n--- Información del Automóvil ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Combustible: {self.tipo_combustible.value}")
        print(f"Tipo: {self.tipo_automovil.value}")
        print(f"Puertas: {self.num_puertas}")
        print(f"Asientos: {self.num_asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad actual: {self.velocidad_actual} km/h")


# Método main
if __name__ == "__main__":

    auto = Automovil(
        marca="Toyota",
        modelo=2020,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.COMPACTO,
        num_puertas=4,
        num_asientos=5,
        velocidad_maxima=180,
        color=Color.NEGRO
    )

    auto.mostrar_info()

    # Secuencia pedida
    auto.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(20)
    auto.desacelerar(50)
    auto.frenar()

    # Ejemplo de cálculo de tiempo
    tiempo = auto.calcular_tiempo_llegada(100)  # 100 km
    if tiempo:
        print(f"Tiempo estimado de llegada: {tiempo:.2f} horas")
