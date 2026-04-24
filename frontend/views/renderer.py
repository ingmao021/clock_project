"""
Renderizador - Dibuja el reloj en la pantalla
Responsable de toda la visualización del reloj
"""
import pygame
import math
from frontend.utils.utils import polar_to_cartesian
from backend.domain.models.AnalogClockList import AnalogClockList
from frontend.config import ui_constants
from config.models import ClockModel, MODEL_DATA
from config import settings


class Renderer:
    """Dibuja el reloj en la pantalla."""

    def __init__(self, width, height, radius, model=ClockModel.CLASSIC):
        """
        Inicializa el renderizador.

        Args:
            width: Ancho de la pantalla
            height: Alto de la pantalla
            radius: Radio del reloj
            model: Modelo de reloj a usar
        """
        self.width = width
        self.height = height
        self.center = (width // 1.7, 250)
        self.radius = radius
        self.model = model
        self.config = settings.MODEL_CONFIGS[self.model]

        # Inicializar lista circular con números del reloj según modelo
        self.clock_numbers = AnalogClockList(MODEL_DATA[self.model])

    def set_model(self, model):
        """
        Cambia el modelo del reloj.

        Args:
            model: Nuevo modelo
        """
        self.model = model
        self.config = settings.MODEL_CONFIGS[self.model]
        self.clock_numbers = AnalogClockList(MODEL_DATA[self.model])

    def draw_clock_face(self, surface):
        """
        Dibuja la cara del reloj (fondo, borde, marcas y números).

        Args:
            surface: Superficie de pygame para dibujar
        """
        # Fondo del reloj
        pygame.draw.circle(surface, self.config["COLOR_CLOCK_FACE"], self.center, self.radius)

        # Borde del reloj
        pygame.draw.circle(surface, self.config["COLOR_CLOCK_BORDER"], self.center, self.radius, self.config["BORDER_WIDTH"])

        # Dibujar marcas de segundos (60 marcas)
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            x_start = self.center[0] + (self.radius - 20) * math.cos(angle)
            y_start = self.center[1] + (self.radius - 20) * math.sin(angle)
            x_end = self.center[0] + self.radius * math.cos(angle)
            y_end = self.center[1] + self.radius * math.sin(angle)

            # Las marcas cada 5 segundos son más gruesas
            if i % 5 == 0:
                tick_width = ui_constants.TICK_MAJOR_WIDTH
                color = self.config["COLOR_TICK_MAJOR"]
            else:
                tick_width = ui_constants.TICK_MINOR_WIDTH
                color = self.config["COLOR_TICK_MINOR"]

            pygame.draw.line(surface, color, (x_start, y_start), (x_end, y_end), tick_width)

        # Dibujar números del reloj
        font = pygame.font.SysFont(self.config["FONT_NAME"], ui_constants.FONT_SIZE, ui_constants.FONT_BOLD)
        numbers = self.clock_numbers.traverse()
        for i, num in enumerate(numbers):
            angle = math.radians(i * 30 - 90)
            x_pos = self.center[0] + (self.radius - 40) * math.cos(angle)
            y_pos = self.center[1] + (self.radius - 40) * math.sin(angle)
            text = font.render(str(num), True, self.config["COLOR_TICK_MAJOR"])
            surface.blit(text, text.get_rect(center=(x_pos, y_pos)))

    def draw_hands(self, surface, clock_hands_angles):
        """
        Dibuja las manecillas del reloj.

        Args:
            surface: Superficie de pygame para dibujar
            clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados

        Returns:
            Tupla (hour_end, minute_end, second_end) con los puntos finales
        """
        # Manecilla de horas
        hour_end = polar_to_cartesian(self.center, clock_hands_angles['hour'], self.radius * ui_constants.HOUR_HAND_LENGTH_RATIO)
        pygame.draw.line(surface, self.config["COLOR_HOUR_HAND"], self.center, hour_end, ui_constants.HOUR_HAND_WIDTH)

        # Manecilla de minutos
        minute_end = polar_to_cartesian(self.center, clock_hands_angles['minute'], self.radius * ui_constants.MINUTE_HAND_LENGTH_RATIO)
        pygame.draw.line(surface, self.config["COLOR_MINUTE_HAND"], self.center, minute_end, ui_constants.MINUTE_HAND_WIDTH)

        # Manecilla de segundos
        second_end = polar_to_cartesian(self.center, clock_hands_angles['second'], self.radius * ui_constants.SECOND_HAND_LENGTH_RATIO)
        pygame.draw.line(surface, self.config["COLOR_SECOND_HAND"], self.center, second_end, ui_constants.SECOND_HAND_WIDTH)

        # Centro del reloj (pin)
        pygame.draw.circle(surface, ui_constants.COLOR_CENTER_PIN, self.center, ui_constants.CENTER_PIN_RADIUS)

        return hour_end, minute_end, second_end

    def draw_country_selector(self, surface, selector, current_country):
        """
        Dibuja el selector de países.

        Args:
            surface: Superficie de pygame
            selector: Instancia de CountrySelector
            current_country: País actual
        """
        selector.draw(surface, current_country)

    def draw_model_selector(self, surface, selector, current_model):
        """
        Dibuja el selector de modelos.

        Args:
            surface: Superficie de pygame
            selector: Instancia de ModelSelector
            current_model: Modelo actual
        """
        selector.draw(surface, current_model)

    def draw_current_timezone(self, surface, current_display):
        """
        Dibuja el texto de la zona horaria actual.

        Args:
            surface: Superficie de pygame
            current_display: Nombre de la ciudad y país actual
        """
        font = pygame.font.SysFont(ui_constants.FONT_NAME, 7, ui_constants.FONT_BOLD)
        text = font.render(current_display, True, self.config["COLOR_CLOCK_FACE"])
        surface.blit(text, text.get_rect(center=(self.center[0], self.center[1] + self.radius - 30)))
