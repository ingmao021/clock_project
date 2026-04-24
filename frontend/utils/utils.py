"""
Utilidades matemáticas para el frontend
Funciones de conversión de coordenadas y detección de colisiones
"""
import math


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


def time_from_angles(clock_hands_angles):
    """
    Convierte ángulos de manecillas a tiempo (hora, minuto, segundo).

    Args:
        clock_hands_angles: Dict con 'hour', 'minute', 'second' en grados

    Returns:
        Tupla (hora, minuto, segundo) en formato 12 horas
    """
    hour = int(math.floor(clock_hands_angles["hour"] / 30)) % 12
    if hour == 0:
        hour = 12
    minute = int(math.floor(clock_hands_angles["minute"] / 6)) % 60
    second = int(math.floor(clock_hands_angles["second"] / 6)) % 60
    return hour, minute, second

