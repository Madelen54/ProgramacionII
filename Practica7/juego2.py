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
            self.numero_de_vidas -= 1  # Resta una vida
            return True
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas, record):
        super().__init__(numero_de_vidas, record)
        self.numero_a_adivinar = None

    def valida_numero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)

        print("Adivina el número entre 0 y 10")

        while self.numero_de_vidas > 0:
            try:
                numeroa = int(input("Ingresa tu adivinanza: "))

                if not self.valida_numero(numeroa):
                    print("Error: El número debe estar entre 0 y 10.")
                    continue

                if numeroa == self.numero_a_adivinar:
                    print("¡Acertaste!!")
                    self.actualiza_record(self.numero_a_adivinar)
                    break
                else:
                    if self.quita_vida():

                        if numeroa < self.numero_a_adivinar:
                            print("El número a adivinar es mayor al que diste.")
                        else:
                            print("El número a adivinar es menor al que diste.")
                        print("¡Inténtalo de nuevo!")
                    else:
                        print("Ya no tienes vidas. ¡Game Over!")
                        break
            except ValueError:
                print("Por favor ingresa un número válido.")
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        else:
            if numero % 2 != 0:
                print("Error: El número debe ser par.")
            elif not (0 <= numero <= 10):
                print("Error: El número debe estar entre 0 y 10.")
            return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        else:
            if numero % 2 == 0:
                print("Error: El número debe ser impar.")
            elif not (0 <= numero <= 10):
                print("Error: El número debe estar entre 0 y 10.")
            return False
def main():
    juego_numero = JuegoAdivinaNumero(3, 10)
    juego_par = JuegoAdivinaPar(3, 10)
    juego_impar = JuegoAdivinaImpar(3, 10)
    print("\n** Juego Adivina Número **")
    juego_numero.juega()

    print("\n** Juego Adivina Par **")
    juego_par.juega()

    print("\n** Juego Adivina Impar **")
    juego_impar.juega()

if __name__ == "__main__":
    main()
