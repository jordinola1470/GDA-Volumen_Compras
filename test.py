import os
from datetime import date

fecha  = (date.today()).strftime('%d%m%Y')
nombre = str(f'matriz_registros_{fecha}.xlsx')

directorio_actual = os.getcwd()

nombre_ruta = os.path.join(directorio_actual,nombre)

print(nombre_ruta)