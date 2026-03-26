#clase con constructor sin parametros
class Animal:
    def __init__(self): #__init__ es el constructor y self es el objeto this 
        print("Estoy en el constructor")

Snoopy = Animal()


#clase con constructor con parametros
class Persona:
    reino = "animal"

    def __init__(self, nombre, edad): #__init__ es el constructor y self es el objeto this 
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print("Feliz cumpleaños: ", self.edad, "Hola ", self.nombre)
        #print(f"Feliz cumpleaños: # {self.edad} {self.nombre}")


paco = Persona("Paco", 20)

print(paco.nombre)
print(paco.edad)
print(paco.reino)

jose = Persona ("Jose", 23)
jose.cumplir_anios()

