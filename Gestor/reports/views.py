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
    report = {
        "code": code,
        "message": "TODO: calcular métricas",
        "items": len(filtered)
    }

    return JsonResponse({
        "data": filtered,
        "report": report
    })