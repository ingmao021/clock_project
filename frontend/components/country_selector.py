"""
Componente selector de países
Gestiona la lista de países y navegación
"""
import pygame
from frontend.config import ui_constants


class CountrySelector:
    """Componente para seleccionar países."""

    def __init__(self, countries, display_names, x, y, width, height):
        """
        Inicializa el selector de países.

        Args:
            countries: Lista de países (claves)
            display_names: Lista de nombres para display (ciudades)
            x, y: Posición del selector
            width, height: Dimensiones
        """
        self.countries = countries
        self.display_names = display_names
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

    def draw(self, surface, current_display):
        """
        Dibuja el selector.

        Args:
            surface: Superficie de pygame
            current_display: Nombre a mostrar para el país actual
        """
        # Botón principal
        pygame.draw.rect(surface, (200, 200, 200), self.main_button)
        pygame.draw.rect(surface, (0, 0, 0), self.main_button, 2)
        country_text = self.font.render(current_display, True, (0, 0, 0))
        surface.blit(country_text, country_text.get_rect(center=self.main_button.center))

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
            País seleccionado o None
        """
        if self.main_button.collidepoint(pos):
            self.expanded = not self.expanded
            return None

        if self.expanded:
            for i, country in enumerate(self.countries):
                button_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                if button_rect.collidepoint(pos):
                    self.expanded = False
                    return country

        return None

    def set_country(self, country):
        """Establece el país actual."""
        if country in self.countries:
            self.current_index = self.countries.index(country)

