# Condicional If

dia = input("¿Que día es hoy?: ")

# if(dia == "Lunes"):
#   print("Hoy tengo clase de Python")
# elif(dia == "Martes"):
#   print("Hoy tenes after class")
# else:
#   print("Hoy no hay clases")

match dia:
  case "Lunes":
    print("Hoy tengo clases de Python")
  case "Martes":
    print("Hoy tengo after class")
  case "Miércoles":
    print("NO hay clases")
  case "Jueves":
    print("NO hay clases")
  case "Viernes":
    print("NO hay clases")
  case "Sábado":
    print("NO hay clases")
  case "Domingo":
    print("NO hay clases")

nombre = input("Ingresa tu nombre: ")
if(nombre == ""):
  print("No ingresaste ningún dato")
else:
  print("Hola", nombre)

  ##########

  texto = "Hola, hoy es lunes"

print(texto.capitalize())
