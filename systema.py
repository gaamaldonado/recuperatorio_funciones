from utils import calcular_subtotale , descuentoso
totaltodo = [] 
for i in range(3):
    precio = (input("ingresa el precio del producto "))
    cantidad =(input("ingresa la cantidad de productos que compraste  ")) 
    subtotal = calcular_subtotale(precio, cantidad) 
    precio_final = descuentoso(subtotal) 
    totaltodo.append(precio_final) 
print(totaltodo)    