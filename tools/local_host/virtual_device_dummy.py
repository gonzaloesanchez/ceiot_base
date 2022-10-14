import requests
import sys
import ast
import time
import json

args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

if cant_args < 2:
    print("ERROR! Muy pocos argumentos")
    sys.exit()

if cant_args > 2:
    print("ERROR! Demasiados argumentos")
    sys.exit()

# Register new device
url_dev = "http://localhost:8080/device"
myobj = {
    "id": "v" + args[1],
    "n": "Virtual Device " + args[1],
    "k": "v00000"}

x = requests.post(url_dev,data=myobj);
print(x.text);


#enter loop sending data
url_meas = "http://localhost:8080/measurement"
id_string = "v" + args[1]
jsonObj = {
    "id": id_string,
    "t": 30.0,
    "h": 65
}

while True:
    x = requests.post(url_meas, json = jsonObj)
    print("Enviada medida de temperatura ", jsonObj["t"], "ºC y humedad ", jsonObj["h"], "%\n")
    print("Dispositivo que aporta los datos: ", jsonObj["id"])
    print(x.text + "\n")

    #Se esperan 10s para volver a enviar
    time.sleep(10)
