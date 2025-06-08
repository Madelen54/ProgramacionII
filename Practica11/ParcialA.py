class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def __str__(self):
        return f"Anuncio    Numero: {self.numero}, Precio: ${self.precio:.2f}"

class Obra:
    def __init__(self, titulo: str, material: str, artista: 'Artista' = None, anuncio: 'Anuncio' = None):
        self.titulo = titulo
        self.material = material
        self.artistas = []
        if artista:
            self.artistas.append(artista)
        self.anuncio = anuncio

    def agregar_artista(self, artista: 'Artista'):
        if artista not in self.artistas:
            self.artistas.append(artista)

    def set_anuncio(self, anuncio: 'Anuncio'):
        self.anuncio = anuncio

    def __str__(self):
        artist_names = ", ".join([a.nombre for a in self.artistas]) if self.artistas else "N/A"
        anuncio_info = f", Anuncio: {self.anuncio.numero}" if self.anuncio else ", Sin Anuncio"
        return f"Titulo: {self.titulo}, Material: {self.material}, Artistas: {artist_names}{anuncio_info}"

class Artista:
    def __init__(self, nombre: str, ci: str, anos_experiencia: int):
        self.nombre = nombre
        self.ci = ci
        self.anos_experiencia = anos_experiencia

    def __str__(self):
        return f"Artista(Nombre: {self.nombre}, CI: {self.ci}, Años Experiencia: {self.anos_experiencia})"

class Pintura(Obra):
    def __init__(self, titulo, material, genero, artista: 'Artista' = None, anuncio: 'Anuncio' = None):
        super().__init__(titulo, material, artista, anuncio)
        self.genero = genero

    def __str__(self):
        artist_names = ", ".join([a.nombre for a in self.artistas]) if self.artistas else "N/A"
        anuncio_info = f", Anuncio: {self.anuncio.numero}" if self.anuncio else ", Sin Anuncio"
        return f"Titulo: {self.titulo}, Material: {self.material}, Genero: {self.genero}, Artistas: {artist_names}{anuncio_info}"

anuncio1 = Anuncio(numero=101, precio=500.00)
artista1 = Artista(nombre="Victor Mamani", ci="12345678", anos_experiencia=30)
artista2 = Artista(nombre="Claudia Morales", ci="87654321", anos_experiencia=25)
pintura_con_anuncio = Pintura(
    titulo="Noche en Marte",
    material="Óleo sobre lienzo",
    genero="Postimpresionismo",
    artista=artista1,
    anuncio=anuncio1
)
print(f"Pintura con anuncio: {pintura_con_anuncio}")
pintura_sin_anuncio = Pintura(
    titulo="Impacto",
    material="Óleo sobre lienzo",
    genero="Impresionismo",
    artista=artista2
)
print(f"Pintura sin anuncio: {pintura_sin_anuncio}\n")
if artista1.anos_experiencia > artista2.anos_experiencia:
    artista_mas_experiencia = artista1
else:
    artista_mas_experiencia = artista2

print(f"El artista con más años de experiencia es: {artista_mas_experiencia.nombre} ({artista_mas_experiencia.anos_experiencia} años)\n")
anuncio_para_pintura_sin_anuncio = Anuncio(numero=102, precio=750.00)
pintura_sin_anuncio.set_anuncio(anuncio_para_pintura_sin_anuncio)

print(f"Pintura 'Impacto' ahora con anuncio: {pintura_sin_anuncio}")

monto_total_venta = 0.0

if pintura_con_anuncio.anuncio:
    monto_total_venta += pintura_con_anuncio.anuncio.precio
    print(f"Precio de '{pintura_con_anuncio.titulo}': ${pintura_con_anuncio.anuncio.precio:.2f}")

if pintura_sin_anuncio.anuncio:
    monto_total_venta += pintura_sin_anuncio.anuncio.precio
    print(f"Precio de '{pintura_sin_anuncio.titulo}': ${pintura_sin_anuncio.anuncio.precio:.2f}")

print(f"\nEl monto total de venta de ambas pinturas es: ${monto_total_venta:.2f}")
