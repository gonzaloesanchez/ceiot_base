import requests
import sys
import ast

"""
This little scrips takes two arguments
The first one is the http address where it has to make the request
The second is the device id to be deleted
"""

args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

if cant_args < 3:
    print("ERROR! Muy pocos argumentos")
    sys.exit()

if cant_args > 3:
    print("ERROR! Demasiados argumentos")
    sys.exit()

url = "http://" + args[1] + ":8080/device/" + args[2]

x = requests.delete(url)

print(x.text)