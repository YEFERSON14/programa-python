# MATRIZ DE INVENTARIO
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Impresora", 7, 7],
    ["A105", "USB", 2, 5]
]

# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR
def calcular_pedido(stock_actual, stock_minimo):

    # Si el stock actual es menor al mínimo
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual

    # Si el stock es suficiente
    else:
        return 0


# ENCABEZADO DEL REPORTE
print("===== REPORTE DE REABASTECIMIENTO =====\n")

# RECORRER LA MATRIZ
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # LLAMADO DE LA FUNCIÓN
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # MOSTRAR RESULTADOS
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("-----------------------------------")