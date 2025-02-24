import math
import turtle

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x**2 + self.y**2)
        angulo = math.atan2(self.y, self.x)
        return radio, angulo

    def __str__(self):
        radio, angulo = self.coord_polares()
        return f'Punto en coordenadas cartesianas: ({self.x}, {self.y}) - Polares: (r={radio:.2f}, θ={angulo:.3f} rad)'
class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def distancia(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def dibuja_linea(self):
        turtle.penup()
        turtle.goto(self.p1.x * 50, self.p1.y * 50)
        turtle.pendown()
        turtle.goto(self.p2.x * 50, self.p2.y * 50)

    def __str__(self):
        return f'La línea entre ({self.p1.x},{self.p1.y}) y ({self.p2.x},{self.p2.y}) tiene una distancia de: {self.distancia():.2f}'
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def dibuja_circulo(self):
        turtle.penup()
        turtle.goto(self.centro.x * 50, (self.centro.y * 50) - (self.radio * 50))
        turtle.pendown()
        turtle.circle(self.radio * 50)

    def __str__(self):
        return f'Círculo con centro en {self.centro} y radio {self.radio:.2f}'

p1 = Punto(1, -4)
p2 = Punto(-3, 3)


linea = Linea(p1, p2)
radio_circulo = linea.distancia() / 2
centro_circulo = Punto((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

circulo = Circulo(centro_circulo, radio_circulo)


print(linea)
print(circulo)


turtle.speed(3)
linea.dibuja_linea()
circulo.dibuja_circulo()

turtle.done()
