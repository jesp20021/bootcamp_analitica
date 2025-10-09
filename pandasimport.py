import pandas as pd

#cargar el archivo.cvs
df=pd.read_csv("data/archivo.csv", sep=";")#,names=#header=None)#cuando los datos no tienen encabezado le agrega uno numerico

#mostrar la data de csv
print(df)
print(df.head(2))
df["P_total"]=df['Precio']*df['Cantidad']
print("La nueva serie es:")
print(df)

#importar colomnas especificas del csv
fr2 = pd.read_csv("data/archivo.csv",sep=";", usecols=["Producto",
"Precio"])
print("Nuevo data frame solo con dos columnas")
print(fr2)

#importar solo el numero de filas especifico
fr3 = pd.read_csv("data/archivo.csv",sep=";", nrows=2, encoding="utf-8")#utf-8 para caracteres especiales
print("nuevo data frame solo con dos filas")
print(fr3)

#exportar 
df.to_csv("nuevo_archivo.csv",index=False)
df.to_excel("archivo_excel.xlsx",index=True)#libreria necesaria -- python -m pip isntall openpyxl