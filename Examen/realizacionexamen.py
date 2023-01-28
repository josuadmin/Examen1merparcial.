"""#si el cliente ingresa por consola la cantidad de articulos menor de 3 nuidades debe realizar las siguientes operaciones.

n1 = int(input("ingrese el primer valor: "))
n2 = int(input("ingrese el segundo valor: "))
n3 = int(input("ingrese el tercer valor: "))
n4 = int(input("ingrese el cuarto valor: "))
n5 = int(input("ingrese el quinto valor: "))
n6 = int(input("ingrese el sexto valor: "))

print("valor total", n1 + n2 + n3 + n4 + n5 + n6)

#calculamos el IVA.

cant = int(input("ingrese el valor total sumado: "))
val = int(input("ingrese el valor: "))

sub = cant * val 
iva = sub * 0.12
total = sub + iva 

print("Cantidad: ", cant)
print("Valor: ", val)
print("Subtotal: ", sub)
print("IVA 12%: ", iva)
print("Total del valor: ", total)"""

#si el cliente ingresa por consola la cantidad de articulos mayor o igual a 5 unidades debe realizar las siguientes operaciones.

n1 = int(input("ingrese el primer valor: "))
n2 = int(input("ingrese el segundo valor: "))
n3 = int(input("ingrese el tercer valor: "))
n4 = int(input("ingrese el cuarto valor: "))
n5 = int(input("ingrese el quinto valor: "))

print("valor total", n1 + n2 + n3 + n4 + n5)


import os

monto = float (input ('Ingresa el valor de monto: '))
if monto>5000:
    descuento = monto * 15
else:
    descuento = 15
print ('Valor de descuento: ' + repr (descuento))
print ()
os.system ('pause')

#iva

cant = int(input("ingrese el valor total sumado: "))
val = int(input("ingrese el valor: "))

sub = cant * val 
iva = sub * 0.12
total = sub + iva 

print("Cantidad: ", cant)
print("Valor: ", val)
print("Subtotal: ", sub)
print("IVA 12%: ", iva)
print("Total del valor: ", total)















