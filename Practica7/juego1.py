class Juego:
    def __init__(self, numero_de_vidas, record):
        self.numero_de_vidas = numero_de_vidas
        self.record = record

    def reinicia_partida(self):
        self.numero_de_vidas = 3
        return self.numero_de_vidas

    def obtener_record(self):
        return self.record

    def actualiza_record(self, nuevo_record):
        if nuevo_record > self.record:
            self.record = nuevo_record

    def quita_vida(self):
        if self.numero_de_vidas == 0:
            return False
        else:
            self.numero_de_vidas -= 1
            return True
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas, record):
        super().__init__(numero_de_vidas, record)
        self.numero_a_adivinar = None

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)

        print("Adivina el número entre 0 y 10")

        while self.numero_de_vidas > 0:
            numero = int(input("Ingresa tu numero: "))

            if numero == self.numero_a_adivinar:
                print("¡Acertaste!!")
                self.actualiza_record(self.numero_a_adivinar)
                break
            else:
                if self.quita_vida():

                    if numero < self.numero_a_adivinar:
                        print("El numero a adivinar es mayor al que diste.")
                    else:
                        print("El numero a adivinar es menor al que diste.")
                    print("¡Intentalo de nuevo!")
                else:
                    print("¡Game Over!")
                    break  
def main():
    juego = JuegoAdivinaNumero(3,12)
    juego.juega()

if __name__ == "__main__":
    main()
