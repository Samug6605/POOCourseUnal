from enum import Enum

UA_KM = 149_597_870  # 1 unidad astronómica en km

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:

    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0, volumen=0.0,
                diametro=0, distancia_sol=0, tipo=None, es_observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa                  # kg
        self.volumen = volumen            # km³
        self.diametro = diametro          # km
        self.distancia_sol = distancia_sol  # millones de km
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa} kg")
        print(f"Volumen del planeta = {self.volumen} km³")
        print(f"Diámetro del planeta = {self.diametro} km")
        print(f"Distancia al sol = {self.distancia_sol} millones de km")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        return self.masa / self.volumen if self.volumen != 0 else 0

    def planeta_es_exterior(self):
        # Exterior: más allá del cinturón de asteroides (3.4 UA)
        limite_millones_km = (3.4 * UA_KM) / 1_000_000  # ≈ 508.63 millones de km
        return self.distancia_sol > limite_millones_km


# --- Main ---
tierra = Planeta(
    nombre="Tierra",
    cantidad_satelites=1,
    masa=5.97e24,
    volumen=1.08e12,
    diametro=12_742,
    distancia_sol=150,
    tipo=TipoPlaneta.TERRESTRE,
    es_observable=True
)

jupiter = Planeta(
    nombre="Júpiter",
    cantidad_satelites=95,
    masa=1.90e27,
    volumen=1.43e15,
    diametro=139_820,
    distancia_sol=779,
    tipo=TipoPlaneta.GASEOSO,
    es_observable=True
)

for planeta in [tierra, jupiter]:
    planeta.imprimir()
    print(f"Densidad = {planeta.calcular_densidad():.4f} kg/km³")
    print(f"Es planeta exterior = {planeta.planeta_es_exterior()}")
    print()
