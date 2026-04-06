# Back_Gestor_Reportes

Aquí va la lógica del back del Gestor de Reportes ya con todas las apis y demás para saber cuales van a ser los gets 
Por último esto se clona en las instancias que vamos crear ( asi se gastan menos creditos porque se hace desde antes se verifica que todo funcione antes de ponerse en una de las instancias) 

## COMO CORRERLO
Para corre mandamos el comando : python manage.py runserver 0.0.0.0:8080
Y luego en google se pone: http://localhost:8080/report?code=XYZ999
y en el codigo por ahora solo se puede poner'XYZ999' y 'ABC123'

## data.jason
En este archivo esta la informacion que le llega al gestor de reportes 

## Cosas por hacer 
* Implementar los TODO que estan en el archivo
   ---
   reports/views.py
   ---
* podemos poner un delay de 100ms (algo pequeño porque sino no cumplimos con latencia) para simular el tiempo que se demora el gestor en obtener la información necesaria (json) del motor de analisis. (El motor de analisis no existe lo simulamos con el json)
* Hacer las pruebas JMeter
