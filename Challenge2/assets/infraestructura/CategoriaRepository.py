import csv
import os

from assets.dominio.Categoria import Categoria

class CategoriaRepository: # Clase que maneja el repositorio de categorias
    def __init__(self, file_path):
        self.file_path = file_path
        self.categorias = []
        self.cargar_categorias()

    def cargar_categorias(self): # Carga las categorias desde el archivo
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader, None) # Salta la primera fila osea el encabezado
            for row in reader:
                if row:
                    self.categorias.append(Categoria(*row))

    def obtener_todos(self): # Obtiene todas las categorias
        return self.categorias

    def obtener_por_id(self, id): # Obtiene una categoria por id
        for c in self.categorias:
            if c.id == str(id):
                 return c
        return None
