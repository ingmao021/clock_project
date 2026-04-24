"""
Utilidades de conversión matemática para el reloj
Convierte entre sistemas de coordenadas y unidades de tiempo
"""
import math
from config import settings


def polar_to_cartesian(center, angle_deg, length):
    """
    Convierte coordenadas polares a cartesianas.

    Args:
        center: Tupla (x, y) del centro
        angle_deg: Ángulo en grados (0° = derecha, 90° = arriba)
        length: Distancia desde el centro

    Returns:
        Tupla (x, y) en coordenadas cartesianas
    """
    angle_rad = math.radians(angle_deg - 90)
    x = center[0] + length * math.cos(angle_rad)
    y = center[1] + length * math.sin(angle_rad)
    return (x, y)


def point_line_distance(pt, line_start, line_end):
    """
    Calcula la distancia perpendicular de un punto a una línea.

    Args:
        pt: Tupla (x, y) del punto
        line_start: Tupla (x, y) del inicio de la línea
        line_end: Tupla (x, y) del final de la línea

    Returns:
        Distancia mínima entre el punto y la línea
    """
    (px, py) = pt
    (x1, y1) = line_start
    (x2, y2) = line_end
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1)

    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

    if t < 0:
        return math.hypot(px - x1, py - y1)
    elif t > 1:
        return math.hypot(px - x2, py - y2)

    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    return math.hypot(px - proj_x, py - proj_y)


def angles_to_time_seconds(clock_hands_angles):
    """
    Convierte ángulos de manecillas a segundos totales (0-43200 para 12 horas).

    Args:
        clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados

    Returns:
        Segundos totales transcurridos en 12 horas
    """

    hour = int(math.floor(clock_hands_angles["hour"] / settings.DEGREES_PER_HOUR)) % 12
    minute = int(math.floor(clock_hands_angles["minute"] / settings.DEGREES_PER_MINUTE)) % 60
    second = int(math.floor(clock_hands_angles["second"] / settings.DEGREES_PER_SECOND)) % 60


    total_seconds = hour * settings.SECONDS_PER_HOUR + minute * 60 + second
    return total_seconds


def time_seconds_to_angles(total_seconds):
    """
    Convierte segundos totales a ángulos de manecillas.

    Args:
        total_seconds: Segundos totales (0-43200 para 12 horas)

    Returns:
        Dict con 'hour', 'minute', 'second' en grados
    """

    #Codigo antiguo si no funciona el nuevo dejar este
    total_seconds = total_seconds % settings.SECONDS_PER_12_HOURS

    hour_angle = (total_seconds % settings.SECONDS_PER_12_HOURS) / settings.SECONDS_PER_12_HOURS * 360
    minute_angle = ((total_seconds % 3600) / 3600) * 360
    second_angle = ((total_seconds % 60) / 60) * 360

    return {
        'hour': hour_angle,
        'minute': minute_angle,
        'second': second_angle
    }


