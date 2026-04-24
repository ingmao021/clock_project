class Time:
    """
    Cada nodo almacena y tiene punteros que permiten recorrer la lista
    en ambas direcciones.
    """
    def __init__(self, data):
        self.data = data      # dato del nodo 
        self.next = None      # puntero al siguiente nodo
        self.prev = None      # puntero al nodo anterior
