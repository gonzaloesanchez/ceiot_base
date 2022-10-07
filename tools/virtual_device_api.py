import requests
import datetime
import sys
import ast

now = datetime.datetime.now()

args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

if cant_args < 2:
    print("ERROR! Muy pocos argumentos")
    sys.exit()

if cant_args > 2:
    print("ERROR! Demasiados argumentos")
    sys.exit()

#Get temperature and humidity data from API

url = "https://api.open-meteo.com/v1/forecast?latitude=-31.73271&longitude=-60.52897&timezone=auto&hourly=temperature_2m&hourly=relativehumidity_2m"

resp = requests.get(url=url)
data = resp.json()

#data is presented as records hourly from 00hs current day up to 168 records

algo = [data["hourly"]["time"][now.hour], data["hourly"]["temperature_2m"][now.hour], data["hourly"]["relativehumidity_2m"][now.hour]]
print (algo)

temp = data["hourly"]["temperature_2m"][now.hour]
hum = data["hourly"]["relativehumidity_2m"][now.hour]

# Register new device
url_dev = "http://localhost:8080/device"
myobj = {
    "id": "v" + args[1],
    "n": "Virtual Device " + args[1],
    "k": "v00000"}

x = requests.post(url_dev,data=myobj);
print(x.text);

url_meas = "http://localhost:8080/measurement"
id_string = "v" + args[1]
jsonObj = {
    "id": id_string,
    "t": temp,
    "h": hum
}

x = requests.post(url_meas, json = jsonObj)
print("Enviada medida de temperatura ", jsonObj["t"], "ºC y humedad ", jsonObj["h"], "%\n")
print("Dispositivo que aporta los datos: ", jsonObj["id"])
print(x.text + "\n")