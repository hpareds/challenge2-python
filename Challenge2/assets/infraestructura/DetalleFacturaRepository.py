import csv
import os
from assets.dominio.DetalleFactura import DetalleFactura

class DetalleFacturaRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.detalles = []

        self.cargar_detalles() 

    def cargar_detalles(self): # Carga los detalles desde el archivo
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'id_factura', 'id_producto', 'cantidad', 'precio_unitario'])
            return

    def agregar(self, detalle): # Agrega un detalle a la lista
        # detalle debe ser instancia de DetalleFactura
        self.detalles.append(detalle)
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            # id, id_factura, id_producto, cantidad, precio_unitario
            writer.writerow([detalle.id, detalle.id_factura, detalle.id_producto, detalle.cantidad, detalle.precio_unitario])

    def generar_nuevo_id(self):
        # Para generar ID, leemos el archivo para encontrar el maximo ID actual
        if not os.path.exists(self.file_path):
             return "1"
        
        ids = []
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None) # Salta la primera fila osea el encabezado
                for row in reader:
                    if row:
                        ids.append(int(row[0])) # Agrega el id a la lista
            
            if ids:
                return str(max(ids) + 1) # retorna nuevo id
            return "1"
        except (ValueError, IndexError):
            return "1"
