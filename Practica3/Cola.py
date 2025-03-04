class Cola:
    def __init__(self,n):
        self.__arreglo=[0]*(n+1)
        self.__inicio=0
        self.__fin=0
        self.__n=n
    def insert(self,e):
        if(self.__fin==self.__n):
            print("cola llena")
        else:
            self.__fin=self.__fin+1
            self.__arreglo[self.__fin]=e
# remove elimina datos de la cola
    def remove(self):
        if(self.__inicio==0 and self.__fin==0):
            print("cola vacia")
            return None
        else:
            self.__inicio=self.__inicio+1
            dato=self.__arreglo[self.__inicio]
            if(self.__inicio==self.__fin):
                self.__inicio=0
                self.__fin=0
            return dato
    def peek(self):
        return self.__arreglo[self.__inicio+1]
    def isEmpty(self):
        if(self.__inicio==0 and self.__fin==0):
            return True
        else:
            return False
    def isFull(self):
        if(self.__fin==self.__n):
            return True
        else:
            return False
    def size(self):
        return self.__n
q=Cola(12)

q.insert(10)
q.insert(20)
q.insert(110)
print("el tamaño de la cola es de ",q.size())
aux=Cola(12)
while(not q.isEmpty()):
    dato= q.remove()
    aux.insert(dato)
    print(dato,end=" ")
while(not aux.isEmpty()):
    dato=aux.remove()
    q.insert(dato)
print(aux.isFull())
