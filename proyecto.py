# diccionario para poder mapear las columnas
col_mapa = { 
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
    }

# crear un tablero vacío
tamaño = [0] * 8
def crear_tablero_vacío():
    for i in range(len(tamaño)):
        tamaño[i] = ["  "] * 8
tablero = crear_tablero_vacío

# crear las piezas
dic_piezas_blancas = {
    "bP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "bC": [(7, 1), (7, 6)],
    "bT": [(7, 2), (7, 5)],
    "bA": [(7, 0), (7, 7)],
    "bD": [(7, 3)],
    "bR": [(7, 4)]
    }

dic_piezas_negras = {
    "nP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "nC": [(0, 1), (0, 6)],
    "nT": [(0, 2), (0, 5)],
    "nA": [(0, 0), (0, 7)],
    "nD": [(0, 3)],
    "nR": [(0, 4)]
    }

# poner piezas en el tablero
def poner_piezas(tablero):
    for pieza, squares in dic_piezas_blancas.items(): # Piezas blancas
        for square in squares:
               x, y = square[0], square[1]
               tablero[x][y] = pieza

    for pieza, squares in dic_piezas_negras.items(): # Piezas negras
        for square in squares:
               x, y = square[0], square[1]
               tablero[x][y] = pieza

# función para imprimir el tablero estandard
def tablero_estandard(tablero):
    for i, row in enumerate(tablero):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

# función para imprimir el menú principal        
def imprimir_menu():
    print("Escoja la opción deseada: ")
    print("1. Posición estandart inicial")
    print("2. Posición inventada")
    print("3. Salir")

# función para evaluar las opciones   
def evaluar_opcion(opcion, tablero):
    if opcion == "1":
        poner_piezas(tablero)
    elif opcion == "2":
        tablero_inventado(tablero)
    elif opcion == "3":
        print("Saliendo del programa")
        return True
    return False


# crear el tablero inventado
def tablero_inventado(tablero):
    for i, row in enumerate(tablero):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")






poner_piezas(tablero)

# creación del turno
turno = 1

while(True):
    tablero_estandard(tablero)
    print("")

    jugador = ""
    if turno % 2 == 1:
        jugador = "Blanco"
    else:
        jugador = "Negro"

    turno += 1

    print(f"Es el turno del jugador {jugador}")
    print("")
    break

# Mover piezas

pieza_a_mover = input("Ingrese la coordenada de la pieza que quiere mover: ")
coor_x, coor_y = pieza_a_mover[0], pieza_a_mover[1]
coor_x = col_mapa[coor_x]
coor_y = 8 - int(coor_y)
coor_x, coor_y = coor_y, coor_x

posicion = input("Ingrese la coordenada de la posición a la que quiere mover la pieza: ")
coor_final_x, coor_final_y = posicion[0], posicion[1]
coor_final_x = col_mapa[coor_final_x]
coor_final_y = 8 - int(coor_final_y)
coor_final_x, coor_final_y = coor_final_y, coor_final_x

jugada = tablero[coor_x][coor_y]
tablero[coor_x][coor_y] = " "
tablero[coor_final_x][coor_final_y] = jugada
