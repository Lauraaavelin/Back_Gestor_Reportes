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

import boto3

def notificar_admin(self):
    # Usamos Boto3 que habla con AWS por el puerto 443 (HTTPS), 
    # el cual SIEMPRE está abierto en AWS.
    try:
        sns = boto3.client('sns', region_name='us-east-1')
        sns.publish(
            TopicArn='tu:arn:de:sns:aquí', # Copia el ARN de tu consola
            Message="Alerta de Seguridad: Acceso no autorizado detectado en Bite.co",
            Subject="Urgente: Brecha de Seguridad"
        )
        print("Alerta enviada vía Amazon SNS")
    except Exception as e:
        print(f"Error enviando SNS: {e}")