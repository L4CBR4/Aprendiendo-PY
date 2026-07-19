#Bucles — for y while
#¿Qué problema resuelven?
#Hasta ahora, si quisieras mostrar los números del 1 al 5, tendrías que escribir 5 print() distintos. 
# Un bucle te permite repetir una acción sin copiar y pegar código.

#for — repetir un número conocido de veces



#Recorrer un rango con inicio y fin personalizados
for numero in range(10):
    print(numero)


# Con un "salto" (tercer parámetro de range
for numero in range(0, 10, 2):
    print(numero)


#Recorrer directamente el texto de un string
palabra = "python"
for letra in palabra:
    print(letra)


#Acumular un resultado usando un bucle (muy común)
suma = 0
for numero in range(1, 6):
    suma = suma + numero
print(suma)

#Usando la variable del bucle dentro de un cálculo

for numero in range(1, 6):
    print(numero * numero)


#while — repetir MIENTRAS algo sea verdadero
#A diferencia de for (que repite un número conocido de veces,
# gracias a range()), while repite mientras una condición sea True 
# — sin saber de antemano cuántas veces será exactamente.

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
    respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe un número, o 'salir' para terminar: ")
    if respuesta != "salir":
        print(f"Escribiste: {respuesta}")

print("Programa terminado")


#break — corta el bucle por completo, de inmediato

for numero in range(10):
    if numero == 5:
        break
    print(numero)

#continue — se salta SOLO esta vuelta, y sigue con la siguiente


for numero in range(10):
    if numero == 5:
        continue
    print(numero)