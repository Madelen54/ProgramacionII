class Observador:
    def actualizar(self, temperatura):
        pass
class EstacionClima:
    def __init__(self):
        self.observadores = []
        self.temperatura = 0

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self):
        for o in self.observadores:
            o.actualizar(self.temperatura)

    def cambiar_temperatura(self, nueva_temp):
        self.temperatura = nueva_temp
        self.notificar()

class Pantalla(Observador):
    def actualizar(self, temperatura):
        print(f"Pantalla actualizada: temperatura = {temperatura}°C")

clima = EstacionClima()
pantalla = Pantalla()

clima.agregar_observador(pantalla)
clima.cambiar_temperatura(25)

