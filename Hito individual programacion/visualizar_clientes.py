# Mediante un 'with open' y la 'r' visualizo el archivo .txt
# creado antes, los almaceno en la variable datos y los imprimo.
def visualizar_clientes():
    with open('datos_personales.txt', 'r') as file:
        datos = file.readlines()
        print(f'Estos son los datos agregados: {datos}')