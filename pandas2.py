#uso de pandas con diccionarios, genera dataframes que son estructuras de datos bidimensionales
import pandas as pa
datos={
    'Nombre':['Juan', 'Ana','Milena'],
    'Edades':[15,25,32],
    'Ciudad': ['Bogota','Cali', 'Medellin'] }

dataf=pa.DataFrame(datos)
print(dataf)

print(dataf['Edades'])
print(dataf.loc[1])#acccede al nombre del indice
print(dataf.iloc[-1])#accede a la posicion del indice

filtro=dataf[dataf['Edades']>=25]#coja toda la dataf y busca en dataf todas las edades que son mayores o iguales a 25
print(filtro)