from django.http import HttpResponse

def ruta_critica_view(request):
    return HttpResponse("Acceso concedido a datos sensibles de Bite.co")