# Primero creo un input para saber el nombre del cliente.
# Creo una lista vacía.Creo un input para saber el nombre  del producto y hago
# un if por si el cliente quiere salirse del bucle.En caso de que no se salga,
# le pediré el precio del producto y le mandaré estos datos a la variable 'productos'.
def realizar_compra():
    cliente_nombre = input('Introduce el nombre del cliente: ')
    productos = []
    while True:
        producto_nombre = input('Introduce el nombre del producto: ')
        if producto_nombre.lower() == 'salir':
            break
        else:
            precio = float(input('Introduce el precio del producto: '))
            productos.append(f'{producto_nombre},{precio}')
# Abro el archivo .txt en modo agregar y escribo dentro de él el nombre del cliente.
# Después itero sobre la lista de productos y meto dentro del .txt los datos de los productos.
    with open('compras.txt', 'a') as file:
        file.write(f'Cliente: {cliente_nombre}\n')
        for producto in productos:
            file.write(f'{producto}\n')
        file.write('\n')
    # Aqui lo que hago es mediante un input me ponga el cliente su nacionalidad,y si es
    # española,se le aplicara un iva del 21%,si no lo es,no se le aplicara ningun cambio en su precio.
    nacionalidad_cliente = input('Pon cual es tu nacionalidad: ')
    if nacionalidad_cliente.lower() == 'española':
        impuestos = precio * 0,21
        precio += impuestos