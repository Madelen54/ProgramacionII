class Pila:
    def __init__(self, n):
        self.__arreglo = [0] * (n + 1)
        self.__n = n
        self.__top = 0

    def push(self, e):
        if self.__top == self.__n:
            print("Pila llena")
        else:
            self.__top += 1
            self.__arreglo[self.__top] = e

    def pop(self):
        if self.__top == 0:
            print("Pila vacía")
            return None  
        else:
            dato = self.__arreglo[self.__top]
            self.__top -= 1
            return dato  

    def peek(self):
        if self.__top == 0:
            print("Pila vacía")
            return None
        return self.__arreglo[self.__top]

    def isEmpty(self):
        return self.__top == 0

    def isFull(self):
        return self.__top == self.__n
p = Pila(8)
p.push(40)
p.push(86)
p.push(68)
p.push(637)

print(p.pop())  
print(p.peek())
print("¿La pila está llena?", p.isFull())
print("¿La pila está vacía?", p.isEmpty())
