import math


class Circulo:
    """Figura geométrica definida por su radio en centímetros."""

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        """Retorna el área del círculo."""
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        """Retorna el perímetro (circunferencia) del círculo."""
        return 2 * math.pi * self.radio


class Rectangulo:
    """Figura geométrica definida por su base y altura en centímetros."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        """Retorna el área del rectángulo."""
        return self.base * self.altura

    def perimetro(self):
        """Retorna el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)


class Cuadrado:
    """Figura geométrica definida por la longitud de sus lados en centímetros."""

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        """Retorna el área del cuadrado."""
        return self.lado ** 2

    def perimetro(self):
        """Retorna el perímetro del cuadrado."""
        return 4 * self.lado


class TrianguloRectangulo:
    """Triángulo rectángulo definido por su base y altura en centímetros."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def hipotenusa(self):
        """Retorna la hipotenusa calculada con el teorema de Pitágoras."""
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def area(self):
        """Retorna el área del triángulo."""
        return (self.base * self.altura) / 2

    def perimetro(self):
        """Retorna el perímetro del triángulo."""
        return self.base + self.altura + self.hipotenusa()

    def tipo_triangulo(self):
        """Retorna el tipo de triángulo según la longitud de sus lados."""
        lado1, lado2, lado3 = self.base, self.altura, self.hipotenusa()
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"


class PruebaFiguras:
    """Clase de prueba para las figuras geométricas."""

    @staticmethod
    def main():
        circulo = Circulo(5)
        rectangulo = Rectangulo(4, 6)
        cuadrado = Cuadrado(4)
        triangulo = TrianguloRectangulo(3, 4)

        print("=== CÍRCULO ===")
        print("Área:", circulo.area())
        print("Perímetro:", circulo.perimetro())

        print("\n=== RECTÁNGULO ===")
        print("Área:", rectangulo.area())
        print("Perímetro:", rectangulo.perimetro())

        print("\n=== CUADRADO ===")
        print("Área:", cuadrado.area())
        print("Perímetro:", cuadrado.perimetro())

        print("\n=== TRIÁNGULO RECTÁNGULO ===")
        print("Área:", triangulo.area())
        print("Perímetro:", triangulo.perimetro())
        print("Hipotenusa:", triangulo.hipotenusa())
        print("Tipo:", triangulo.tipo_triangulo())


PruebaFiguras.main()
