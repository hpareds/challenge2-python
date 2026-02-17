import csv
import os
import sys

# Agregamos la carpeta raíz del proyecto al path de Python si se ejecuta directamente
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)

from assets.dominio.Producto import Producto

class ProductoRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.productos = []
        self.cargar_productos()

    def cargar_productos(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'nombre', 'precio', 'stock', 'id_categoria', 'activo'])
            return

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader, None) # Skip header
            for row in reader:
                if row:
                    self.productos.append(Producto(*row))

    def guardar_productos(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nombre', 'precio', 'stock', 'id_categoria', 'activo'])
            for p in self.productos:
                writer.writerow([p.id, p.nombre, p.precio, p.stock, p.id_categoria, p.activo])

    def obtener_todos(self):
        return self.productos

    def agregar(self, producto):
        self.productos.append(producto)
        self.guardar_productos()

    def actualizar(self, producto):
        for i, p in enumerate(self.productos):
            if p.id == producto.id:
                self.productos[i] = producto
                self.guardar_productos()
                return True
        return False

    def eliminar(self, id):
        for i, p in enumerate(self.productos):
            if p.id == id:
                del self.productos[i]
                self.guardar_productos()
                return True
        return False
