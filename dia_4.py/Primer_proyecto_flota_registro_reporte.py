mantenimientos = [
    {
        "id_tecnico": "T045",
        "placa": "SB1234",
        "fecha": "2024-03-15",
        "tipo": "preventivo mecanico",
        "motivo_principal": "cambio de pastillas de freno programado",
        "trabajos_realizados": [
            {"componente": "frenos", "repuesto": "pastillas delanteras", "diagnostico": "desgaste normal por uso"},
            {"componente": "aceite motor", "repuesto": "aceite y filtro", "diagnostico": "cambio segun kilometraje"}
        ],
        "pendientes": [
            {"componente": "discos de freno", "recomendacion": "presentan leve desgaste, revisar en proximo mantenimiento"}
        ],
        "costo_total": 320000,
        "km": 85000
    },
    {
        "id_tecnico": "T045",
        "placa": "SB1234",
        "fecha": "2024-03-15",
        "tipo": "preventivo electrico",
        "motivo_principal": "cambio de alternadores",
        "trabajos_realizados": [
            {"componente": "alternadores", "repuesto": "alternador de flota", "diagnostico": "desgaste normal por uso"},
            {"componente": "extractores", "repuesto": "extractor", "diagnostico": "cambio por daño electrico"}
        ],
        "pendientes": [
            {"componente": "solenoides", "recomendacion": "presentan leve desgaste, revisar en proximo mantenimiento"}
        ],
        "costo_total": 500000,
        "km": 85000
    },
    {
        "id_tecnico": "T045",
        "placa": "SB1234",
        "fecha": "2024-03-15",
        "tipo": "preventivo carroceria",
        "motivo_principal": "bosters puertas de servicio",
        "trabajos_realizados": [
            {"componente": "cambio de empaques", "repuesto": "empaquetadura bosters", "diagnostico": "cambio por tiempo cumplido"},
            {"componente": "caucho sanfona", "repuesto": "caucho, alma, brocas, tornillos y otros", "diagnostico": "cambio por daño evidente"}
        ],
        "pendientes": [
            {"componente": "silla", "recomendacion": "silla con signo de daño"}
        ],
        "costo_total": 620000,
        "km": 85000
        
    }
]

print(mantenimientos)


def mostrar_reporte(lista_mantenimientos):
    for m in lista_mantenimientos:
        print(f"Placa: {m['placa']} | Fecha: {m['fecha']} | Tipo: {m['tipo']}")
        print(f"Motivo principal: {m['motivo_principal']}")
        print(f"Costo: ${m['costo_total']}")
        print("---")

mostrar_reporte(mantenimientos)

def costo_total_flota(lista_mantenimientos):
    total = 0
    for m in lista_mantenimientos:
        total = total + m['costo_total']
    return total

total = costo_total_flota(mantenimientos)
print(f"El costo total de mantenimiento del bus SB1234 fue: ${total}")

def contar_pendientes(lista_mantenimientos):
    total_pendientes = 0
    for m in lista_mantenimientos:
        for pendiente in m['pendientes']:
            total_pendientes = total_pendientes + 1
    return total_pendientes

pendientes = contar_pendientes(mantenimientos)
print(f"Quedaron {pendientes} pendientes por resolver, programar a novedades para dar solucion")

def generar_novedades(lista_mantenimientos):
    novedades = []
    for m in lista_mantenimientos:
        for pendiente in m['pendientes']:
            novedad = {
                "placa": m['placa'],
                "fecha_origen": m['fecha'],
                "componente": pendiente['componente'],
                "recomendacion": pendiente['recomendacion'],
                "estado": "pendiente por programar"
            }
            novedades.append(novedad)
    return novedades

lista_novedades = generar_novedades(mantenimientos)
for n in lista_novedades:
    print(f"Placa: {n['placa']} | Componente: {n['componente']} | Estado: {n['estado']}")
    print(f"Recomendacion: {n['recomendacion']}")
    print("---")