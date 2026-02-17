class CategoriaService:
    def __init__(self, categoria_repository):
        self.repository = categoria_repository

    def obtener_todas(self):
        return self.repository.obtener_todos()

    def existe_categoria(self, id):
        return self.repository.obtener_por_id(id) is not None
