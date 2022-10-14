import subprocess
from sys import stdout
import sys
from time import sleep
import re
import requests
import ast

"""
This little scrips takes two arguments
The first one is the IP address where it has to make the post request

WARNING: THIS MUST BE EXECUTED ON A DIFFERENT COMPUTER, NOT THE HOST ITSELF

The second is the device id which its posting the met information
The API has some intelligence to only register devices that are not present already

usage example:

python3 temp_sensor_send.py 10.0.0.107 01
python3 temp_sensor_send.py www.somerandomsite.com 01
"""

#capture args
args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

if cant_args < 3:
    print("ERROR! Muy pocos argumentos")
    sys.exit()

if cant_args > 3:
    print("ERROR! Demasiados argumentos")
    sys.exit()


# Register new device
url_dev = "http://" + args[1] + ":8080/device"
myobj = {
    "id": "it" + args[2],
    "n": "Internal Temp Device " + args[2],
    "k": "it000" + args[2]
    }

x = requests.post(url_dev,data=myobj);
print(x.text);

#enter loop sending data
url_meas = "http://" + args[1] +":8080/measurement"
id_string = "it" + args[2]
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

    print(x.text)

    sleep(5)