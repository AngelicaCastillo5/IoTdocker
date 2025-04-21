# IoTdocker
testeo de arquitecturas de transmisión en iot como utilización de node-red, telegraf, chonograf, influxdb, emqx, grafana, thingsboard.

Idea principal:
Simular envio de datos por medio de python, hacia un tópico mqtt.
Tomar los datos del topico mqtt via node-red y adecuarlos para que los datos sean seleccionados por telegraf.
Utilizar agente telegraf para incorporar los datos a una base serie temporal como influxdb.
Monitorear los datos ingresados por medio de chronograf y grafana
crear alertas por medio de grafana y utilizar kapacitor 
Crear dashboard y gestion de alertas por medio de node-red, grafana, chronograf, thingsboard con la finalidad de dar diversas alternativas de monitoreo



#Datos utiles

Docker contenedores:

activacion de todos los contenedores:  docker compose up -d
estado de los contenedores: docker compose ps
logs de todos los servicios: docker compose logs -f
Reiniciar todos los contenedores: docker compose restart
Detener todos los contenedores: docker compose down
Volver a reconstruir y levantar los contenedores: docker compose up --build
Levantar y volver a reconstruir solo un contendero: docker compose up -d --build <contenedor>
activar solo un contenedor: docker compose up -d <nombre_del_servicio>
Ver servicios disponibles: docker compose config --services

Docker redes: 
