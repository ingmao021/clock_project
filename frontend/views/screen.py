"""
Gestión de la pantalla de pygame
Centraliza la creación e inicialización de pantalla
"""
import pygame
from frontend.config import ui_constants


class Screen:
    """Gestiona la pantalla de pygame y sus recursos."""

    def __init__(self):
        """Inicializa la pantalla de pygame."""
        self.width = ui_constants.APP_WIDTH
        self.height = ui_constants.APP_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        # Cargar y configurar icono
        try:
            icon = pygame.image.load(ui_constants.ASSET_ICON_PATH)
            pygame.display.set_icon(icon)
        except pygame.error as e:
            print(f"Aviso: No se pudo cargar el icono: {e}")

        # Establecer título de la ventana
        pygame.display.set_caption(ui_constants.WINDOW_TITLE)

        # Cargar fondo
        try:
            self.background = pygame.image.load(ui_constants.ASSET_BACKGROUND_PATH)
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
        except pygame.error as e:
            print(f"Aviso: No se pudo cargar el fondo: {e}")
            self.background = None

    def draw_background(self):
        """Dibuja el fondo en la pantalla."""
        if self.background:
            self.screen.blit(self.background, (0, 0))

    def clear(self):
        """Limpia la pantalla con color negro."""
        self.screen.fill((0, 0, 0))

    def update(self):
        """Actualiza la pantalla (pygame.display.flip)."""
        pygame.display.flip()

    def tick(self, fps):
        """
        Controla la velocidad de fotogramas (FPS).

        Args:
            fps: Fotogramas por segundo deseados
        """
        self.clock.tick(fps)

    def get_surface(self):
        """
        Obtiene la superficie de pygame para dibujar.

        Returns:
            Objeto pygame.Surface
        """
        return self.screen

    def quit(self):
        """Finaliza pygame y cierra la ventana."""
        pygame.quit()

