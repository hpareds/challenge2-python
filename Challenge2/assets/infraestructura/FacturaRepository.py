import csv
import os
from assets.dominio.Factura import Factura

class FacturaRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.facturas = []
        self.cargar_facturas()

    def cargar_facturas(self): # Carga las facturas desde el archivo
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'fecha', 'id_cliente', 'total', 'items'])
            return

        with open(self.file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None) 
            for row in reader:
                if row:
                    # id, fecha, id_cliente, total, items
                    items = row[4] if len(row) > 4 else ""
                    self.facturas.append(Factura(row[0], row[1], row[2], float(row[3]), items))

    def agregar(self, factura): # Agrega una factura a la lista
        self.facturas.append(factura)
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([factura.id_factura, factura.fecha, factura.id_cliente, factura.total, factura.items])

    def generar_nuevo_id(self): # Genera un nuevo id
        if not self.facturas:
            return "1" # Si no hay facturas retorna 1 como validacion
        try:
            max_id = max([int(f.id_factura) for f in self.facturas]) # Obtiene el maximo id
            return str(max_id + 1)
        except ValueError:
             return "1" # Si no hay facturas retorna 1 como validacion

    def obtener_todos(self): # Obtiene todas las facturas
        return self.facturas

    def obtener_por_cliente(self, id_cliente): # Obtiene todas las facturas de un cliente
        return [f for f in self.facturas if str(f.id_cliente) == str(id_cliente)]
