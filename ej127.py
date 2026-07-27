class Plato:
    """
    Representa un componente del pedido (primer plato, segundo plato,
    bebida o postre), con un nombre y un valor monetario.
    """

    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


class Pedido:
    """
    Calcula el valor de un pedido de restaurante.

    Python no soporta la sobrecarga de métodos como Java o C++ (si se
    definen varias funciones con el mismo nombre, solo la última queda
    registrada). Por eso se simula la sobrecarga con un único método que
    recibe argumentos opcionales (segundo_plato y postre), cubriendo así
    las tres combinaciones pedidas:
      - primer plato + bebida
      - primer plato + segundo plato + bebida
      - primer plato + segundo plato + bebida + postre
    """

    def calcular_valor_pedido(self, primer_plato, bebida, segundo_plato=None, postre=None):
        total = primer_plato.valor + bebida.valor
        if segundo_plato is not None:
            total += segundo_plato.valor
        if postre is not None:
            total += postre.valor
        return total


def main():
    pedido = Pedido()

    # Pedido 1: primer plato + bebida
    sopa = Plato("Sopa de verduras", 8000)
    gaseosa = Plato("Gaseosa", 4000)
    total1 = pedido.calcular_valor_pedido(sopa, gaseosa)
    print(f"Pedido 1 -> {sopa.nombre} + {gaseosa.nombre}: ${total1}")

    # Pedido 2: primer plato + segundo plato + bebida
    ensalada = Plato("Ensalada César", 9000)
    bandeja = Plato("Bandeja paisa", 22000)
    jugo = Plato("Jugo natural", 5000)
    total2 = pedido.calcular_valor_pedido(ensalada, jugo, segundo_plato=bandeja)
    print(f"Pedido 2 -> {ensalada.nombre} + {bandeja.nombre} + {jugo.nombre}: ${total2}")

    # Pedido 3: primer plato + segundo plato + bebida + postre
    crema = Plato("Crema de champiñones", 8500)
    pescado = Plato("Pescado a la plancha", 25000)
    limonada = Plato("Limonada de coco", 6000)
    flan = Plato("Flan de caramelo", 7000)
    total3 = pedido.calcular_valor_pedido(crema, limonada, segundo_plato=pescado, postre=flan)
    print(f"Pedido 3 -> {crema.nombre} + {pescado.nombre} + {limonada.nombre} + {flan.nombre}: ${total3}")


if __name__ == "__main__":
    main()
