"""
Servicio de reloj - Orquestación de la lógica del reloj
Gestiona sincronización, modo manual y estado general
"""
from backend.services.time_service import TimeService
from backend.services.timezone_service import TimezoneService


class ClockService:
    """Servicio que orquesta la lógica del reloj."""

    def __init__(self):
        """Inicializa el servicio del reloj."""
        self.time_service = TimeService()
        self.timezone_service = TimezoneService()
        self.manual_mode = False
        self.manual_seconds = None

    def update_from_system(self):
        """
        Actualiza los ángulos basado en la hora del sistema.

        Returns:
            Dict con 'hour', 'minute', 'second' en grados
        """
        self.manual_mode = False
        self.manual_seconds = None
        return self.time_service.get_system_time_angles(self.timezone_service.current_timezone)

    def start_manual_mode(self, clock_hands_angles):
        """
        Inicia el modo manual desde los ángulos actuales.

        Args:
            clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados
        """
        self.manual_mode = True
        self.manual_seconds = self.time_service.angles_to_seconds(clock_hands_angles)

    def update_manual_mode(self, delta_time):
        """
        Actualiza el tiempo en modo manual.

        Args:
            delta_time: Incremento de tiempo en segundos

        Returns:
            Dict con nuevos ángulos
        """
        if not self.manual_mode or self.manual_seconds is None:
            return None

        self.manual_seconds = self.time_service.advance_time_seconds(
            self.manual_seconds,
            delta_time
        )
        return self.time_service.seconds_to_angles(self.manual_seconds)

    def update_angle(self, hand_type, angle):
        """
        Actualiza un ángulo específico de una manecilla.

        Args:
            hand_type: 'hour', 'minute' o 'second'
            angle: Nuevo ángulo en grados
        """
        # Este método se usa cuando se arrastra una manecilla
        # Aquí se podría actualizar manualmente
        pass

    def reset_to_system_time(self):
        """
        Reinicia el reloj a la hora del sistema.

        Returns:
            Dict con ángulos actualizados a hora del sistema
        """
        return self.update_from_system()

    def end_drag_from_angles(self, clock_hands_angles):
        """
        Finaliza el arrastre y actualiza el modo manual.

        Args:
            clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados
        """
        if self.manual_mode:
            self.manual_seconds = self.time_service.angles_to_seconds(clock_hands_angles)

    def set_timezone(self, country_name):
        """
        Establece la zona horaria para un país.

        Args:
            country_name: Nombre del país
        """
        self.timezone_service.set_timezone(country_name)

    def get_current_country(self):
        """
        Obtiene el país actualmente seleccionado.

        Returns:
            Nombre del país
        """
        return self.timezone_service.get_current_country()

    def get_available_countries(self):
        """
        Obtiene la lista de países disponibles.

        Returns:
            Lista de países
        """
        return self.timezone_service.get_available_countries()
