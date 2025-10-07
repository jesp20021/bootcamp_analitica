import pandas as pd
data1={'Producto':['Manazana','Banana','Cereza'],
       'Precio':[2.5,1.8,3.0],
       'Cantidad':[10,15,8]}
dataf=pd.DataFrame(data1)
print(dataf)
filtro=dataf[dataf['Cantidad']>=10]
print(filtro)
