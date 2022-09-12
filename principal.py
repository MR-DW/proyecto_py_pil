def menu():
    stock = iniciarVec()
    # print((stock))
    while(True):
        print("\n \n BIENVENIDO AL MENU CONTROL DE STOCK DE LA EMPRESA PIL: \n \n")
        print("Lista de opciones disponibles")
        print("1) Mostrar todos los productos disponibles")
        print("2) Mostrar producto por categoria")
        print("3) Realizar compra de stock")
        print("4) Realizar venta de stock")
        print("salir) Salir del menu \n")
        opcion = input("Ingrese la opcion de que desea consultar: ")
        if(opcion == "1"):
            mostrarTodo(stock)
        elif(opcion == "2"):
            mostrarUnaCate(stock)
        elif(opcion == "3"):
           ingreso_stock()

        elif(opcion == "4"):
            print(True)
        elif(opcion.upper == "SALIR"):
            break
        else:
            print("La opcion marcada no esta entre las opciones del menu")


def iniciarVec():
    vector = [[],[],[],[],[]]
    vector[0].append("Camperas")
    vector[1].append("Sweters")
    vector[2].append("Accesorios")
    vector[3].append("Remeras")
    vector[4].append("Pantalones")
    return(vector)


def mostrarTodo(matriz):
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            if(columna == 0):
                print("\n\n Esta categoria es: " + matriz[fila][columna])
            elif(False):
                  print(matriz[columna][fila].name + matriz[columna][fila].cantidad + matriz[columna][fila].precio)

def mostrarUnaCate(matriz):
    print("Que categoria quieres ver:")
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones")
    categoria = int(input("\n Ingrese la opcion que desea ver: "))
    print("")
    print("\n\n Esta categoria es: " + matriz[categoria-1][0])


    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            if(categoria - 1 == fila and columna != 0):
                print("Nada")
            elif(False):
                  print(matriz[columna][fila].name + matriz[columna][fila].cantidad + matriz[columna][fila].precio)


# Opción 3 del menú / Compra de stock

def ingreso_stock():
    
    ingreso =   {
                'producto': 'x1',
                'cantidad':'x2',
                'valor':  'x3'
                }
    stock_compra = {   'camperas':[],
                'sweters':[],
                'accesorios':[],
                'remeras':[],
                'pantalones':[]
            }

    print('\n \nIngreso de Stock\n')
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones")
    
    categoria = input('Seleccione una Categoría:\t')

    x1= input('Ingresar producto:\t')
    x2= int(input('Ingresar cantidad de productos:\t'))
    x3= int(input('Ingresar valor:\t'))

    # Añade un nuevo elemento al diccionario
    # >>> d['tres'] = 3
    # >>> d
    # {'uno': 1, 'dos': 2, 'tres': 3}

    if categoria == 1:
        stock_compra['camperas'][0] = x1,x2,x3
       
    elif categoria == 2:
        stock_compra[1][0].append(x1,x2,x3)
    elif categoria == 3:
        stock_compra[2][0].append(x1,x2,x3)
    elif categoria == 4:
        stock_compra[3][0].append(x1,x2,x3)
    elif categoria == 5:
        stock_compra[4][0].append(x1,x2,x3)

    

# Lamado a ejecutar la función de menú principal.
menu()
