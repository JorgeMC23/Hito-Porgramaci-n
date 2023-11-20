# Primero creo un input para que me diga el nombre y lo meto en la variable ‘palabra’.
# Después hago lo mismo que en el anterior para visualizar el archivo .txt.
# Hago un 'if' para ver si 'palabra' está en 'datos' y en caso de que este lo mando
# mediante un append a la lista vacía creada antes  llamada 'encontrado'.
# Ahora lo imprimo y hago un else por si 'palabra' no se ha encontrado.
def buscar_clientes():
    palabra = input('Introduzca el nombre del cliente que desea buscar: ')
    with open('datos_personales.txt', 'r') as file:
        datos = file.readlines()
        encontrado = []
        if palabra in datos:
            encontrado.append(palabra.strip())
            print(f'{encontrado} ha sido encontrado')
        else:
            print(f'{encontrado} no ha sido encontrado,pruebe otra vez')