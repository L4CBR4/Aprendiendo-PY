#Cerrando funciones — las piezas que faltaban
# Parámetros con valor por defecto
#A veces quieres que un parámetro tenga un valor "de repuesto" si no se lo pasan explícitamente:

def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar("Camila")   # Hola, Camila!
saludar()            # Hola, invitado!   (no le pasaste nada, usa el valor por defecto)

#*args — recibir una cantidad variable de argumentos 
# Hasta ahora tus funciones tenían un número fijo de parámetros (a, b). Pero,
#¿qué pasa si quieres sumar 2 números a veces,
#y 5 números otras veces, sin escribir una función distinta para cada caso?

def sumar_todo(*numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total

print(sumar_todo(1, 2))          # 3
print(sumar_todo(1, 2, 3, 4, 5)) # 15
print(sumar_todo(9, 5, 3, 7)) # 24


#El * antes de numeros le dice a Python: "junta todos los argumentos que me pasen,
#  sin importar cuántos sean, en una sola cosa llamada numeros

#Scope (alcance) — dónde "vive" cada variable

def crear_lista():
    mi_lista = [1, 2, 3]
    print(mi_lista)

crear_lista()

 #print(mi_lista)   # ¡ERROR! mi_lista no existe aquí afuera