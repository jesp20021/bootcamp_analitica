'''def suma(a,b): # se define def el nombre de la funcion y dentro del parentesis
    sum=a+b
    return sum

print(suma(8,10))
print(suma(2,4))
print(suma(6,5))'''

'''def saluda(nom):
    return print(f"hola buenos dias{nom}")

saluda("Juan")
saluda("Miguel")
saluda("Paola")

def cuadrado(n):
    return n** 2

numero= cuadrado(2)
print(f"el resultado es: {numero}")

def cambia(d,o):
    r=[]
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)
    return r

datos=[1,None,2,None,3]
print(cambia(datos,0))

#funciones lambda son la que se ejecutan en una sola linea
suma2 = lambda x,y:x+y
print(f"la suma de 4 + 1 ={suma2(4,1)}")

cambia2 = lambda datos,p: [p if i is None else i for i in datos]
print(f"cambia con lambda{cambia2(datos,0)}")'''

#numeros=[10,8,45,26,7]
numero=(10,8,45,26,7)
def ejercicio(numero):
    may=max(numero)
    menor=min(numero)
    su=sum(numero)
    return print(f"El mayor es {may} El menor es {menor} La suma total es {su}")
ejercicio(numero)
print(f"Ordenados{sorted(numero)}")