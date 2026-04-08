import json
from datetime import datetime
from pathlib import Path
from django.http import JsonResponse

def report_view(request):
    code = request.GET.get('code')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # Validación básica
    if not code:
        return JsonResponse({"error": "code is required"}, status=400)

    # Cargar JSON (simulado) desde la carpeta Gestor
    data_file = Path(__file__).resolve().parents[1] / 'data.json'
    with data_file.open(encoding='utf-8') as f:
        data = json.load(f)

    # Filtrar datos
    filtered = []

    for item in data:
        if item["code"] != code:
            continue

        if start and end:
            fecha_item = datetime.strptime(item["fecha"], "%Y-%m-%d")
            fecha_start = datetime.strptime(start, "%Y-%m-%d")
            fecha_end = datetime.strptime(end, "%Y-%m-%d")

            if not (fecha_start <= fecha_item <= fecha_end):
                continue

        filtered.append(item)

    #  TODO: aquí van los cálculos del reporte
    cantidad = len(filtered)
    prom_costo = 0
    prom_uso = 0
    prom_datos = [0, 0, 0]

    for item in filtered:
        prom_costo += item.get("cost", 0)
        prom_uso += item.get("time_used", 0)
        usage = item.get("usage", {})
        prom_datos[0] += usage.get("cpu", 0)
        prom_datos[1] += usage.get("storage", 0)
        prom_datos[2] += usage.get("network", 0)

    if cantidad > 0:
        prom_costo = prom_costo / cantidad
        prom_uso = prom_uso / cantidad
        prom_datos[0] = prom_datos[0] / cantidad
        prom_datos[1] = prom_datos[1] / cantidad
        prom_datos[2] = prom_datos[2] / cantidad

    report = {
        "Code": code,
        "Costo promedio": prom_costo,
        "Uso promedio": prom_uso,
        "Datos promedio": {
            "cpu": prom_datos[0],
            "storage": prom_datos[1],
            "network": prom_datos[2]
        },
        "Cantidad de items": len(filtered)
    }

    return JsonResponse({
        "data": filtered,
        "report": report
    })