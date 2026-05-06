import time
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger('security')

class SecurityExperimentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. PASO DE DETECCIÓN (Antes de la vista)
        if '/ataque/configuracion-sensible/' in request.path:
            if not request.user.is_authenticated:
                start_time = time.perf_counter()
                
                # Ejecutamos la alerta SIN detener la petición
                self.notificar_admin()
                
                end_time = time.perf_counter()
                print(f"--- EVENTO DETECTADO EN: {end_time - start_time:0.5f}s ---")

        # 2. CONTINUIDAD (Esto asegura que NO sea prevención)
        # Dejamos que la petición siga su curso hacia la URL/Vista
        response = self.get_response(request)
        
        return response

    def notificar_admin(self):
        # Para el experimento inicial, usamos la consola de Django 
        # para no pelear con SMTP antes de tiempo
        send_mail(
            'ALERTA SEGURIDAD BITE.CO',
            'Acceso no autorizado detectado.',
            'sistema@bite.co',
            ['admin@bite.co'],
            fail_silently=False,
        )