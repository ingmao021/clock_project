"""
Modelo de estado del reloj - Almacena el estado local del reloj
Separa los datos de la presentación
"""


class ClockState:
    """Representa el estado actual del reloj."""

    def __init__(self):
        """Inicializa el estado del reloj."""
        self.clock_hands_angles = {'hour': 90, 'minute': 90, 'second': 90}
        self.manual_mode = False
        self.manual_seconds = None
        self.hands_ends = (None, None, None)  # (hour_end, minute_end, second_end)
        self.selected_country = "Colombia"  # País por defecto

    def set_angles(self, hour, minute, second):
        """
        Establece los ángulos de las manecillas.

        Args:
            hour: Ángulo en grados de la manecilla de horas
            minute: Ángulo en grados de la manecilla de minutos
            second: Ángulo en grados de la manecilla de segundos
        """
        self.clock_hands_angles = {
            'hour': hour,
            'minute': minute,
            'second': second
        }

    def set_angles_dict(self, angles_dict):
        """
        Establece los ángulos desde un diccionario.

        Args:
            angles_dict: Dict con 'hour', 'minute', 'second'
        """
        self.clock_hands_angles = angles_dict.copy()

    def get_angles(self):
        """
        Obtiene los ángulos actuales.

        Returns:
            Dict con 'hour', 'minute', 'second'
        """
        return self.clock_hands_angles.copy()

    def set_manual_mode(self, enabled, manual_seconds=None):
        """
        Cambia el modo manual.

        Args:
            enabled: True/False para habilitar o deshabilitar
            manual_seconds: Segundos en modo manual (opcional)
        """
        self.manual_mode = enabled
        self.manual_seconds = manual_seconds

    def is_manual_mode(self):
        """
        Verifica si está en modo manual.

        Returns:
            True si está en modo manual
        """
        return self.manual_mode

    def set_hands_ends(self, hour_end, minute_end, second_end):
        """
        Establece los puntos finales de las manecillas para detección de clics.

        Args:
            hour_end: Tupla (x, y) del final de la manecilla de horas
            minute_end: Tupla (x, y) del final de la manecilla de minutos
            second_end: Tupla (x, y) del final de la manecilla de segundos
        """
        self.hands_ends = (hour_end, minute_end, second_end)

    def get_hands_ends(self):
        """
        Obtiene los puntos finales de las manecillas.

        Returns:
            Tupla (hour_end, minute_end, second_end)
        """
        return self.hands_ends

    def set_selected_country(self, country):
        """
        Establece el país seleccionado.

        Args:
            country: Nombre del país
        """
        self.selected_country = country

    def get_selected_country(self):
        """
        Obtiene el país seleccionado.

        Returns:
            Nombre del país
        """
        return self.selected_country

    def reset(self):
        """Reinicia el estado del reloj a valores por defecto."""
        self.clock_hands_angles = {'hour': 90, 'minute': 90, 'second': 90}
        self.manual_mode = False
        self.manual_seconds = None
        self.hands_ends = (None, None, None)
        self.selected_country = "Colombia"
