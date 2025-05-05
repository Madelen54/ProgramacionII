from multimethod import multimethod
class LineaTeleferico:

    def __init__(self, color="", tramo="", nroCabinas=0,nroEmpleados=4):  
        self.__color = color
        self.__tramo = tramo
        self.__nroCabinas = nroCabinas
        self.__nroEmpleados = nroEmpleados
        self.__empleados = [["pedro", "rojas", "luna"],
                            ["lucy", "sosa", "rios"],
                            ["ana", "perez", "rojas"],
                            ["saul", "arce", "calle"]]
        self.__edades = [35, 43, 26, 29]
        self.__sueldos = [2500.0, 3250.0, 2700.0, 2500.0]

    def __str__(self):
        cad = f"Color: {self.__color}, Tramo: {self.__tramo}, nroCabinas: {self.__nroCabinas}, nroEmpleados: {self.__nroEmpleados}\n"
        cad = cad + " Empleados: \n"
        for i in range(len(self.__empleados)):
            cad = cad + f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        return cad

        def eliminarPorApellido(self, x):
        rango = len(self.__empleados)
        for i in range(rango - 2):
            if ((self.__empleados[i])[1] == x or (self.__empleados[i])[
                2] == x):  # se usa or por que asi lo especifica el problema
                self.__empleados.pop(i)
                self.__edades.pop(i)
                self.__sueldos.pop(i)
                self.__nroEmpleados -= 1

    def __add__(self, parametros):
        otro, x = parametros
      
        if (isinstance(otro, LineaTeleferico)):
            for i in range(len(self.__empleados)):
                if ((self.__empleados[i])[0] == x):
                    nombre = (self.__empleados[i])[0]
                    paterno = (self.__empleados[i])[1]
                    materno = (self.__empleados[i])[2]
                    otro.__empleados.append([nombre, paterno, materno])
                    otro.__edades.append(self.__edades[i])
                    otro.__sueldos.append(self.__sueldos[i])
                    self.__empleados.pop(i)
                    self.__edades.pop(i)
                    self.__sueldos.pop(i)
                    self.__nroEmpleados -= 1
                    otro.__nroEmpleados += 1
                    break
        return otro
    def mayorEdad(self): 
        mayor = 0
        for i in range(len(self.__empleados)):
            if (self.__edades[i] > mayor):
                mayor = self.__edades[i]
        return mayor

    def mayorSueldo(self):
        mayor = 0.0
        for i in range(len(self.__empleados)):
            if (self.__sueldos[i] > mayor):
                mayor = self.__sueldos[i]
        return mayor
    @multimethod
    def mostrar(self, e: int):  
        cad = "Empelados con mayor edad: \n"
        for i in range(len(self.__empleados)):
            if (self.__edades[i] == e):
                cad = cad + f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)

    @multimethod
    def mostrar(self, s: float): 
        cad = "Empelados con mayor sueldo: \n"
        for i in range(len(self.__empleados)):
            if (self.__sueldos[i] == s):
                cad = cad + f"Nombre: {(self.__empleados[i])[0]} {(self.__empleados[i])[1]} {(self.__empleados[i])[2]}, Edad: {self.__edades[i]} sueldo: {self.__sueldos[i]}\n"
        print(cad)
    class main():
    t1 = LineaTeleferico("rojo", "estacion central, estacion cementerio, estacion 16 de julio", 20, 4)
    t2 = LineaTeleferico()
    print("primer teleferico: ")
    print(t1)
    print("segundo teleferico: ")
    print(t2)
    t1.eliminarPorApellido("rojas")
    print(t1)
    print(t1 + (t2, "saul")) 
    mayorEdad = t1.mayorEdad()
    t1.mostrar(mayorEdad)  
    maySueldo = t1.mayorSueldo()
    t1.mostrar(maySueldo) 
