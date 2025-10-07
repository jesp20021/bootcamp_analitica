import pandas as pd
serie1=pd.Series([100,200,300,400,500], 
                 index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
print(serie1['Miercoles'])
print(f'el promedio es {serie1.mean()}')
#En pandas no es necesario crear un for para que me recorra todos los datos
serie2=serie1+50
print(serie2)
print(serie1)