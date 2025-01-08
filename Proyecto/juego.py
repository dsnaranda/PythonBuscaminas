from buscaminas import Tablero

class Juego:
    def __init__(self, tamaño, num_minas):
        self.tablero = Tablero(tamaño, num_minas)

    def jugar(self):
        while not self.tablero.juego_terminado:
            self.tablero.mostrar_tablero()
            accion = input("\nElige una acción (revelar/marcar) y posición (fila columna): ").split()
            if len(accion) != 3:
                print("Entrada inválida. Intenta de nuevo.")
                continue

            accion_tipo, fila, columna = accion[0], int(accion[1]), int(accion[2])
            if accion_tipo == "revelar":
                self.tablero.revelar(fila, columna)
            elif accion_tipo == "marcar":
                self.tablero.marcar(fila, columna)
            else:
                print("Acción desconocida. Usa 'revelar' o 'marcar'.")
