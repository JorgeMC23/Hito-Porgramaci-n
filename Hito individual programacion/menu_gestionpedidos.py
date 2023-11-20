from registro_clientes import *
from seguimiento_compra import seguimiento_compra
from visualizar_clientes import *
from buscar_clientes import *
from realizar_compras import *
from seguimiento_compra import *
# Aquí hago unos print con las distintas opciones que le ofrezco al cliente.
while True:
    print('1. Agregar un cliente')
    print('2. Visualizar datos personales')
    print('3. Buscar un cliente')
    print('4. Realizar compra')
    print('5. Seguimiento compra')
    print('6. Salir')




    # Solicita al usuario que elija una opción.
    opcion = int(input('Elige una opcion: '))




    if opcion == 1:
        registro_cliente()
    elif opcion == 2:
        visualizar_clientes()
    elif opcion == 3:
        buscar_clientes()
    elif opcion == 4:
        realizar_compra()
    elif opcion == 5:
        seguimiento_compra()
    elif opcion == 6:
        print('Hasta luego')
        break
    else:
        print('Opcion no valida, pruebe otra vez')
