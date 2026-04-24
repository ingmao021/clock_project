class Time:
    """
    Cada nodo almacena y tiene punteros que permiten recorrer la lista
    en ambas direcciones.
    """
    def __init__(self, time_value ):
        # Representa un "instante" del reloj (por ejemplo: (hora, minuto, segundo))
        self.time_value  = time_value       # dato del nodo

        # Apunta al siguiente instante en el ciclo del reloj
        self.tick = None      # puntero al siguiente nodo

        # Apunta al instante anterior en el ciclo del reloj
        self.tack = None      # puntero al nodo anterior
