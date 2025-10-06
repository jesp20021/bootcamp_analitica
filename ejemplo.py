#Hay que tener presente como se maneja la data en una estructura de datos
d=[0,1,2] #es un arreglo almacenado las diferentes notas 
print(d, 'Lista original')
"""e=['pera','uva','manzana']
f=[2.5,3,4.5]
print(e)
print(e[2])
d.append(9)
print(d, ' Funcion append agregar')
d.extend([3,4,5,6,2.9,3])
print(d, ' Funcion extend')
d.insert(2,909)
print(d, ' Funcion insert') 
d.remove(3)
print(d, ' Funcion remove') #Borra el primer resultado que sea igual a lo que indique
pp=d.pop(2)
print(pp,d, ' Funcion pop') #Borra el la posicion que sea igual a lo que indique y devuelve el elemento y se almacena en una variable
d[0]=1230.2
print(d)"""
lista=[]
nombre=input('Ingrese el nombre del usuario a ingresar: ')
lista.append(nombre)
pregunta=input('Desea agregar un nuevo nombre: ')
if pregunta == "si":
    nombre=input('Ingrese el nombre del usuario a ingresar: ')
    lista.append(nombre)
else:
    print(lista)