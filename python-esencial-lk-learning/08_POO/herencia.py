class Persona:
    def __init__(self, nombre, edad): #__init__ es el constructor y self es el objeto this 
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print("Feliz cumpleaños: ", self.edad, " ", self.nombre)

class Empleado(Persona):
    def __init__(self, nombre, edad, horas_totales):
        super(Empleado, self).__init__(nombre, edad)
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print("Hoy, has trabajado ", horas_trabajadas, " horas")
        print("En total has trabajado", self.horas_totales)

paco = Empleado("Paco", 20, 500)
paco.trabajar(7)
paco.cumplir_anios()
       