from backend.domain.models.Time import Time


class AnalogClockList:
    # La ultima posicion se conecta de nuevo con el inicio, lo que facilita el recorrido cíclico
    def __init__(self):
        self.head = None  # La lista inicia vacía

    def insert(self, data):
        # Si la lista est vacía el nodo se auto-referencia en sus punteros next y prev
        new_node = Time(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node    # Como es el único nodo se apunta ael mismo
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node        # ultimo nodo apunta al nuevo nodo
            new_node.prev = last        # nuevo nodo apunta hacia atras
            new_node.next = self.head   # siguiente es la cabeza
            self.head.prev = new_node   # headd actualiza su puntero 'prev' al nuevo nodo

    def traverse(self):
        # Recorre la lista circular y devuelve una lista con los datos almacenados
        elements = []
        if not self.head:
            return elements
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements
