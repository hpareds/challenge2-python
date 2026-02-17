import csv
import os
import sys

# Agregamos la carpeta raíz del proyecto al path de Python si se ejecuta directamente
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)

from assets.dominio.Categoria import Categoria

class CategoriaRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.categorias = []
        self.cargar_categorias()

    def cargar_categorias(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader, None) # Skip header
            for row in reader:
                if row:
                    self.categorias.append(Categoria(*row))

    def obtener_todos(self):
        return self.categorias

    def obtener_por_id(self, id):
        for c in self.categorias:
            if c.id == str(id):
                 return c
        return None
