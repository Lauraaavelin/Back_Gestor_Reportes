import time
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger('security')

class SecurityExperimentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Definimos el objetivo del ataque
        if '/ataque/configuracion-sensible/' in request.path:
            # Iniciamos cronómetro
            start_time = time.perf_counter()
            
            # 2. Simulamos la falta de Auth0 (verificamos si NO está autenticado)
            if not request.user.is_authenticated:
                # 3. LOGGING INMEDIATO (Para auditoría)
                logger.warning(f"ANOMALÍA: Intento de acceso en {request.path} | Usuario: Anónimo")
                
                # 4. DISPARAR ALERTA (Aquí es donde mides los < 5s)
                self.notificar_admin()
                
                end_time = time.perf_counter()
                print(f"--- TIEMPO DE DETECCIÓN: {end_time - start_time:0.5f} segundos ---")

        return self.get_response(request)

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