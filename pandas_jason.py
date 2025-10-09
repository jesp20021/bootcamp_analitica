import pandas as pd

#Leer archivo Json
df=pd.read_json("data/personas.json")
#imprimimos la data importada
print(df)

#Normalizacion de data
df_normalizado=pd.json_normalize(df["estudios"].tolist())
print(df_normalizado)

df_final=pd.concat([df.drop(columns="estudios"),df_normalizado],axis=1)
print(df_final)
#axis(0) lo parte en filas y axis(1) en columnas
