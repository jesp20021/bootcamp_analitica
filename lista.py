

import random;

frutas=["uva","pera","manzana","banano","fresa"]
print(frutas[0]) # Accede al primer elemento de la lista (''' sig comentario)
print(frutas[-1]) # Accede al ultimo elemento de la lista
print("________")
#recorer toda la lista elemento por elemento
for elemento in frutas:
    print(elemento)
#eliminar manzana???
print("__________")
#del frutas[2] # Para eliminar algun elemento de la lista
print(frutas)
if "manzana" in frutas:
    print("manzana se encuentra en la lista")
else:
    print("Manzana No se encuentra en la lista")
print("_________")
#contar elementos de lista
print(f"La lista de frutas contiene {len(frutas)} elementos")
#contar elementos de la lista con nombre menor a 5 letras
f_corta = [f for f in frutas if len(f)<= 4] # =<5

f_corta2=[]
for f in frutas:
    if len(f)<= 3:
        f_corta2.append(f)


print(f"La lista cuenta con {len(f_corta)} frutas con nombres cortos")
print(f" Las frutas con nombres cortos son: {f_corta}")
n=random.randint(1,11)
print(f"numero aleatorio es {n}")
#Crear en una lista de 15 numeros generados aleatoriamente entre 1 y 50 y mostras una nueva lista de los pares e 
# impares; adicional si el numero 32 se encuentra entre la lista

