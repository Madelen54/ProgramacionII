import math
from multimethod import multimethod

class FiguraGeometrica:
    @multimethod
    def Area(self, radio: float):
        return math.pi * radio * radio

    @multimethod
    def Area(self, base: int, altura: int):
        return base * altura
    @multimethod
    def Area(self, cateto1:float ,cateto2:float):
        return (cateto1*cateto2)/2
    @multimethod
    def Area(self, bmayor:float,bmenor:float,altura:float):
        return (bmayor+bmenor)/2*altura
    @multimethod
    def Area(self, lado:float,apotema:int):
        perimetro=lado*5
        return (perimetro*apotema)/2
f = FiguraGeometrica()
f1 = f.Area(6.3)  # Círculo
f2 = f.Area(12,18)  # Rectángulo
f3 = f.Area(6.0,4.0)#triangulo rectangulo
f4 = f.Area(8.0,6.0,4.0)#trapecio
f5 = f.Area(4.5,4)#pentagono
print("El área del círculo es de:", f1)
print("El área del rectángulo es de:", f2)
print("El area del triangulo rectangulo es de :",f3)
print("El area del trapecio es de :",f4)
print("EL area del pentagono es de :",f5)
