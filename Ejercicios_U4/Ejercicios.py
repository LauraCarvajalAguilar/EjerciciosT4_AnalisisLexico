import re

path = "Prueba.txt"

try:
    archivo = open(path, 'r')
except:
    print ("El Archivo No Se Encuentra En Esta Carpeta")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print (texto)

#Buscar y Mostrar VARIABLES VALIDAS
patron = r"/([VE]-)?[0-9]{1,8}/i"
result = re.findall(patron,texto)

print ("\n Resultado de búsqueda " , result)

print"\n"
print"\n"

#Buscar y Mostrar ENTEROS Y DECIMALES
patronEnTDEC = r"[0-9]+\.[0-9]+([eE][+\-]?[0-9]+)?"
resultEnTDEC = re.findall(patronEnTDEC,texto)

print ("\n Resultado de búsqueda " , resultEnTDEC)

print"\n"
print"\n"

#Buscar y Mostrar OPERADORES ARITMETICOS
patronOPERARIT = r"(\w[+|-|*|/])\w+/g"
resultOPERSRTI = re.findall(patronOPERARIT,texto)

print ("\n Resultado de búsqueda " , resultOPERSRTI)

print"\n"
print"\n"

#Buscar y Mostrar OPERADORES RELACIONES
patronOPERREL = r"\w[!]|[/<>=]\w+/g"
resultOPERREL = re.findall(patronOPERREL,texto)

print ("\n Resultado de búsqueda " , resultOPERREL)

print"\n"
print"\n"

#Buscar y Mostrar PALABRAS RESERVADAS
patronPALRES = r"(program|var|const|begin|end|Writeln|if|then|else|end|Mayor|Menor)\\b"
resultPALRES = re.findall(patronPALRES,texto)

print ("\n Resultado de búsqueda " , resultPALRES)