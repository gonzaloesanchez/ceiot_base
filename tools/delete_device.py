import requests
import sys
import ast

args = ast.literal_eval(str(sys.argv))
cant_args = len(sys.argv)

if cant_args < 2:
    print("ERROR! Muy pocos argumentos")
    sys.exit()

if cant_args > 2:
    print("ERROR! Demasiados argumentos")
    sys.exit()

url = 'http://localhost:8080/device/' + args[1]

x = requests.delete(url)

print(x.text)