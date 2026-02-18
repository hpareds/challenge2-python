class Factura:
    def __init__(self, id_factura, fecha, id_cliente, total, items=""):
        self.id_factura = id_factura
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.total = total
        self.items = items