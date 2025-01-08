import pygame
from buscaminas import Tablero
from celdas import Celda

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (169, 169, 169)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Tamaño de la pantalla
TAM_CELDA = 40
ANCHO = 600
ALTO = 600

class Interfaz:
    def __init__(self, tamaño, num_minas):
        pygame.init()
        self.tamaño = tamaño
        self.num_minas = num_minas
        self.tablero = Tablero(tamaño, num_minas)
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Buscaminas")
        self.fuente = pygame.font.SysFont("arial", 20)

    def dibujar_tablero(self):
        for fila in range(self.tamaño):
            for columna in range(self.tamaño):
                x = columna * TAM_CELDA
                y = fila * TAM_CELDA
                celda = self.tablero.area_tablero[fila][columna]

                # Color de fondo de la celda
                if celda.revelada:
                    if celda.es_mina:
                        pygame.draw.rect(self.pantalla, ROJO, (x, y, TAM_CELDA, TAM_CELDA))
                    else:
                        pygame.draw.rect(self.pantalla, GRIS, (x, y, TAM_CELDA, TAM_CELDA))
                        if celda.minas_alrededor > 0:
                            texto = self.fuente.render(str(celda.minas_alrededor), True, NEGRO)
                            self.pantalla.blit(texto, (x + TAM_CELDA//4, y + TAM_CELDA//4))
                else:
                    pygame.draw.rect(self.pantalla, BLANCO, (x, y, TAM_CELDA, TAM_CELDA))
                    if celda.marcada:
                        pygame.draw.line(self.pantalla, NEGRO, (x, y), (x + TAM_CELDA, y + TAM_CELDA), 2)
                        pygame.draw.line(self.pantalla, NEGRO, (x + TAM_CELDA, y), (x, y + TAM_CELDA), 2)

                pygame.draw.rect(self.pantalla, NEGRO, (x, y, TAM_CELDA, TAM_CELDA), 2)

    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo
                    fila = event.pos[1] // TAM_CELDA
                    columna = event.pos[0] // TAM_CELDA
                    self.tablero.revelar(fila, columna)
                elif event.button == 3:  # Clic derecho
                    fila = event.pos[1] // TAM_CELDA
                    columna = event.pos[0] // TAM_CELDA
                    self.tablero.marcar(fila, columna)

        return True

    def iniciar_juego(self):
        # Lo que se va a hacer por cada iteración del juego
        jugando = True
        while jugando:
            self.pantalla.fill(BLANCO)
            jugando = self.manejar_eventos()
            self.dibujar_tablero()

            pygame.display.flip()

            if self.tablero.juego_terminado:
                pygame.time.delay(1000)
                break

        pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    interfaz = Interfaz(tamaño=10, num_minas=5)
    interfaz.iniciar_juego()
