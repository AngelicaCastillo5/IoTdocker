# IoTdocker
testeo de arquitecturas de transmisión en iot como utilización de node-red, telegraf, chonograf, influxdb, emqx, grafana, thingsboard.

Idea principal:
Simular envio de datos por medio de python, hacia un tópico mqtt.
Tomar los datos del topico mqtt via node-red y adecuarlos para que los datos sean seleccionados por telegraf.
Utilizar agente telegraf para incorporar los datos a una base serie temporal como influxdb.
Monitorear los datos ingresados por medio de chronograf y grafana
crear alertas por medio de grafana y utilizar kapacitor 
Crear dashboard y gestion de alertas por medio de node-red, grafana, chronograf, thingsboard con la finalidad de dar diversas alternativas de monitoreo
