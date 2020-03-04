#!/usr/bin/env python
import requests
from os import system
from datetime import datetime

system('cls')

now = datetime.now().strftime("%Y/%m/%d ~ %H:%M:%S")

print('')
print('   Cotizacion Oficial Dolar')

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

json = requests.get(URL).json()

print()
print('  MONEDA  |  COMPRA  |  VENTA')
print('  ---------------------------')

for index, emoji in enumerate(('🟢', '🔵')):
    
    nombre = json[index]['casa']['nombre']
    
    if nombre=='Dolar Oficial':
    	moneda='USD '
    if nombre=='Dolar Blue' :
    	moneda='BLUE'

    compra = json[index]['casa']['compra'][:-1]
    venta = json[index]['casa']['venta'][:-1]
   
    print(f"  {moneda}    |   {compra}  |  {venta}")

print('  ---------------------------')

print()
print('  ' + str(now))
print()