# financieros.py será un archivo que va a contener los calculos
# de IGV, SubTotal y Total

# Recordar financieros utiliza conceptos de modularidad
# Que pueden ser reutilizados en cualquier momento por el programa

# Variable
igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total - obtenerSubtotalconTotal(total)

