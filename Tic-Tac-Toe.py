def tablero(tablero):
    tablero_hecho = ""
    tablero_hecho += " _____Tic_Tac_Toe_Python_Version_1.0_____\n\n"
    tablero_hecho += " __Player1_==_'O'__&__Player2_=_'X'__\n"
    tablero_hecho += "┌───────────┬───────────┬───────────┐\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[0][0]}     │     {tablero[0][1]}     │     {tablero[0][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += "├───────────┼───────────┼───────────┤\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[1][0]}     │     {tablero[1][1]}     │     {tablero[1][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += "├───────────┼───────────┼───────────┤\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[2][0]}     │     {tablero[2][1]}     │     {tablero[2][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += "└───────────┴───────────┴───────────┘\n"
    return tablero_hecho


def verificar_victoria(tablero):
    for i in range(3):
        # Verificar filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' ':
            return f"Jugador {'2' if tablero[i][0] == 'X' else '1'} Ha Ganado!"
        # Verificar columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' ':
            return f"Jugador {'2' if tablero[0][i] == 'X' else '1'} Ha Ganado!"
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return f"Jugador {'2' if tablero[0][0] == 'X' else '1'} Ha Ganado!"
    if tablero[2][0] == tablero[1][1] == tablero[0][2] and tablero[2][0] != ' ':
        return f"Jugador {'2' if tablero[2][0] == 'X' else '1'} Ha Ganado!"
    
    # Verificar empate
    if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
        return "Han Empatado"

    return ""  # No hay ganador ni empate


def main():
    tablero_juego = [[' ' for _ in range(3)] for _ in range(3)]
    jugador1_eleccion = ' '
    jugador2_eleccion = ' '

    print("Introduce si quieres ser 'X' o 'O': ")
    while True:
        eleccion = input().lower()
        if eleccion == 'x' or eleccion == 'o':
            jugador1_eleccion = eleccion.upper()
            jugador2_eleccion = 'O' if jugador1_eleccion == 'X' else 'X'
            break
        else:
            print("Has introducido un caracter no válido")

    for i in range(9):
        print(tablero(tablero_juego))
        resultado = ""

        if i % 2 == 0:
            # Turno jugador 1
            while True:
                try:
                    print("Turno Jugador 1")
                    fila = int(input("Introduce la Fila (1-3): ")) - 1
                    columna = int(input("Introduce la Columna (1-3): ")) - 1

                    if 0 <= fila < 3 and 0 <= columna < 3:
                        if tablero_juego[fila][columna] == ' ':
                            tablero_juego[fila][columna] = jugador1_eleccion
                            break
                        else:
                            print("¡Casilla ocupada, prueba otra!")
                    else:
                        print("¡Posición fuera de rango! Introduce un número entre 1 y 3.")
                except ValueError:
                    print("Entrada no válida. Por favor ingresa un número.")

        else:
            # Turno jugador 2
            while True:
                try:
                    print("Turno Jugador 2")
                    fila = int(input("Introduce la Fila (1-3): ")) - 1
                    columna = int(input("Introduce la Columna (1-3): ")) - 1

                    if 0 <= fila < 3 and 0 <= columna < 3:
                        if tablero_juego[fila][columna] == ' ':
                            tablero_juego[fila][columna] = jugador2_eleccion
                            break
                        else:
                            print("¡Casilla ocupada, prueba otra!")
                    else:
                        print("¡Posición fuera de rango! Introduce un número entre 1 y 3.")
                except ValueError:
                    print("Entrada no válida. Por favor ingresa un número.")

        # Verificar si hay un ganador o empate después de cada turno
        resultado = verificar_victoria(tablero_juego)
        if resultado:
            print(tablero(tablero_juego))  # Imprimir el tablero después de la victoria
            print(resultado)
            break

if __name__ == "__main__":
    main()
