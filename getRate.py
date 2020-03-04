#!/usr/bin/env python
import requests
from os import system
from datetime import datetime

system('cls')

#obtener fecha y hora
now = datetime.now().strftime("%Y/%m/%d ~ %H:%M:%S")

#titulo
print('')
print('   Cotizacion Oficial Dolar')

#url
URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

#respuesta
json = requests.get(URL).json()

#header
print()
print('  MONEDA  |  COMPRA  |  VENTA')
print('  ---------------------------')

for index, emoji in enumerate(('🟢', '🔵')):
    
    nombre = json[index]['casa']['nombre']
    
    if nombre=='Dolar Oficial':
    	moneda='USD '
    if nombre=='Dolar Blue' :
    	moneda='BLUE'
    
    #datos
    compra = json[index]['casa']['compra'][:-1]
    venta = json[index]['casa']['venta'][:-1]
   
    #salida
    print(f"  {moneda}    |   {compra}  |  {venta}")

print('  ---------------------------')

print()
print('  ' + str(now))
print()