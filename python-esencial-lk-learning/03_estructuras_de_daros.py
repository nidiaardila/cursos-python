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


#Diccionarioa
print('...Diccionarios...') 