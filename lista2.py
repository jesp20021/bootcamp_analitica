import random
lista=[]
for j in range(15):
    j=random.randint(1,50)
    lista.append(j)
print(lista)

pares=[]
impares=[]
for f in lista:
    if f %2 ==0: 
        pares.append(f)
    else:
        impares.append(f)
print(pares)
print(impares)    
if 32 in lista:
    print("El numero 32 se encuentra en la lista")
else:
    print("El numero no se encuentra en la lista")
    
print(sum(lista))
print(max(lista))
print(min(lista))
prom=sum(lista)/len(lista)
print(prom)
lista2=lista[::-1]
print(lista[::-1])#reordenar la lista de atra hacia adelante(hacer un bucle en reversa)
print(lista[-1])#imprime el ultimo numero
print(set(lista))#elimina los numeros duplicados de la lista y los ordena de menor a mayor 
numor=set(lista)
print(f"numeros ordenados{sorted(numor)}")
print(f"ordenados 2 {sorted(lista)}")   

