"""
Controlador de entrada - Maneja eventos del mouse y teclado
Responsable de detectar interacciones del usuario con el reloj
"""
import pygame
import math
from frontend.utils.utils import point_line_distance
from frontend.config import ui_constants


class InputHandler:
    """Maneja los eventos de entrada del usuario."""

    def __init__(self, center):
        """
        Inicializa el controlador de entrada.

        Args:
            center: Tupla (x, y) del centro del reloj
        """
        self.center = center
        self.active_hand = None

    def handle_event(self, event, clock_hands_angles, hands_ends):
        """
        Procesa un evento de pygame.

        Args:
            event: Evento de pygame
            clock_hands_angles: Dict con ángulos de manecillas
            hands_ends: Tupla (hour_end, minute_end, second_end)

        Returns:
            Tupla (action, data) donde action puede ser:
            - "reset": Reiniciar a hora del sistema
            - "start_manual": Iniciar arrastre de manecilla
            - "end_drag": Terminar arrastre
            - "update_angle": Actualizar ángulo durante arrastre
            - None, None: Sin acción
        """
        if event.type == pygame.KEYDOWN:
            return self._handle_keydown(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            return self._handle_mouse_down(event, clock_hands_angles, hands_ends)

        elif event.type == pygame.MOUSEBUTTONUP:
            return self._handle_mouse_up(event)

        elif event.type == pygame.MOUSEMOTION:
            return self._handle_mouse_motion(event)

        return None, None

    def _handle_keydown(self, event):
        """Maneja eventos de teclado."""
        if event.key == pygame.K_r:
            self.active_hand = None
            return "reset", None
        return None, None

    def _handle_mouse_down(self, event, clock_hands_angles, hands_ends):
        """Maneja cuando se presiona el botón del mouse."""
        mouse_pos = pygame.mouse.get_pos()
        hour_end, minute_end, second_end = hands_ends

        # Detectar qué manecilla fue clickeada (en orden: minuto, segundo, hora - por encima)
        if minute_end and point_line_distance(mouse_pos, self.center, minute_end) < ui_constants.MOUSE_DETECTION_RADIUS:
            self.active_hand = 'minute'
            return "start_manual", self.active_hand
        elif second_end and point_line_distance(mouse_pos, self.center, second_end) < ui_constants.MOUSE_DETECTION_RADIUS:
            self.active_hand = 'second'
            return "start_manual", self.active_hand
        elif hour_end and point_line_distance(mouse_pos, self.center, hour_end) < ui_constants.MOUSE_DETECTION_RADIUS:
            self.active_hand = 'hour'
            return "start_manual", self.active_hand

        return None, None

    def _handle_mouse_up(self, event):
        """Maneja cuando se suelta el botón del mouse."""
        if self.active_hand is not None:
            self.active_hand = None
            return "end_drag", None
        return None, None

    def _handle_mouse_motion(self, event):
        """Maneja el movimiento del mouse."""
        if self.active_hand is not None:
            mx, my = pygame.mouse.get_pos()
            angle = math.degrees(math.atan2(my - self.center[1], mx - self.center[0])) + 90
            if angle < 0:
                angle += 360
            return "update_angle", angle
        return None, None

