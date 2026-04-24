"""
Modelos de reloj disponibles en la aplicación
"""
from enum import Enum


class ClockModel(Enum):
    CLASSIC = "Clasico"
    ROMAN = "Romano"
    BULOVA_VINTAGE = "Vintage"
    DECORATIVE_NO_FRAME = "Decorativo"


# Datos para cada modelo
MODEL_DATA = {
    ClockModel.CLASSIC: [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    ClockModel.ROMAN: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"],
    ClockModel.BULOVA_VINTAGE: [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  # Mismos números, estilo diferente
    ClockModel.DECORATIVE_NO_FRAME: [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  # Mismos números, estilo diferente
}
