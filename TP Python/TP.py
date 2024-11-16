productos = []
stock = []
while True:
    print("*********Menú de Inventario*********")
    print("1-Ingresar un producto")
    print("2-Mostrar productos")
    print("3-Salir")
    opcion=int(input("Ingresa una opción\n"))
    
    if opcion==1:
        print("***Agregar producto***")
        nombre = str(input("Ingresa el nombre del producto a agregar:\n"))
        productos.append(nombre)
        cant = int(input("Ingresa el stock del producto:\n"))
        stock.append(cant)
        input("Ingresaste un producto al Inventario\n***Presiona ENTER para volver al Menú***\n")
    elif opcion==2:
        #modicar el mostrar productos para que aparezca sin los corchetes y vincular el prod con el stock
        print("***Lista de productos***")
        print(productos,stock)
        input("***Presiona ENTER para volver al Menú***")
    elif opcion==3:
        break
    else:
        input("Ingresaste una opción incorrecta - Presiona ENTER para volver al Menú\n")
        continue
print("Saliste del Menú, saludos!!")
