"""
Componente selector de modelos de reloj
Gestiona la lista de modelos y navegación
"""
import pygame
from frontend.config import ui_constants
from config.models import ClockModel


class ModelSelector:
    """Componente para seleccionar modelos de reloj."""

    def __init__(self, x, y, width, height):
        """
        Inicializa el selector de modelos.

        Args:
            x, y: Posición del selector
            width, height: Dimensiones
        """
        self.models = list(ClockModel)
        self.display_names = [model.value.replace('_', ' ').title() for model in self.models]
        self.current_index = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.expanded = False

        # Botón principal
        self.main_button = pygame.Rect(x, y, width, height)

        # Fuente
        self.font = pygame.font.SysFont(ui_constants.FONT_NAME, 20, ui_constants.FONT_BOLD)

    def draw(self, surface, current_model):
        """
        Dibuja el selector.

        Args:
            surface: Superficie de pygame
            current_model: Modelo actual
        """
        current_display = current_model.value.replace('_', ' ').title()
        # Botón principal
        pygame.draw.rect(surface, (200, 200, 200), self.main_button)
        pygame.draw.rect(surface, (0, 0, 0), self.main_button, 2)
        model_text = self.font.render(current_display, True, (0, 0, 0))
        surface.blit(model_text, model_text.get_rect(center=self.main_button.center))

        # Si está expandido, dibujar la lista
        if self.expanded:
            for i, display_name in enumerate(self.display_names):
                button_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                pygame.draw.rect(surface, (255, 255, 255), button_rect)
                pygame.draw.rect(surface, (0, 0, 0), button_rect, 1)
                text = self.font.render(display_name, True, (0, 0, 0))
                surface.blit(text, text.get_rect(center=button_rect.center))

    def handle_click(self, pos):
        """
        Maneja clics en los botones.

        Args:
            pos: Posición del clic (x, y)

        Returns:
            Modelo seleccionado o None
        """
        if self.main_button.collidepoint(pos):
            self.expanded = not self.expanded
            return None

        if self.expanded:
            for i, model in enumerate(self.models):
                button_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                if button_rect.collidepoint(pos):
                    self.expanded = False
                    return model

        return None

    def set_model(self, model):
        """Establece el modelo actual."""
        if model in self.models:
            self.current_index = self.models.index(model)
