class ArticuloCientifico:
    """
    Modela un artículo científico con sus metadatos: nombre, autor,
    palabras clave, nombre de la publicación, año y resumen.

    Python no permite definir varios __init__ (constructores sobrecargados)
    como Java. Para simular la sobrecarga y el encadenamiento pedido
    (cada constructor invoca al anterior) se usa __init__ como el primer
    constructor (solo nombre y autor), y dos @classmethod que actúan como
    constructores alternativos, cada uno invocando al anterior.
    """

    def __init__(self, nombre, autor):
        # Primer constructor: solo título y autor.
        self.nombre = nombre
        self.autor = autor
        self.palabras_claves = None
        self.nombre_publicacion = None
        self.anio = None
        self.resumen = None

    @classmethod
    def con_publicacion(cls, nombre, autor, palabras_claves, nombre_publicacion, anio):
        # Segundo constructor: invoca al primero y completa los demás datos.
        articulo = cls(nombre, autor)
        articulo.palabras_claves = palabras_claves
        articulo.nombre_publicacion = nombre_publicacion
        articulo.anio = anio
        return articulo

    @classmethod
    def completo(cls, nombre, autor, palabras_claves, nombre_publicacion, anio, resumen):
        # Tercer constructor: invoca al segundo y agrega el resumen.
        articulo = cls.con_publicacion(nombre, autor, palabras_claves, nombre_publicacion, anio)
        articulo.resumen = resumen
        return articulo

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Autor = {self.autor}")
        print(f"Palabras clave = {self.palabras_claves}")
        print(f"Nombre de la publicación = {self.nombre_publicacion}")
        print(f"Año = {self.anio}")
        print(f"Resumen = {self.resumen}")


def main():
    articulo = ArticuloCientifico.completo(
        nombre="Aprendizaje profundo aplicado a la clasificación de imágenes médicas",
        autor="Ana Torres",
        palabras_claves=["deep learning", "clasificación", "redes neuronales"],
        nombre_publicacion="Revista Colombiana de Computación",
        anio=2024,
        resumen="Este artículo presenta un enfoque de aprendizaje profundo para "
                "la clasificación de imágenes médicas, logrando una precisión "
                "del 95% en el conjunto de datos evaluado."
    )
    articulo.imprimir()


if __name__ == "__main__":
    main()
