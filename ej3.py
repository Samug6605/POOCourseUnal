from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase raíz abstracta de la jerarquía taxonómica de animales.
    Almacena los atributos comunes (sonido, alimentos, hábitat y nombre
    científico) y declara los métodos abstractos que cada animal concreto
    debe implementar.
    """

    def __init__(self, sonido, alimentos, habitat, nombre_cientifico):
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat
        self.nombre_cientifico = nombre_cientifico

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    """Subclase intermedia de Animal para los cánidos."""
    pass


class Felino(Animal):
    """Subclase intermedia de Animal para los felinos."""
    pass


class Perro(Canido):

    def __init__(self):
        super().__init__(
            sonido="Ladrido",
            alimentos="Carnívora",
            habitat="Doméstico",
            nombre_cientifico="Canis lupus familiaris"
        )

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Lobo(Canido):

    def __init__(self):
        super().__init__(
            sonido="Aullido",
            alimentos="Carnívora",
            habitat="Bosque",
            nombre_cientifico="Canis lupus"
        )

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Leon(Felino):

    def __init__(self):
        super().__init__(
            sonido="Rugido",
            alimentos="Carnívora",
            habitat="Pradera",
            nombre_cientifico="Panthera leo"
        )

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Gato(Felino):

    def __init__(self):
        super().__init__(
            sonido="Maullido",
            alimentos="Ratones",
            habitat="Doméstico",
            nombre_cientifico="Felis silvestris catus"
        )

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class PruebaAnimales:
    """Clase de prueba para la jerarquía de animales."""

    @staticmethod
    def main():
        animales = [Perro(), Lobo(), Leon(), Gato()]

        for animal in animales:
            print(f"Nombre científico = {animal.get_nombre_cientifico()}")
            print(f"Sonido            = {animal.get_sonido()}")
            print(f"Alimentación      = {animal.get_alimentos()}")
            print(f"Hábitat           = {animal.get_habitat()}")
            print()


PruebaAnimales.main()
