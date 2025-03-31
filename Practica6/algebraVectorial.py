import math
#30/03/25
#Escarlet Zapana

class AlgebraVectorial:
    def __init__(self, v=None):
        self.v = v

    def perpendicular(self, o):
        return self.producto_punto(o) == 0

    def producto_punto(self, o):
        if len(self.v) != len(o.v):
            return f"Los vectores deben tener la misma longitud"

        resultado = 0
        for i in range(len(self.v)):
            resultado += self.v[i] * o.v[i]
        return resultado

    def paralela(self, o):
        return self.producto_cruzado(o) == 0

    def producto_cruzado(self, o):
        i1 = self.v[1] * o.v[2] - o.v[1] * self.v[2]
        j1 = self.v[0] * o.v[2] - o.v[0] * self.v[2]
        k1 = self.v[0] * o.v[1] - o.v[0] * self.v[1]

        return i1 - j1 + k1

    def proyeccion(self, o):
        producto_punto = self.producto_punto(o)
        modulo_cuadrado = o.producto_punto(o)
        escala = producto_punto / modulo_cuadrado
        proyeccion = [escala * x for x in o.v]
        return proyeccion

    def componente(self, o):
        return self.producto_punto(o) / math.sqrt(o.producto_punto(o))

    def __str__(self):
        return f"[{', '.join(map(str, self.v))}]"
if __name__ == "__main__":
    v1 = [3.2, 5.0, 7.8]
    v2 = [7.3, -1.6, 2.9]

    vector1 = AlgebraVectorial(v1)
    vector2 = AlgebraVectorial(v2)

    print("Son perpendiculares (ortogonales):", vector1.perpendicular(vector2))
    print("Son paralelos:", vector1.paralela(vector2))

    p = vector1.proyeccion(vector2)
    print("Proyección de v1 sobre v2:", p)

    c = vector1.componente(vector2)
    print("Componente de v1 en la dirección de v2:", c)
