from django.shortcuts import render

from .services import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    registros_historicos = [
        {"planta": "Planta Norte", "consumo_kwh": 1500.0},
        {"planta": "Planta Sur", "consumo_kwh": 3200.5},
        {"planta": "Planta Este", "consumo_kwh": 980.4},
        {"planta": "Planta Oeste", "consumo_kwh": 2450.0},
        {"planta": "Planta Norte", "consumo_kwh": 600.0},
        {"planta": "Planta Sur", "consumo_kwh": 450.0},
    ]

    metricas = obtener_metricas_consumo(registros_historicos)

    contexto = {
        "total_emisiones": metricas["total_global_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "detalle_emisiones": metricas["emisiones_por_planta"]
    }

    return render(request, "sustentabilidad/panel.html", contexto)
