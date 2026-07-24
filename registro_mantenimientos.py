#ESTE ES EL PROGRMA DEFINITIVO PARA REGISTRAR ACTIVIDADES DIARIAS DE PROCESOS EN UNA FLOTA DE TRANSPORTE

# ============================================================
# FUNCIONES DE VALIDACION
# ============================================================



def pedir_id_tecnico():
    while True:
        id_tecnico = input("Ingrese su ID de tecnico (letras y numeros): ")
        if id_tecnico.isalnum():
            return id_tecnico
        else:
            print("ID invalido. Solo se permiten letras y numeros, sin espacios ni simbolos.\n")


def pedir_placa():
    while True:
        placa = input("Placa del vehiculo (letras y numeros): ")
        if placa.isalnum():
            return placa
        else:
            print("Placa invalida. Solo se permiten letras y numeros.\n")


def pedir_fecha():
    while True:
        fecha = input("Fecha (formato AAAA-MM-DD): ")
        valido = True
        for caracter in fecha:
            if not (caracter.isdigit() or caracter == "-" or caracter == "/"):
                valido = False
        if valido and fecha != "":
            return fecha
        else:
            print("Fecha invalida. Solo se permiten numeros, guiones (-) o barras (/).\n")


def pedir_tipo_mantenimiento():
    while True:
        tipo = input("Tipo de mantenimiento (mecanico/electrico/carroceria): ")
        tipo = tipo.lower()
        if tipo in ["mecanico", "electrico", "carroceria"]:
            return tipo
        else:
            print("Tipo invalido. Debe ser: mecanico, electrico o carroceria.\n")


def pedir_motivo():
    while True:
        motivo = input("Motivo principal de la intervencion (solo letras): ")
        valido = True
        for caracter in motivo:
            if not (caracter.isalpha() or caracter == " "):
                valido = False
        if valido and motivo != "":
            return motivo
        else:
            print("Motivo invalido. Solo se permiten letras y espacios.\n")


def pedir_kilometraje():
    while True:
        km = input("Kilometraje actual del vehiculo (solo numeros): ")
        if km.isdigit():
            return int(km)
        else:
            print("Kilometraje invalido. Solo se permiten numeros.\n")


def pedir_texto_alfanumerico(mensaje):
    while True:
        texto = input(mensaje)
        valido = True
        for caracter in texto:
            if not (caracter.isalnum() or caracter == " "):
                valido = False
        if valido and texto != "":
            return texto
        else:
            print("Texto invalido. Solo se permiten letras, numeros y espacios.\n")


# ============================================================
# FUNCIONES DE REGISTRO
# ============================================================

def pedir_trabajos_realizados():
    trabajos = []
    while True:
        componente = input("Componente trabajado (o escribe 'fin' para terminar): ")
        if componente.lower() == "fin":
            break
        repuesto = pedir_texto_alfanumerico("Repuesto utilizado: ")
        diagnostico = pedir_texto_alfanumerico("Diagnostico / que se hizo: ")
        trabajo = {"componente": componente, "repuesto": repuesto, "diagnostico": diagnostico}
        trabajos.append(trabajo)
        print("Trabajo agregado correctamente.\n")
    return trabajos


def pedir_pendientes():
    pendientes = []
    while True:
        componente = input("Componente con novedad pendiente (o escribe 'fin' para terminar): ")
        if componente.lower() == "fin":
            break
        recomendacion = pedir_texto_alfanumerico("Recomendacion / que se debe revisar despues: ")
        pendiente = {"componente": componente, "recomendacion": recomendacion}
        pendientes.append(pendiente)
        print("Pendiente agregado correctamente.\n")
    return pendientes


def registrar_mantenimiento():
    id_tecnico = pedir_id_tecnico()
    placa = pedir_placa()
    fecha = pedir_fecha()
    tipo = pedir_tipo_mantenimiento()
    motivo_principal = pedir_motivo()
    km = pedir_kilometraje()

    print("\n--- Registro de trabajos realizados ---")
    trabajos = pedir_trabajos_realizados()

    print("\n--- Registro de pendientes/novedades ---")
    pendientes = pedir_pendientes()

    nuevo_registro = {
        "id_tecnico": id_tecnico,
        "placa": placa,
        "fecha": fecha,
        "tipo": tipo,
        "motivo_principal": motivo_principal,
        "trabajos_realizados": trabajos,
        "pendientes": pendientes,
        "km": km
    }
    return nuevo_registro


# ============================================================
# PROGRAMA PRINCIPAL DEL TECNICO
# ============================================================

registros_del_dia = []

while True:
    nuevo = registrar_mantenimiento()
    registros_del_dia.append(nuevo)
    print("\nRegistro guardado correctamente. Gracias por su reporte.\n")

    continuar = input("¿Otro tecnico desea ingresar un registro? (si/no): ")
    if continuar.lower() != "si":
        break

print(f"\nSesion finalizada. Se registraron {len(registros_del_dia)} mantenimientos.")