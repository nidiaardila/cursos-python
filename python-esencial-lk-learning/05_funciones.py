
# Definimos una función para calcular el perímetro de un cuadrado
# 'lado' espera un número y 'unidades' espera un texto (string)
def perimetro_cuadrado(lado, unidades):
  perimetro = lado * 4 
  
   # Usamos una f-string para mostrar el resultado formateado
  # Las llaves { } insertan el valor de las variables directamente en el texto
  print(f"El perimetro es {perimetro} {unidades}") #imprimir formateado

  print("El perimetro es", perimetro, unidades) #imprimir forma mas sencilla

perimetro_cuadrado(25, "metros")


#Retorno de valores de una funcion y Documentacion de la funcion
def perimetro_cuadrado(lado):
  """Calcular el perimetro de un cuadrado
  
  ESta funcion recibe el valor de un lado de un cuadrado y a partir de esto calcula  y retorna
  su perimetro

  Args:
    lado (int): medida del lado del cuadrado

  Returns:
    perimetro (int): retorna el perimetro del cuadrado  
  """
  perimetro = lado * 4
  return perimetro

def area_cuadrado(lado):
  area = lado * lado
  return area

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)

print("Area: ", area, "Perimetro: ", perimetro)  

#Funcion con retorno multiple, Asignar la misma funcion a dos variables, area y perimetro
def calcular_cuadrado(lado):
  perimetro = lado * 4
  area = lado * lado
  return area, perimetro

area, perimetro = calcular_cuadrado(lado=5)

print("Area: ", area, "Perimetro: ", perimetro)  

