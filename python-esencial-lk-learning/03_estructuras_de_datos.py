#ESTRUCTURAS DE DATOS
print('...Estructuras de datos...')

#Listas
print('...Listas...')
lenguajes = ['python', 'java', 'golang']
print(lenguajes)
print(lenguajes[1])
lenguajes.append("typescript")
print(lenguajes)

lista = [1, "apple", 1.58, True]
print(lista)

print(len(lista)) #imprimir la lista
print(lista[-2]) #imprimir elemento orden inverso, indice negativo, comienza del ultimo al primero
print(lista[2]) #imprimir elemento en posicion 3
print(lista[0:2]) #imprimir dos elemntos desde la posicion 0

#lista anidada
print("Lista anidada")
anidada = [lista, lenguajes,"importante"] #dos listas y agrego un string a la nueva lista
print(anidada)


#Tuplas
print('...Tuplas...') #no se pueden modificar sus elementos son inmutables

lenguajes_tuplas = ("python", "C", "C++", "typescript") # tambien se pueden declarar en ()
print(lenguajes_tuplas)
print(lenguajes_tuplas[1]) 
print(lenguajes_tuplas[-1]) #imprimir ultima elemento
#lenguajes_tuplas[0]= "java" no se puede modificar los elementos, duplas son inmutables


#Diccionarios
print('...Diccionarios...') #similar a los JSON

lenguajes ={
   "nombre": "python",
   "creador": "Guido"
}  

print(lenguajes)
print(lenguajes["nombre"])
lenguajes["anio_lanzamiento"] = 1991
print(lenguajes)
lenguajes["caracteristicas"] = ["sencillo", "facil", "genial"]
print(lenguajes["caracteristicas"])
print(lenguajes.items())
print(lenguajes.keys())
print("values...")
print(lenguajes.values())


#Sets
print('...Sets...') #Sets -> No permite valores repetidos, solo valores unicos

set1 = {1,2,3,4,5}
print(set1)
set2 ={1,1,1,2,2} #omite los valores repetidos
print(set2)
set3 = {1, 2,57, "Hola", True}
print(set3)
set1.add(6) #agregar elemento a un set
print(set1)
set1.update([5,6,7,8])
print(set1)
print(len(set1)) #mirar la cantidad de elmentos que tiene el set
set1.discard(3) #eliminar un elmento del set, se hace por valor no por llave
print(set1)
set1.remove(2) #eliminar un elemnto del set, se hace por valor no por llave, si no existe nos envia error
print(set1)
set1.clear() #deja vacio el set, lo limpia
print(set1)