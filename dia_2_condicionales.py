
#CONDICIONALES

#permite decidir qué hacer según una condición mediante palabras reservadas.
# EN PY son if / elif / else
#if → palabra reservada, significa "si"

#Si la condición es True, se ejecuta lo de adentro. Si es False, simplemente se salta ese bloque y sigue de largo.
#Operadores de comparación (el corazón de la condición)
#Operador...Significado

#   == es igual a       diferente de asignar  =
#   !=  es diferente de 
#   > mayor que
#   < menor que
#   >= mayor o igual que
#   <= menor o igual que

#ejemplos IF

edad = 12
if edad<= 18:
    print ("usted es menor de edad")

esta_haciendo_calor =  True
if esta_haciendo_calor:
    print("usa bloquiador solar")

# para unir dos variables

edad = 33
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
    
#  else — que es literalmente "y si no se cumple, haz esto otro" 

edad = 32

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


esta_haciendo_calor =  False
if esta_haciendo_calor:
    print("usa bloquiador solar")
else:
    print("lleva paraguas")


esta_haciendo_calor =  True
if esta_haciendo_calor:
    print("usa bloquiador solar")
else:
    print("lleva paraguas")


# con dos o mas variables
   
age = 11
tiene_licencia = True

if age >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print(" deberias estar en la escuela")

age = 23
tiene_licencia = False

if age >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print(" deberias estar en la escuela")

age = 33
tiene_licencia = True

if age >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print(" deberias estar en la escuela")

# elif — cuando hay más de dos caminos posibles
# Hasta ahora con if/else solo puedes decidir entre dos opciones: esto, o lo contrario. 
# Pero muchas veces necesitas más de dos caminos. Ahí entra elif (que es la forma corta de decir "else if" — "si no, entonces si...").

nota = 77

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")



nota = 33

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")



nota = 81

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")


nota = 91

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")