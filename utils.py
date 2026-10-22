def calcular_subtotale(precio, cantidad):
    return precio * cantidad 
def descuentoso(subtotal):
    if subtotal >= 20000:
        return subtotal * 0.90
    else:
        return subtotal