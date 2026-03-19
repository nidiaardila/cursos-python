
# Definimos una función para calcular el perímetro de un cuadrado
# 'lado' espera un número y 'unidades' espera un texto (string)
def perimetro_cuadrado(lado, unidades):
  perimetro = lado * 4 
  
   # Usamos una f-string para mostrar el resultado formateado
  # Las llaves { } insertan el valor de las variables directamente en el texto
  print(f"El perimetro es {perimetro} {unidades}") #imprimir formateado

  print("El perimetro es", perimetro, unidades) #imprimir forma mas sencilla

perimetro_cuadrado(25, "metros")

