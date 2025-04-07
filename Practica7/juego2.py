import random

class Juego:
    def __init__(self, numeroDevidas, record):
        self.__numeroDevidas = numeroDevidas
        self.__record = record

    def reinicia_partida(self):
        self.__numeroDevidas = 3
        return self.__numeroDevidas

    def obtener_record(self):
        return self.__record

    def actualiza_record(self, nuevo_record):
        if nuevo_record > self.__record:
            self.__record = nuevo_record

    def quita_vida(self):
        if self.__numeroDevidas == 0:
            return False
        else:
            self.__numeroDevidas -= 1
            return True

    def obtener_vidas(self):
        return self.__numeroDevidas

    def set_vidas(self, vidas):
        if vidas >= 0:
            self.__numeroDevidas = vidas

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDevidas, record):
        super().__init__(numeroDevidas, record)
        self.__numeroAAdivinar = None

    def valida_numero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reinicia_partida()
        self.__numeroAAdivinar = random.randint(0, 10)

        print("Adivina el numero entre 0 y 10")

        while self.obtener_vidas() > 0:
            try:
                numeroa = int(input("Ingresa tu numero: "))

                if not self.valida_numero(numeroa):
                    print("Error: El numero debe estar entre 0 y 10.")
                    continue

                if numeroa == self.__numeroAAdivinar:
                    print("¡Acertaste!!")
                    self.actualiza_record(self.__numeroAAdivinar)
                    break
                else:
                    if self.quita_vida():
                        if numeroa < self.__numeroAAdivinar:
                            print("El numero a adivinar es mayor al que diste.")
                        else:
                            print("El numero a adivinar es menor al que diste.")
                        print("¡Intentalo de nuevo!")
                    else:
                        print("¡Game Over!")
                        break
            except ValueError:
                print("Por favor ingresa un numero valido.")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        else:
            if numero % 2 != 0:
                print("Error: El numero debe ser par.")
            elif not (0 <= numero <= 10):
                print("Error: El numero debe estar entre 0 y 10.")
            return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        else:
            if numero % 2 == 0:
                print("Error: El numero debe ser impar.")
            elif not (0 <= numero <= 10):
                print("Error: El numero debe estar entre 0 y 10.")
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