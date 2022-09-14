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
"""Variables que almacenan el stock ingresado"""
stock_camperas=[]
stock_sweters=[]
stock_accesorios=[]
stock_remeras=[]
stock_pantalones=[]


def ingreso_stock():
    """_summary_: Brinda un menú de opciones con categorías de ropa, 
    para que se pueda ingresar en la categoría adecuada el nuevo stock para la tienda.
    
    Args:   
        No recibe. 
    Returns:
        print: stock completo, con el producto nuevo ingresado.
    """

    print('\n \nIngreso de Stock\n')
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones\n")
    
    categoria= int(input('Seleccione una Categoría:\t'))

    ingreso=[]

    ingreso.append(input('Ingresar nombre del producto:\t'))
    ingreso.append(int(input('Ingresar cantidad de productos:\t')))
    ingreso.append(int(input('Ingresar costo:\t')))  

    if categoria== 1: 
        
        stock_camperas.extend(ingreso)
        print(stock_camperas)
    elif categoria == 2:
       
        stock_sweters.extend(ingreso)
        print(stock_sweters)  
    elif categoria == 3:
       
        stock_accesorios.extend(ingreso)
        print(stock_accesorios)
    elif categoria == 4:
        
        stock_remeras.extend(ingreso)
        print(stock_remeras)
    elif categoria == 5:
        
        stock_pantalones.extend(ingreso)
        print(stock_pantalones)
    else:
        print('Categoria no valida.')

    print("\n\nStock Total: \n")
    print('Camperas: \n' + str(stock_camperas))
    print('Sweters: \n' + str(stock_sweters))  
    print('Accesorios: \n' + str(stock_accesorios))  
    print('Remeras: \n' + str(stock_remeras))  
    print('Pantalones: \n' + str(stock_pantalones))     
    
   
    

# Lamado a ejecutar la función de menú principal.
menu()
