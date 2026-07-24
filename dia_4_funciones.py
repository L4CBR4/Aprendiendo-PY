# Funciones — organizar código en bloques reutilizables
#Hasta ahora, si quisieras calcular el área de un rectángulo en 3 lugares distintos de tu código, 
# tendrías que escribir la misma fórmula 3 veces. Una función te permite escribirla una sola vez, 
# ponerle un nombre, y usarla ("llamarla") todas las veces que quieras.

def saludar():
    print("Hola, bienvenido a Python")

saludar()
saludar()

def ayuda():
    print("que necesitas?")

ayuda()

#Parámetros — funciones que reciben datos

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Camila")
saludar("Lucho")
saludar("Maria")
saludar("David")
saludar("Julieta")
saludar("Lucia")

def variable(a, b):
    print(a * b)

variable(3, 4)
variable(10, 20)

# función que pide los datos ella misma

#sin parametros

def sumar():
    a = input("Escribe el primer número: ")
    a = int(a)
    b = input("Escribe el segundo número: ")
    b = int(b)
    print(f"La suma es: {a + b}")

sumar()
#con parametros

def sumar(a, b):
    print(f"La suma es: {a + b}")

num1 = input("Escribe el primer número: ")
num1 = int(num1)
num2 = input("Escribe el segundo número: ")
num2 = int(num2)

sumar(num1, num2)


def resta(a, b):
    print(f"La resta es: {a - b}")

num3 = input("Escribe el primer número: ")
num3 = int(num3)
num4 = input("Escribe el segundo número: ")
num4 = int(num4)

resta(num3, num4)

#return — hacer que una función te devuelva un valor

#Hasta ahora, tus funciones imprimen el resultado directamente adentro (print(a + b)).
#  Eso funciona, pero tiene una limitación importante: 
#el resultado se muestra en pantalla y ya, no lo puedes reutilizar después en tu código.

#return es distinto: en vez de mostrar el resultado, la función te lo entrega de vuelta, para que hagas lo que quieras con él.


def resta(a, b):
    return a - b

resultado = resta(7, 2)
print(resultado)
triple = resultado * 3
print(triple)



def sumar(a, b):
    return a + b

num1 = input("Escribe el primer número: ")
num1 = int(num1)
num2 = input("Escribe el segundo número: ")
num2 = int(num2)

resultado = sumar(num1, num2)
print(f"La suma es: {resultado}")
triple = resultado * 3
print(f"el triple de tu numero es: {triple}")


