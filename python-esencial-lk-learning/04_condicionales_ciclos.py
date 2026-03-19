#CONDICIONALES
print("...CONDICIONALES...")
print("...IF..")

#if
a = 1
b = 2

if a > b:
  print('A es mayor que B')
elif a == b: 
  print('A es igual a B')
else:
  print('A es menor que B')

c = True

if a:
  print("A es verdadero")
else:
  print("A es falso")

#FOR
print("...FOR..")

for letra in "Kaminando":
  print(letra)


lenguajes = ["python", "java", "javascript"]
  
for lenguaje in lenguajes:
  print(lenguaje)
  if lenguaje == "java":  #imprime sale del ciclo
    break
  
for lenguaje in lenguajes:
  if lenguaje == "java": #cuando sea igual a java no lo imprime, continua con el siguiente ciclo
    continue
  print(lenguaje)


for element in range(4,10): #imprime elementos del 4 al 9, el ultimo no lo incluye
  print(element)


#WHILE
print("...WHILE..")

i = 1 
while i <= 5:
  print(i)
  i += 1

i = 1
while i <= 5:
  print(i)
  i += 1
  if i == 3:
    break


#Iterando sobre una lista
print("...ITERANDO SOBRE UNA LISTA...")

lenguajes = ['python', 'java', 'golang']
print(lenguajes)
print(lenguajes[1])

#Iterando sobre una lista con for
for index in range(len(lenguajes)):
  print("indidce", index)
  print("elemento", lenguajes[index])

#iterando sobre una lista con while
i = 0
longitud = len(lenguajes)

while i < longitud:
  print(lenguajes[i])
  i += 1

#Iterando sobre un diccionario
print("...ITERANDO SOBRE UN DICCIONARIO...")

lenguajes ={
   "nombre": "python",
   "creador": "Guido van Rossum"
}  

for llave in lenguajes:
  print("llave:", llave)
  print("valor:", lenguajes[llave])

for elemento in lenguajes.items():
  print(elemento)