import pandas as pd

#leer json
df = pd.read_json("data/data.json")
print("DataFrame original:")
print(df)

#Filtro por fecha
"""df_filtrado=df[df["fecha_nac"] > "2000-01-01"]
print(df_filtrado)"""

df["fecha_nac"]=pd.to_datetime(df["fecha_nac"],format=('%d/%m/%Y'))
df_filtrado=df[df["fecha_nac"].between("1998-01-01","2001-01-01") ]#between para filtrar
print("Nuevo data frame por fecha")
print(df_filtrado)