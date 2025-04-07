# Definimos una función que construye visualmente el tablero de juego
def tablero(tablero):
    # Inicializamos una cadena vacía para ir construyendo el tablero
    tablero_hecho = ""
    
    # Añadimos título y leyenda al tablero
    tablero_hecho += " _____Tic_Tac_Toe_Python_Version_1.0_____\n\n"
    tablero_hecho += " __Player1_==_'O'__&__Player2_=_'X'__\n"
    
    # Dibujamos la primera fila del tablero
    tablero_hecho += "┌───────────┬───────────┬───────────┐\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[0][0]}     │     {tablero[0][1]}     │     {tablero[0][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"
    
    # Dibujamos la segunda fila
    tablero_hecho += "├───────────┼───────────┼───────────┤\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[1][0]}     │     {tablero[1][1]}     │     {tablero[1][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"

    # Dibujamos la tercera fila
    tablero_hecho += "├───────────┼───────────┼───────────┤\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += f"│     {tablero[2][0]}     │     {tablero[2][1]}     │     {tablero[2][2]}     │\n"
    tablero_hecho += "│           │           │           │\n"
    tablero_hecho += "└───────────┴───────────┴───────────┘\n"
    
    # Devolvemos el tablero ya construido como string
    return tablero_hecho


# Definimos una función que verifica si hay un ganador o si hay empate
def verificar_victoria(tablero):
    # Recorremos filas y columnas para comprobar si hay 3 en línea
    for i in range(3):
        # Verificamos filas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' ':
            return f"Jugador {'1' if tablero[i][0] == 'X' else '2'} Ha Ganado!"  # Corrige la asignación del jugador
        # Verificamos columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' ':
            return f"Jugador {'1' if tablero[0][i] == 'X' else '2'} Ha Ganado!"  # Corrige la asignación del jugador

    # Verificamos diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return f"Jugador {'1' if tablero[0][0] == 'X' else '2'} Ha Ganado!"  # Corrige la asignación del jugador
    if tablero[2][0] == tablero[1][1] == tablero[0][2] and tablero[2][0] != ' ':
        return f"Jugador {'1' if tablero[2][0] == 'X' else '2'} Ha Ganado!"  # Corrige la asignación del jugador

    # Verificamos si hay empate (ninguna casilla vacía)
    if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
        return "Han Empatado"

    # Si no hay ganador ni empate, devolvemos cadena vacía
    return ""


# Función principal que controla el flujo del juego
def main():
    while True:  # Creamos un bucle para permitir reiniciar partidas
        # Inicializamos el tablero como una matriz de 3x3 vacía
        tablero_juego = [[' ' for _ in range(3)] for _ in range(3)]

        # Inicializamos variables para los jugadores
        jugador1_eleccion = ' '
        jugador2_eleccion = ' '

        # Solicitamos al jugador 1 que elija entre X u O
        print("Introduce si quieres ser 'X' o 'O': ")
        while True:
            eleccion = input().lower()
            if eleccion == 'x' or eleccion == 'o':
                # Convertimos a mayúsculas y asignamos símbolo a cada jugador
                jugador1_eleccion = eleccion.upper()
                jugador2_eleccion = 'O' if jugador1_eleccion == 'X' else 'X'
                break
            else:
                print("Has introducido un caracter no válido")

        turno = 0  # Contador de turnos
        while turno < 9:  # Máximo 9 movimientos en el tablero
            print(tablero(tablero_juego))  # Mostramos el tablero actual

            # Determinamos qué jugador tiene el turno
            jugador_actual = 1 if turno % 2 == 0 else 2
            print(f"Turno Jugador {jugador_actual}")

            while True:
                try:
                    # Pedimos al jugador que introduzca coordenadas
                    fila = int(input("Introduce la Fila (1-3): ")) - 1
                    columna = int(input("Introduce la Columna (1-3): ")) - 1

                    # Verificamos que la posición esté dentro del tablero
                    if 0 <= fila < 3 and 0 <= columna < 3:
                        # Verificamos que la casilla esté vacía
                        if tablero_juego[fila][columna] == ' ':
                            # Colocamos el símbolo del jugador correspondiente
                            if jugador_actual == 1:
                                tablero_juego[fila][columna] = jugador1_eleccion
                            else:
                                tablero_juego[fila][columna] = jugador2_eleccion
                            break
                        else:
                            print("¡Casilla ocupada, prueba otra!")
                    else:
                        print("¡Posición fuera de rango! Introduce un número entre 1 y 3.")
                except ValueError:
                    print("Entrada no válida. Por favor ingresa un número.")

            # Verificamos si alguien ha ganado o si hay empate
            resultado = verificar_victoria(tablero_juego)
            if resultado:
                print(tablero(tablero_juego))  # Mostramos el tablero final
                print(resultado)  # Mostramos el resultado
                break  # Terminamos la partida

            turno += 1  # Pasamos al siguiente turno

        # Preguntamos si se desea jugar una nueva partida
        jugar_nueva_partida = input("¿Deseas iniciar una nueva partida? (sí/no): ").lower()
        if jugar_nueva_partida != 'si':
            # Si no se quiere una nueva partida, preguntamos si se desea salir
            salir = input("¿Deseas salir? (sí/no): ").lower()
            if salir == 'si':
                print("¡Gracias por jugar!")  # Mensaje de despedida
                exit()  # Cerramos el programa por completo


# Llamamos a la función principal solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
