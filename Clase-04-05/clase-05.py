# Bucle While (mientras)

# contador = 1
# while contador <= 5:
#   print(f"Este es el intento número {contador}")
#   contador +=1
  
# nombre = ""
# while nombre == "":
#   nombre = input("Ingresá tu nombre: ").strip()
#   if nombre == "":
#     print("El nombre no puede estar vacío. Intentá de nuevo.")
# print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")

# Break y Continue
numero = 200
numeros = [10, 20, 30, 40, 50]
cantidad = len(numeros)
# len -> cantidad total de caracteres / valores
print(len(numeros))

contador = 0
while contador < cantidad:
  print(f"El numero {numeros[contador]} esta en la posicion {contador}")
  if(numeros[contador] < 0):
    # break
    continue
  contador = contador + 1
  
productos = ["manzanas", "bananas", "peras", "frutillas"]

for producto in productos:
  print("Productos disponibles:", producto)