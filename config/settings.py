"""
Configuración centralizada de la aplicación
Contiene constantes globales para colores, dimensiones y rutas
"""

# ==================== RESOLUCIÓN Y GEOMETRÍA ====================
APP_WIDTH = 900
APP_HEIGHT = 750
CLOCK_CENTER = (APP_WIDTH // 1.8, 250)
CLOCK_RADIUS = 140

# ==================== RUTAS DE ASSETS ====================
ASSET_ICON_PATH = "assets/reloj.png"
ASSET_BACKGROUND_PATH = "assets/fondo.jpg"
ASSET_BACKGROUNDS = [
    "assets/fondo.jpg",
    "assets/fondo1.jpg",
    "assets/fondo2.jpg",
    "assets/fondo3.jpg",
]

# ==================== COLORES (RGB) ====================
COLOR_CLOCK_FACE = (255, 250, 240)  # Beige claro (fondo del reloj)
COLOR_CLOCK_BORDER = (5, 25, 25)    # Azul oscuro (borde)
COLOR_TICK_MAJOR = (5, 25, 25)       # Azul oscuro (marcas principales)
COLOR_TICK_MINOR = (100, 100, 100)   # Gris (marcas menores)
COLOR_HOUR_HAND = (34, 139, 34)      # Verde oscuro
COLOR_MINUTE_HAND = (5, 25, 25)      # Azul oscuro
COLOR_SECOND_HAND = (153, 0, 0)      # Rojo oscuro
COLOR_CENTER_PIN = (5, 25, 25)       # Azul oscuro

# ==================== ESPESOR DE LÍNEAS ====================
TICK_MAJOR_WIDTH = 4
TICK_MINOR_WIDTH = 2
HOUR_HAND_WIDTH = 8
MINUTE_HAND_WIDTH = 6
SECOND_HAND_WIDTH = 2
CENTER_PIN_RADIUS = 10

# ==================== PROPORCIONES DE MANECILLAS ====================
HOUR_HAND_LENGTH_RATIO = 0.5
MINUTE_HAND_LENGTH_RATIO = 0.75
SECOND_HAND_LENGTH_RATIO = 0.9

# ==================== FUENTES ====================
FONT_NAME = "Times New Roman"
FONT_SIZE = 32
FONT_BOLD = True

# ==================== VELOCIDADES Y TIEMPOS ====================
FPS = 30
MOUSE_DETECTION_RADIUS = 10

# ==================== CONSTANTES DE TIEMPO ====================
SECONDS_PER_HOUR = 3600
SECONDS_PER_12_HOURS = 43200
DEGREES_PER_HOUR = 30        # 360 / 12
DEGREES_PER_MINUTE = 6       # 360 / 60
DEGREES_PER_SECOND = 6       # 360 / 60
DEGREES_PER_MINUTE_SECOND = 0.1  # Movimiento suave del minutero

# ==================== VENTANA ====================
WINDOW_TITLE = "Reloj Vintage"


# ==================== MODELOS DE RELOJ ====================
from config.models import ClockModel

MODEL_CONFIGS = {
    ClockModel.CLASSIC: {
        "COLOR_CLOCK_FACE": (255, 250, 240),  # Beige claro
        "COLOR_CLOCK_BORDER": (5, 25, 25),    # Azul oscuro
        "COLOR_TICK_MAJOR": (5, 25, 25),      # Azul oscuro
        "COLOR_TICK_MINOR": (100, 100, 100),  # Gris
        "COLOR_HOUR_HAND": (34, 139, 34),     # Verde oscuro
        "COLOR_MINUTE_HAND": (5, 25, 25),     # Azul oscuro
        "COLOR_SECOND_HAND": (153, 0, 0),     # Rojo oscuro
        "BORDER_WIDTH": 4,
        "FONT_NAME": "Times New Roman",
    },
    ClockModel.ROMAN: {
        "COLOR_CLOCK_FACE": (255, 250, 240),  # Beige claro
        "COLOR_CLOCK_BORDER": (5, 25, 25),    # Azul oscuro
        "COLOR_TICK_MAJOR": (5, 25, 25),      # Azul oscuro
        "COLOR_TICK_MINOR": (100, 100, 100),  # Gris
        "COLOR_HOUR_HAND": (34, 139, 34),     # Verde oscuro
        "COLOR_MINUTE_HAND": (5, 25, 25),     # Azul oscuro
        "COLOR_SECOND_HAND": (153, 0, 0),     # Rojo oscuro
        "BORDER_WIDTH": 4,
        "FONT_NAME": "Times New Roman",  # Podría cambiarse a fuente romana si disponible
    },
    ClockModel.BULOVA_VINTAGE: {
        "COLOR_CLOCK_FACE": (245, 245, 220),  # Beige crema
        "COLOR_CLOCK_BORDER": (184, 134, 11), # Dorado
        "COLOR_TICK_MAJOR": (184, 134, 11),   # Dorado
        "COLOR_TICK_MINOR": (169, 169, 169),  # Gris claro
        "COLOR_HOUR_HAND": (184, 134, 11),    # Dorado
        "COLOR_MINUTE_HAND": (184, 134, 11),  # Dorado
        "COLOR_SECOND_HAND": (139, 69, 19),   # Marrón
        "BORDER_WIDTH": 6,
        "FONT_NAME": "Times New Roman",
    },
    ClockModel.DECORATIVE_NO_FRAME: {
        "COLOR_CLOCK_FACE": (255, 255, 255),  # Blanco
        "COLOR_CLOCK_BORDER": (255, 255, 255),# Blanco (sin borde visible)
        "COLOR_TICK_MAJOR": (200, 200, 200),  # Gris claro
        "COLOR_TICK_MINOR": (220, 220, 220),  # Gris muy claro
        "COLOR_HOUR_HAND": (0, 0, 0),         # Negro
        "COLOR_MINUTE_HAND": (0, 0, 0),       # Negro
        "COLOR_SECOND_HAND": (100, 100, 100), # Gris
        "BORDER_WIDTH": 1,  # Borde muy delgado
        "FONT_NAME": "Arial",
    },
}
