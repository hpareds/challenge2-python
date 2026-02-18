import csv
import os

from assets.dominio.Producto import Producto

class ProductoRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.productos = []
        self.cargar_productos()

    def cargar_productos(self): # Carga los productos desde el archivo
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file: # escribe en el archivo 
                writer = csv.writer(file)
                writer.writerow(['id', 'nombre', 'precio', 'stock', 'id_categoria', 'activo'])
            return

        with open(self.file_path, 'r') as file: # Lee el archivo
            reader = csv.reader(file)
            next(reader, None) 
            for row in reader:
                if row:
                    self.productos.append(Producto(*row))

    def guardar_productos(self): # Guarda los productos en el archivo
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nombre', 'precio', 'stock', 'id_categoria', 'activo']) # encabezado
            for p in self.productos:
                writer.writerow([p.id, p.nombre, p.precio, p.stock, p.id_categoria, p.activo]) # escribe en el archivo

    def obtener_todos(self): # Obtiene todos los productos
        return self.productos

    def agregar(self, producto): # Agrega un producto
        self.productos.append(producto)
        self.guardar_productos()

    def actualizar(self, producto): # Actualiza un producto
        for i, p in enumerate(self.productos):
            if p.id == producto.id:
                self.productos[i] = producto
                self.guardar_productos()
                return True
        return False

    def eliminar(self, id): # Elimina un producto
        for i, p in enumerate(self.productos):
            if p.id == id:
                del self.productos[i]
                self.guardar_productos()
                return True
        return False
