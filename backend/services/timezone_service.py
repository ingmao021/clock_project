"""
Servicio de zonas horarias - Gestiona conversiones de tiempo entre zonas
Responsable de mapear países a zonas horarias y realizar conversiones
"""
import pytz
from datetime import datetime


class TimezoneService:
    """Servicio que gestiona zonas horarias y conversiones."""

    # Mapeo de países a zonas horarias
    COUNTRIES_TIMEZONES = {
        "USA (NY)": "America/New_York",
        "USA (LA)": "America/Los_Angeles",
        "UK": "Europe/London",
        "España": "Europe/Madrid",
        "Japón": "Asia/Tokyo",
        "China": "Asia/Shanghai",
        "India": "Asia/Kolkata",
        "Australia": "Australia/Sydney",
        "Brasil": "America/Sao_Paulo",
        "México": "America/Mexico_City",
        "Colombia": "America/Bogota",
    }

    # Mapeo de países a nombres de ciudades principales para display
    COUNTRIES_DISPLAY = {
        "USA (NY)": "New York, USA",
        "USA (LA)": "Los Angeles, USA",
        "UK": "London, UK",
        "España": "Madrid, España",
        "Japón": "Tokyo, Japón",
        "China": "Shanghai, China",
        "India": "Kolkata, India",
        "Australia": "Sydney, Australia",
        "Brasil": "São Paulo, Brasil",
        "México": "Mexico City, México",
        "Colombia": "Bogotá, Colombia",
    }

    def __init__(self):
        """Inicializa el servicio de zonas horarias."""
        self.current_timezone = pytz.UTC
        self.current_country = "Colombia"
        self.set_timezone(self.current_country)  # Establecer la zona horaria por defecto

    def get_available_countries(self):
        """
        Obtiene la lista de países disponibles.

        Returns:
            Lista de nombres de países
        """
        return list(self.COUNTRIES_TIMEZONES.keys())

    def get_timezone(self, country_name):
        """
        Obtiene el objeto timezone para un país.

        Args:
            country_name: Nombre del país

        Returns:
            Objeto pytz.timezone
        """
        if country_name in self.COUNTRIES_TIMEZONES:
            tz_name = self.COUNTRIES_TIMEZONES[country_name]
            return pytz.timezone(tz_name)
        return pytz.UTC

    def set_timezone(self, country_name):
        """
        Establece la zona horaria actual para un país.

        Args:
            country_name: Nombre del país
        """
        if country_name in self.COUNTRIES_TIMEZONES:
            self.current_timezone = self.get_timezone(country_name)
            self.current_country = country_name

    def get_current_country(self):
        """
        Obtiene el país actualmente seleccionado.

        Returns:
            Nombre del país
        """
        return self.current_country

    def get_time_for_timezone(self, timezone_obj):
        """
        Obtiene la hora actual en una zona horaria específica.

        Args:
            timezone_obj: Objeto pytz.timezone

        Returns:
            Objeto datetime con la hora en esa zona
        """
        utc_now = datetime.now(pytz.UTC)
        return utc_now.astimezone(timezone_obj)

    def get_current_time(self):
        """
        Obtiene la hora actual en la zona horaria seleccionada.

        Returns:
            Objeto datetime
        """
        return self.get_time_for_timezone(self.current_timezone)

    def get_utc_offset_string(self, country_name):
        """
        Obtiene el offset UTC como string para un país.

        Args:
            country_name: Nombre del país

        Returns:
            String con offset (ej: "UTC+5:30")
        """
        tz = self.get_timezone(country_name)
        now = datetime.now(tz)
        offset = now.strftime("%z")
        if offset:
            # Convertir "+0530" a "+05:30"
            return f"UTC{offset[:3]}:{offset[3:]}"
        return "UTC"

    def get_display_name(self, country_name):
        """
        Obtiene el nombre de la ciudad principal para display.

        Args:
            country_name: Nombre del país

        Returns:
            Nombre de la ciudad
        """
        return self.COUNTRIES_DISPLAY.get(country_name, country_name)
