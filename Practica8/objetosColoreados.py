import random
import math
from abc import ABC, abstractmethod
class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self):
        pass
Colores=["azul","lila","naranja","verde","amarillo","rosa","rojo"]

class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str =None):
        color=color or random.choice(Colores)
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado ({super().__str__()}, Lado: {self.lado:.2f})"

class Circulo(Figura):
    def __init__(self, radio: float, color: str =None):
        color=color or random.choice(Colores)
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo ({super().__str__()}, Radio: {self.radio:.2f})"

figuras = []
for _ in range(5):
    tipo = random.randint(1, 2)  # 1 = Cuadrado, 2 = Circulo
    if tipo == 1:
        lado = random.uniform(1.0, 10.0)
        figura = Cuadrado(lado)
    else:
        radio = random.uniform(1.0, 10.0)
        figura = Circulo(radio)
    figuras.append(figura)

for figura in figuras:
    print(figura)
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
    if isinstance(figura, Coloreado):
        print(f"Cómo colorear: {figura.como_colorear()}")
    else:
        print("Cómo colorear: No aplica")
    print("_" * 40)
