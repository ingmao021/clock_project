"""
Servicio de UI - Orquesta las interacciones entre controladores y vistas
Responsable de coordinar el flujo de eventos y actualizaciones
"""
from frontend.models.clock_state import ClockState
from frontend.controllers.input_handler import InputHandler
from frontend.views.renderer import Renderer
from backend.services.clock_service import ClockService


class UIService:
    """Servicio que orquesta las interacciones del UI."""

    def __init__(self, width, height, radius):
        """
        Inicializa el servicio de UI.

        Args:
            width: Ancho de la pantalla
            height: Alto de la pantalla
            radius: Radio del reloj
        """
        self.state = ClockState()
        self.clock_service = ClockService()
        self.renderer = Renderer(width, height, radius)
        self.input_handler = InputHandler(self.renderer.center)

    def initialize(self):
        """Inicializa el estado del reloj con la hora del sistema."""
        angles = self.clock_service.update_from_system()
        self.state.set_angles_dict(angles)

    def handle_event(self, event):
        """
        Maneja un evento de entrada.

        Args:
            event: Evento de pygame

        Returns:
            String con la acción a realizar, o None
        """
        hands_ends = self.state.get_hands_ends()
        action, data = self.input_handler.handle_event(
            event,
            self.state.get_angles(),
            hands_ends
        )

        if action == "reset":
            self._handle_reset()
        elif action == "start_manual":
            self._handle_start_manual()
        elif action == "end_drag":
            self._handle_end_drag()
        elif action == "update_angle":
            self._handle_update_angle(data)

        return action

    def update(self, delta_time):
        """
        Actualiza la lógica del reloj.

        Args:
            delta_time: Tiempo transcurrido en segundos
        """
        if self.input_handler.active_hand is not None:
            # Pausa la actualización temporal durante el arrastre
            return
        # Si está en modo manual pero no se está arrastrando, continuar con el tiempo
        if self.state.is_manual_mode():
            angles = self.clock_service.update_manual_mode(delta_time)
            if angles:
                self.state.set_angles_dict(angles)
        else:
            # Modo automático: sincronizar con hora del sistema
            angles = self.clock_service.update_from_system()
            self.state.set_angles_dict(angles)

        """
        if self.state.is_manual_mode():
            angles = self.clock_service.update_manual_mode(delta_time)
            if angles:
                self.state.set_angles_dict(angles)
        else:
            angles = self.clock_service.update_from_system()
            self.state.set_angles_dict(angles)
        """

    def render(self, surface):
        """
        Dibuja el reloj en la pantalla.

        Args:
            surface: Superficie de pygame
        """
        self.renderer.draw_clock_face(surface)
        hands_ends = self.renderer.draw_hands(surface, self.state.get_angles())
        self.state.set_hands_ends(*hands_ends)

    def _handle_reset(self):
        """Maneja el reinicio a la hora del sistema."""
        self.clock_service.reset_to_system_time()
        angles = self.clock_service.update_from_system()
        self.state.set_angles_dict(angles)
        self.state.set_manual_mode(False)
        self.input_handler.active_hand = None

    def _handle_start_manual(self):
        """Maneja el inicio del modo manual."""
        self.state.set_manual_mode(True)
        self.clock_service.start_manual_mode(self.state.get_angles())

    def _handle_end_drag(self):
        """Maneja el final del arrastre de manecilla."""
        if self.state.is_manual_mode():
            self.clock_service.end_drag_from_angles(self.state.get_angles())

    def _handle_update_angle(self, angle):
        """
        Maneja la actualización de un ángulo durante arrastre.

        Args:
            angle: Nuevo ángulo en grados
        """

        hand = self.input_handler.active_hand
        if hand:
            angles = self.state.get_angles()
            angles[hand] = angle
            self.state.set_angles_dict(angles)


