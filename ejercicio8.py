import pandas as pd
datos= {
    'Producto':['Manzana','Banana','Cereza'],
    'Precio':[2.5,1.8,3.0],
    'Cantidad':[10,15,8]
}
df= pd.DataFrame(datos)
print(df.head(2))#imprime las filas que le indiquemos de arriba hacia abajo
print(df.tail(2))#imprime las filas desde la ultima hacia arriba
df['p_total']=df['precio']*df['cantidad']
print('la nueva serie es:')
print(df)
print(f'la suma total de los p_total es: {df['p_total'].sum()}')

df_ordenado = df.sort_values(by='producto', key=lambda x: x.str.lower())#,ascending=False)# lo ordena en orden alfabetico
print('el data frame ordenado es:')
print(df_ordenado)