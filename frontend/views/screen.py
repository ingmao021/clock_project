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

        # Inicializar lista de fondos
        self.backgrounds_paths = ui_constants.ASSET_BACKGROUNDS
        self.current_background_index = 0
        self.backgrounds = []
        self._load_all_backgrounds()

    def _load_all_backgrounds(self):
        """Carga todos los fondos disponibles."""
        self.backgrounds = []
        for path in self.backgrounds_paths:
            try:
                bg = pygame.image.load(path)
                bg = pygame.transform.scale(bg, (self.width, self.height))
                self.backgrounds.append(bg)
            except pygame.error as e:
                print(f"Aviso: No se pudo cargar el fondo {path}: {e}")
                self.backgrounds.append(None)

    def set_background(self, index):
        """
        Establece el fondo actual por índice.

        Args:
            index: Índice del fondo (0 a len(backgrounds)-1)
        """
        if 0 <= index < len(self.backgrounds):
            self.current_background_index = index

    def next_background(self):
        """Cambia al siguiente fondo (navegación cíclica)."""
        self.current_background_index = (self.current_background_index + 1) % len(self.backgrounds)

    def prev_background(self):
        """Cambia al fondo anterior (navegación cíclica)."""
        self.current_background_index = (self.current_background_index - 1) % len(self.backgrounds)

    @property
    def background(self):
        """Obtiene el fondo actual."""
        if self.backgrounds and self.current_background_index < len(self.backgrounds):
            return self.backgrounds[self.current_background_index]
        return None

    def draw_background(self):
        """Dibuja el fondo en la pantalla."""
        bg = self.background
        if bg:
            self.screen.blit(bg, (0, 0))

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

