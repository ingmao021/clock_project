from backend.domain.models.Time import Time


class AnalogClock:
    # Implementa un reloj analógico usando una lista doblemente enlazada circular
    def __init__(self, time_values):
        # Referencia al instante actual del reloj (inicio del ciclo)
        self.current_time = None

        # Si se proporcionan valores iniciales, se insertan en la estructura
        if time_values:
            for value in time_values:
                self.insert(value)

    def insert(self, time_value):
        """
       Inserta un nuevo instante en el reloj.

       - Si el reloj está vacío, el nodo se auto-referencia (circularidad).
       - Si ya existen nodos, se inserta al final del ciclo y se mantiene la estructura circular.
       """
        new_node = Time(time_value)

        # Caso 1: reloj vacío
        if not self.current_time:
            self.current_time = new_node

            # El nodo se apunta a sí mismo en ambas direcciones
            new_node.tick = new_node
            new_node.tack = new_node

        # Caso 2: reloj con instantes existentes
        else:
            # Último nodo del ciclo (el anterior al current_time)
            last = self.current_time.tack

            # Conectar el último nodo con el nuevo
            last.tick = new_node
            new_node.tack = last

            # Conectar el nuevo nodo con el inicio del ciclo
            new_node.tick = self.current_time
            self.current_time.tack = new_node

    def traverse(self):
        """
       Recorre el reloj de forma circular desde el instante actual.

       Retorna:
           list: Lista con los valores de tiempo almacenados en orden de recorrido.
       """
        elements = []

        # Si el reloj está vacío, retorna lista vacía
        if not self.current_time:
            return elements

        current = self.current_time

        # Recorre hasta volver al punto de inicio
        while True:
            elements.append(current.time_value)
            current = current.tick

            if current == self.current_time:
                break

        return elements

    def advance(self):
        """
        Avanza el reloj al siguiente instante (simula el paso del tiempo).
        """
        if self.current_time:
            self.current_time = self.current_time.tick