from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('configuracion-sensible/', lambda r: HttpResponse("test")),
]