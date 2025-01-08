import random
from celdas import Celda

class Tablero:
    def __init__(self, tamaño, num_minas):
        self.tamaño = tamaño
        self.num_minas = num_minas
        self.area_tablero = [[Celda() for _ in range(tamaño)] for _ in range(tamaño)]
        self.juego_terminado = False 
        self.primera_jugada = True

    def _colocar_minas(self, excluir_fila=None, excluir_columna=None):
        minas_colocadas = 0
        while minas_colocadas < self.num_minas:
            fila = random.randint(0, self.tamaño - 1)
            columna = random.randint(0, self.tamaño - 1)
            if (fila == excluir_fila and columna == excluir_columna) or self.area_tablero[fila][columna].es_mina:
                continue
            self.area_tablero[fila][columna].es_mina = True
            minas_colocadas += 1

    def _calcular_numeros(self):
        for fila in range(self.tamaño):
            for columna in range(self.tamaño):
                if self.area_tablero[fila][columna].es_mina:
                    continue
                self.area_tablero[fila][columna].minas_alrededor = self._contar_minas_alrededor(fila, columna)

    def _contar_minas_alrededor(self, fila, columna):
        contador = 0
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < self.tamaño and 0 <= j < self.tamaño:
                    if self.area_tablero[i][j].es_mina:
                        contador += 1
        return contador

    def revelar(self, fila, columna):
        if self.juego_terminado:
            print("El juego ha terminado. Reinicia para jugar de nuevo.")
            return

        if self.area_tablero[fila][columna].marcada:
            print("No puedes revelar una celda marcada.")
            return

        if self.primera_jugada:
            self._colocar_minas(excluir_fila=fila, excluir_columna=columna)
            self._calcular_numeros()
            self.primera_jugada = False
            self._revelar_adyacentes_forzado(fila, columna)
            return

        self.area_tablero[fila][columna].revelada = True

        if self.area_tablero[fila][columna].es_mina:
            self.juego_terminado = True
            print("\n¡BOOM! Pisaste una mina. Fin del juego.")
            return

        if self.area_tablero[fila][columna].minas_alrededor == 0:
            self._revelar_adyacentes(fila, columna)

        if self._juego_ganado():
            self.juego_terminado = True
            print("\n¡Felicidades! Has ganado el juego.")

    def _revelar_adyacentes(self, fila, columna):
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < self.tamaño and 0 <= j < self.tamaño:
                    if not self.area_tablero[i][j].revelada and not self.area_tablero[i][j].es_mina:
                        self.area_tablero[i][j].revelada = True
                        if self.area_tablero[i][j].minas_alrededor == 0:
                            self._revelar_adyacentes(i, j)

    def _revelar_adyacentes_forzado(self, fila, columna):
        visitados = set()

        def dfs(fila, columna):
            if (fila, columna) in visitados:
                return
            visitados.add((fila, columna))

            if 0 <= fila < self.tamaño and 0 <= columna < self.tamaño:
                celda = self.area_tablero[fila][columna]
                celda.revelada = True
                if celda.minas_alrededor == 0:
                    for i in range(fila - 1, fila + 2):
                        for j in range(columna - 1, columna + 2):
                            if 0 <= i < self.tamaño and 0 <= j < self.tamaño:
                                dfs(i, j)

        dfs(fila, columna)

    def marcar(self, fila, columna):
        if self.area_tablero[fila][columna].revelada:
            print("No puedes marcar una celda ya revelada.")
            return
        self.area_tablero[fila][columna].marcada = not self.area_tablero[fila][columna].marcada

    def _juego_ganado(self):
        for fila in range(self.tamaño):
            for columna in range(self.tamaño):
                if not self.area_tablero[fila][columna].es_mina and not self.area_tablero[fila][columna].revelada:
                    return False
        return True

    def mostrar_tablero(self):
        for fila in self.area_tablero:
            print(" ".join(str(celda) for celda in fila))