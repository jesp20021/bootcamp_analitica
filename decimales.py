import math as ma
num=3.9875
truncado=int(num) #elimina la parte decimal y deja la parte entera
redondeado=round(num,0) #aproximacion del numero teniendo encuenta la parte decimal
print(f'numero truncado: {truncado}')
print(f'numero redondeado: {redondeado}')

print(f'Raiz cuadrada de 16 {ma.sqrt(16)}')
print(f'potencia 4: {4**2}')#primera fora de exponenete
print(f'ptencia con pow: {pow(4,2)}')# segunda forma de sacar los exponentes
print(f'logaritmos 100 en base 10 {ma.log(100,10)}') #la funcion logaritmo esta dentro de las funcion math
print(f'round hacia arriba {ma.ceil(3.7)}')
print(f'round hacia abajo {ma.floor (3.7)}')