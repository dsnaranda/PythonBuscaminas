from juego import Juego

class Jugador:
    def __init__(self):
        pass

    def iniciar_juego(self, tamaño, num_minas):
        juego = Juego(tamaño, num_minas)
        juego.jugar()

if __name__ == "__main__":
    jugador = Jugador()
    jugador.iniciar_juego(5, 2)