import pandas as pa
ej=pa.read_csv("data/ejemploo.csv",nrows=5)
print(ej)
ej["Edad"]=2025-ej["Anacimiento"]
print(ej)
#defino columnas a selecionar
columnas=["Nombres","Apellidos","Edad"]
#crea la nueva serie con la columnas selecionadas
ej2=ej[columnas]
print(ej2)
ej.to_excel("usuarios.xlsx",index=False)
print("se creo elarchivo excel")