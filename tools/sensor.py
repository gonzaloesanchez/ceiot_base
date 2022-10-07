import subprocess
from sys import stdout
import sys
from time import sleep
import re
import requests
import ast

#capture args
args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

# Register new device
url_dev = "http://10.0.0.107:8080/device"
myobj = {
    "id": "it" + args[1],
    "n": "Internal Temp Device " + args[1],
    "k": "it00000"
    }

x = requests.post(url_dev,data=myobj);
print(x.text);

#enter loop sending data
url_meas = "http://10.0.0.107:8080/measurement"
id_string = "it" + args[1]
jsonObj = {
    "id": id_string,
    "t": 0,
    "h": 0
}

while True:
    aux = subprocess.run(["sensors"], capture_output=True)
    sensors_str = aux.stdout.decode("utf-8")
    temp = re.findall("\+[0-9.]+",sensors_str)
    jsonObj["t"] = float(temp[0])

    x = requests.post(url_meas, json = jsonObj)

    sleep(5)