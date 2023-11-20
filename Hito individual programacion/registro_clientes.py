# Creo tres input para que me escriba sus datos personales,
# y creo un archivo .txt para almacenarlos ahí.
def registro_cliente():
    nombre = input('Escribe  tu nombre: ')
    apellidos = input('Escribe tus apellidos: ')
    facturacion = input('Escribe tu factura: ')
    with open('datos_personales.txt', 'a') as file:
        file.write(f'{nombre},{apellidos},{facturacion} \n')
