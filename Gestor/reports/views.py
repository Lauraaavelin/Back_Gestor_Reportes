import json
from datetime import datetime
from django.http import JsonResponse

def report_view(request):
    code = request.GET.get('code')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # Validación básica
    if not code:
        return JsonResponse({"error": "code is required"}, status=400)

    # Cargar JSON (simulado)
    with open('data.json') as f:
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
    prom_costo=0
    prom_uso=0
    prom_datos=[0, 0, 0]
    for i in filtered:
        for j in i:
            if j=="costo":
                prom_costo+=j["costo"]
            if j=="uso":
                prom_uso+=j["uso"]
            if j=="datos":
                prom_datos[0]+=j["datos"]["cpu"]
                prom_datos[1]+=j["datos"]["storage"]
                prom_datos[2]+=j["datos"]["network"]

    prom_costo= prom_costo/cantidad
    prom_uso= prom_uso/cantidad
    prom_datos[0]= prom_datos[0]/cantidad
    prom_datos[1]= prom_datos[1]/cantidad
    prom_datos[2]= prom_datos[2]/cantidad    

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