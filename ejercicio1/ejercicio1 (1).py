# funciones
def limpiar_registro_sensor(registro_raw: dict[str, str]):

    # aca limpiamos el id
    sensor_id = registro_raw["sensor_id"].strip()

    # limpiamos la temperatura y la pasamos a float
    temperatura = float(registro_raw["temperatura"]
                        .replace("°C", "")
                        .replace("C", "")
                        .strip()
                        )

    #  aqui limpiamos la ubicacion
    ubicacion = registro_raw.get("ubicacion", "").strip()

    if ubicacion == "":
        ubicacion = "Ubicación desconocida"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]
        sensor_id = sensor["sensor_id"]

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor_id)

        suma_temperaturas = suma_temperaturas + temperatura

    # calculamos el promedio
    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0

    return lista_sensores_alerta, promedio_temperatura


# Bloque principal
sensores_raw = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },

    {
        "sensor_id": " SENSOR-002",
        "temperatura": "31.2 °C",
        "ubicacion": "  Planta Sur "
    },

    {
        "sensor_id": "SENSOR-003 ",
        "temperatura": "27.8 °C",
        "ubicacion": "Almacén"
    },

    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "33.6C"
    },

    {
        "sensor_id": "SENSOR-005",
        "temperatura": "22.9 °C",
        "ubicacion": "   "
    }
]


# limpiar los registros
sensores_limpios = []

for registro in sensores_raw:
    registro_limpio = limpiar_registro_sensor(registro)
    sensores_limpios.append(registro_limpio)


umbral = 30.0

sensores_alerta, promedio_global = generar_resumen_sensores(sensores_limpios, umbral)


# reporte final
print("========== REPORTE ECOTECH SOLUTIONS ==========")
print()
print("Registros normalizados:")

for sensor in sensores_limpios:
    print(f"- {sensor['sensor_id']} | {sensor['temperatura']} °C | {sensor['ubicacion']}")

print()
print(f"Umbral de temperatura: {umbral} °C")

if len(sensores_alerta) > 0:
    print("Sensores en alerta:")
    for sensor_id in sensores_alerta:
        print(f"- {sensor_id}")
else:
    print("No hay sensores en alerta.")

print()
print(f"Temperatura promedio de la planta: {promedio_global:.2f} °C")
print("===============================================")
