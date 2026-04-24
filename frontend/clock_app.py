"""
Aplicación principal del reloj analógico
Orquesta el loop principal y maneja la interacción general
"""
import pygame
from frontend.services.ui_service import UIService
from frontend.views.screen import Screen
from frontend.config import ui_constants


class ClockApp:
    """Aplicación principal del reloj analógico."""

    def __init__(self):
        """Inicializa la aplicación del reloj."""
        pygame.init()

        # Inicializar pantalla
        self.screen = Screen()

        # Inicializar servicio de UI
        self.ui_service = UIService(
            ui_constants.APP_WIDTH,
            ui_constants.APP_HEIGHT,
            ui_constants.CLOCK_RADIUS
        )
        self.ui_service.initialize()

        # Variables de control
        self.running = True
        self.last_update_time = pygame.time.get_ticks() / 1000.0

    def run(self):
        """Ejecuta el loop principal de la aplicación."""
        self.last_update_time = pygame.time.get_ticks() / 1000.0

        while self.running:
            # Calcular delta de tiempo
            current_time = pygame.time.get_ticks() / 1000.0
            delta_time = current_time - self.last_update_time
            self.last_update_time = current_time

            # Dibujar fondo
            self.screen.draw_background()

            # Actualizar lógica del reloj
            self.ui_service.update(delta_time)

            # Renderizar reloj
            self.ui_service.render(self.screen.get_surface())

            # Procesar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.ui_service.handle_event(event)

            # Actualizar pantalla
            self.screen.update()
            self.screen.tick(ui_constants.FPS)

        # Limpieza
        self.screen.quit()

