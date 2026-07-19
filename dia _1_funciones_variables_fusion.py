#funciones...
#cadenas de texto
print("hello py")
print("Estoy creando mis orimeras lineas de codigo")
print("py es el mejor")
#operaciones matematicas basicass
print(8+2)
print(8-5)
print(34*6)
print(10//2)
#variables...
#Es una caja con nombre donde guardas un valor para reutilizarlo después, sin tener que escribirlo de nuevo cada vez.

nombre = "camila"
edad = 32
fruta = "fresa"
animal = "fenix"
color = "amarillo"
casa = 23
corresponsal = 369

print(nombre)
print(edad)
print(fruta)
print(animal)
print(color)
print(casa)
print(corresponsal)

#fusion de variables...

#concatenación con +

print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años")
print("vivo en el " + str(corresponsal) + " y me encanta la " + (fruta))
print("El numero de mi casa es el " + str(casa) + " y tengo un " + animal)



#Con f-string

print(f"Mi nombre es {nombre} y tengo {edad} años")
print(f"vivo en el {corresponsal} y me encanta la  {fruta}" )
print(f"el numero de mi casa es el  {casa} y tengo un  {animal}" )

#input() — pedirle algo al usuario

nombre = input("¿Cómo te llamas? ")
print(f"Mucho gusto, {nombre}")

age = input("¿cual es tu edad? ")
age = int(age)
print(" tu edad es " + str(age + 5) + " años")

#Resolucion de ejercicios
# crea un saludo debe devolver "hola py"


lenguaje = "py"

print("hola " + lenguaje + " encantado de poder practicar contigo " )
print(f"hola {lenguaje} mucho gusto en conocerte" )

# crea un ejercicio que te permita sumar numeros

a = 7
b = 5
c = 15
print(a + b + c)

#Pide el nombre y la edad al usuario con input(), y muestra: "Hola <nombre>, el próximo año tendrás <edad+1> años".

nombre = input("escribe tu nombre por favor ")
print(f"hola, {nombre}")
edad= input("¿cual es tu edad? ")
edad = int(edad)
print(" el otro año tendras " + str(edad + 1) + " años")

#Crea variables base y altura con números que tú elijas, calcula el área (base * altura) y muéstrala con un f-string.


base = 18
altura = 15
print(f" el area de este triangulo es " + str(base*altura))

#Pide al usuario una temperatura en Celsius con input() (recuerda convertir a número), y calcula Fahrenheit: F = C * 9/5 + 32. Muestra el resultado.

temperatura = input("escribe a que temperatura celsius estas en el momento ")
temperatura = int(temperatura)
print(" en este momento te encuentras a  " + str(temperatura * 9/5 + 32) + " grados Fahrenheit ")

#¿Par o impar? (sin condicionales, solo mostrando el resto)
#Pide un número al usuario, y muestra el resultado de numero % 2 (0 significa par, 1 significa impar) — solo describe qué significa en un print, aún no usamos if.

num = input("escribe un numero ")
num = int(num)
print(" tu numero es " + str(num % 2))
print(f"El resto de dividir {num} entre 2 es {num % 2} (0 = par, 1 = impar)")

#Pide dos números al usuario (con input() + int()), y muestra su suma, resta, multiplicación y división,
#  cada una en su propio print.

num_a = input("escribe un numero ")
num_a= int(num_a)
num_b = input("escribe un numero ")
num_b = int(num_b)
print(f"la suma de tus numeros es {num_a + num_b}")
print(f"la resta de tus numeros es {num_a - num_b}")
print(f"la multiplicacion de tus numeros es {num_a * num_b}")
print(f"la division de tus numeros es {num_a // num_b}")

# Crea una variable precio y una descuento (por ejemplo 20 = 20%), calcula el precio final: precio - (precio * descuento / 100),
#  y muéstralo con f-string.

precio = 752000
descuento = 22
print(f"el descuento que se aplica a este producto es de  {precio * descuento / 100}")
print(f"usted debe pagar {precio - (precio * descuento / 100)}")

