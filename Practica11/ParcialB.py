class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def __str__(self):
        return f"Anuncio    Numero: {self.numero}, Precio: ${self.precio:.2f})"

class Obra:
    def __init__(self, titulo: str, material: str, artista: 'Artista' = None, anuncio: 'Anuncio' = None):
        self.titulo = titulo
        self.material = material
        self.artistas = []  # Cambiado a una lista para acomodar múltiples artistas
        if artista:
            self.artistas.append(artista)
        self.anuncio = anuncio

    def agregar_artista(self, artista: 'Artista'):
        if artista not in self.artistas:
            self.artistas.append(artista)

    def set_anuncio(self, anuncio: 'Anuncio'):
        self.anuncio = anuncio

    def get_precio_anuncio(self):
        return self.anuncio.precio if self.anuncio else 0.0

    def __str__(self):
        nombres_artistas = ", ".join([a.nombre for a in self.artistas]) if self.artistas else "N/A"
        info_anuncio = f", Anuncio: {self.anuncio.numero} (Precio: ${self.anuncio.precio:.2f})" if self.anuncio else ", Sin Anuncio"
        return f"Obra(Titulo: {self.titulo}, Material: {self.material}, Artistas: {nombres_artistas}{info_anuncio})"

class Artista:
    def __init__(self, nombre, ci, anos_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.anos_experiencia = anos_experiencia

    def __str__(self):
        return f"Artista   Nombre: {self.nombre}, CI: {self.ci}, Años Experiencia: {self.anos_experiencia}"

class Pintura(Obra):
    def __init__(self, titulo: str, material: str, genero: str, artista: 'Artista' = None, anuncio: 'Anuncio' = None):
        super().__init__(titulo, material, artista, anuncio)
        self.genero = genero

    def __str__(self):
        nombres_artistas = ", ".join([a.nombre for a in self.artistas]) if self.artistas else "N/A"
        info_anuncio = f", Anuncio: {self.anuncio.numero} (Precio: ${self.anuncio.precio:.2f})" if self.anuncio else ", Sin Anuncio"
        return f" Titulo: {self.titulo}, Material: {self.material}, Genero: {self.genero}, Artistas: {nombres_artistas}{info_anuncio}"

artista_p1 = Artista(nombre="Lupita Marca", ci="154278", anos_experiencia=20)
artista_p2 = Artista(nombre="Diego Rivera", ci="705632", anos_experiencia=32)
artista_p3 = Artista(nombre="Santiago Prado", ci="1475896", anos_experiencia=15)
anuncio_a = Anuncio(numero=201, precio=1200.00)
anuncio_b = Anuncio(numero=220, precio=950.00)
anuncio_c = Anuncio(numero=103, precio=1500.00)
pintura1 = Pintura(
    titulo="La  luz de verano",
    material="Óleo sobre lienzo",
    genero="Autorretrato",
    artista=artista_p1,
    anuncio=anuncio_a
)
print(f"Pintura 1: {pintura1}")

pintura2 = Pintura(
    titulo="la mañana detras del valle",
    material="Fresco",
    genero="Muralismo",
    artista=artista_p2,
    anuncio=anuncio_b
)
print(f"Pintura 2: {pintura2}\n")
todos_los_artistas = set()
for artista in pintura1.artistas:
    todos_los_artistas.add(artista)
for artista in pintura2.artistas:
    todos_los_artistas.add(artista)
print("-*40")
if todos_los_artistas:
    total_experiencia = sum(artista.anos_experiencia for artista in todos_los_artistas)
    promedio_experiencia = total_experiencia / len(todos_los_artistas)
    print(f"El promedio de años de experiencia de los artistas es: {promedio_experiencia:.2f} años")
else:
    print("Error")
nombre_artista_a_modificar = "Lupita Marca"
incremento_precio = 270.00

if pintura1.artistas and any(artista.nombre == nombre_artista_a_modificar for artista in pintura1.artistas):
    if pintura1.anuncio:
        precio_original = pintura1.anuncio.precio
        pintura1.anuncio.precio += incremento_precio
        print(f"Precio de '{pintura1.titulo}' (Artista: {nombre_artista_a_modificar}) incrementado.")
        print(f"Precio Original: ${precio_original:.2f}, Nuevo Precio: ${pintura1.anuncio.precio:.2f}")
    else:
        print(f"La pintura '{pintura1.titulo}' del artista {nombre_artista_a_modificar} no tiene un anuncio para incrementar su precio.")
elif pintura2.artistas and any(artista.nombre == nombre_artista_a_modificar for artista in pintura2.artistas):
    if pintura2.anuncio:
        precio_original = pintura2.anuncio.precio
        pintura2.anuncio.precio += incremento_precio
        print(f"Precio de '{pintura2.titulo}' (Artista: {nombre_artista_a_modificar}) incrementado.")
        print(f"Precio Original: ${precio_original:.2f}, Nuevo Precio: ${pintura2.anuncio.precio:.2f}")
    else:
        print(f"La pintura '{pintura2.titulo}' del artista {nombre_artista_a_modificar} no tiene un anuncio para incrementar su precio.")
else:
    print(f"No se encontró una pintura asociada al artista '{nombre_artista_a_modificar}' entre las pinturas creadas.")

print("\nEstado final de las pinturas después de la modificación:")
print(f"Pintura 1: {pintura1}")
print(f"Pintura 2: {pintura2}")
