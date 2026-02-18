class CategoriaService:
    def __init__(self, categoria_repository): # Inicializamos el servicio
        self.repository = categoria_repository # Inicializamos el repositorio

    def obtener_todas(self): # Obtenemos todas las categorias
        return self.repository.obtener_todos() 

    def existe_categoria(self, id): # Verificamos si existe una categoria
        return self.repository.obtener_por_id(id) is not None
