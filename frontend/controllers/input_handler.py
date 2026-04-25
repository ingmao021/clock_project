"""
Controlador de entrada - Maneja eventos del mouse y teclado
Responsable de detectar interacciones del usuario con el reloj
"""
import pygame


class InputHandler:
    """Maneja los eventos de entrada del usuario."""

    def __init__(self, center):
        """
        Inicializa el controlador de entrada.

        Args:
            center: Tupla (x, y) del centro del reloj
        """
        self.center = center

    def handle_event(self, event, clock_hands_angles, hands_ends):
        """
        Procesa un evento de pygame.

        Args:
            event: Evento de pygame
            clock_hands_angles: Dict con ángulos de manecillas
            hands_ends: Tupla (hour_end, minute_end, second_end)

        Returns:
            Tupla (action, data) donde action puede ser:
            - "next_background": Siguiente fondo
            - "prev_background": Fondo anterior
            - None, None: Sin acción
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                return "next_background", None
            elif event.key == pygame.K_LEFT:
                return "prev_background", None

        return None, None

