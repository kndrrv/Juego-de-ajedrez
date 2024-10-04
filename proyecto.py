# crear el tablero 8x8
tablero = [0] * 8

for i in range(len(tablero)):
        tablero[i] = ["__"] * 8

def tablero_estandard(tablero):
    for i, row in enumerate(tablero):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

tablero_estandard(tablero)

# crear las piezas 

dic_piezas_blancas = {
    "P": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    "C": [(7, 1), (7, 6)],
    "T": [(7, 2), (7, 5)],
    "A": [(7, 0), (7, 7)],
    "D": [(7, 3)],
    "R": [(7, 4)]
    }

dic_piezas_negras = {
    "P": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
    "C": [(0, 1), (0, 6)],
    "T": [(0, 2), (0, 5)],
    "A": [(0, 0), (0, 7)],
    "D": [(0, 3)],
    "R": [(0, 4)]
    }

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