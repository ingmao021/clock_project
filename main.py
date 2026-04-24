"""
Punto de entrada principal de la aplicación
Ejecuta la aplicación del reloj analógico
"""
from frontend.clock_app import ClockApp


if __name__ == "__main__":
    app = ClockApp()
    app.run()

