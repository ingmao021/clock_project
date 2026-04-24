"""
Servicio de tiempo - Gestiona la lógica de conversión de tiempo
Responsable de sincronizar con hora del sistema y conversiones
"""
import time
from backend.utils.converters import angles_to_time_seconds, time_seconds_to_angles
from config import settings


class TimeService:
    """Servicio que maneja toda la lógica relacionada con el tiempo."""

    @staticmethod
    def get_system_time_seconds():
        """
        Obtiene los segundos actuales del sistema en formato 12 horas.

        Returns:
            Segundos totales (0-43200 para 12 horas)
        """
        t = time.localtime()
        hour = t.tm_hour % 12
        minute = t.tm_min
        second = t.tm_sec

        return hour * settings.SECONDS_PER_HOUR + minute * 60 + second

    @staticmethod
    def get_system_time_angles():
        """
        Obtiene los ángulos de las manecillas basado en la hora del sistema.

        Returns:
            Dict con 'hour', 'minute', 'second' en grados
        """
        t = time.localtime()
        sec = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12

        angles = {
            'second': sec * settings.DEGREES_PER_SECOND,
            'minute': minute * settings.DEGREES_PER_MINUTE + sec * settings.DEGREES_PER_MINUTE_SECOND,
            'hour': hour * settings.DEGREES_PER_HOUR + minute * 0.5
        }
        return angles

    @staticmethod
    def advance_time_seconds(total_seconds, delta_time):
        """
        Avanza el tiempo en modo manual.

        Args:
            total_seconds: Segundos actuales
            delta_time: Incremento de tiempo en segundos

        Returns:
            Nuevos segundos totales
        """
        new_seconds = total_seconds + delta_time
        return new_seconds % settings.SECONDS_PER_12_HOURS

    @staticmethod
    def seconds_to_angles(total_seconds):
        """
        Convierte segundos a ángulos de manecillas.

        Args:
            total_seconds: Segundos totales (0-43200 para 12 horas)

        Returns:
            Dict con ángulos de las manecillas
        """
        return time_seconds_to_angles(total_seconds)

    @staticmethod
    def angles_to_seconds(clock_hands_angles):
        """
        Convierte ángulos a segundos totales.

        Args:
            clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados

        Returns:
            Segundos totales
        """
        return angles_to_time_seconds(clock_hands_angles)

