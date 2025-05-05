class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    def incrementaxz(self):
        self.x += 1
        self.z += 1
    def incrementaz(self):
        self.z += 1

class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z
    def incrementayz(self):
        self.y += 1
        self.z += 1
    def incrementaz(self):
        self.z += 1

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)
    def incrementaxyz(self):
        self.x += 1
        self.y += 1
        self.z += 1
    def mostrar(self):
        print(f"x:{self.x}, y:{self.y}, z:{self.z}")

objeto = D(9, 12, 4)
objeto.incrementaxyz()
objeto.mostrar()
objeto.incrementayz()
objeto.mostrar()
