import pandas as pd

#carga archivo json
df=pd.read_json("data/personas2.json")
print("dataframe origial")
print(df)

#seleccionar o dividir grupos por dataframe separados para luego unirlos
df1= pd.json_normalize(df["grupo1"])#.tolist())para versiones anteriores de python 13.13
df2= pd.json_normalize(df["grupo2"])#versiones 13.13 en adelante sin el tolist

print("datos 1")
print(df1)
print("datos 2")
print(df2)

#se unifica la data para que se muestre en un solo conjunto de datos
df_final=pd.concat([df1,df2],axis=0,ignore_index=True)
print(df_final)