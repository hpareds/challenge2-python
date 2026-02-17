import csv
import sys
import os

# Agregamos la carpeta raíz del proyecto al path de Python si se ejecuta directamente
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)

from assets.dominio.Usuario import Usuario

class AutenticacionService:
    def __init__(self, usuario_repository):
        # Recibimos el repositorio para cumplir con la separación de capas
        self.repository = usuario_repository

    def login(self, username, password):
        # verificar campos vacios
        if not username.strip() or not password.strip():
            raise ValueError("El usuario y la contraseña no pueden estar vacíos.")

        # obtener usuarios de la lista
        usuarios = self.repository.obtener_todos()

        # buscar coincidencia de usuario y contraseña
        for usuario in usuarios:
            if usuario.username == username and usuario.password == password: 
                # retorna el objeto usuario completo
                return usuario 
        
        # si no hay usuario o no existe coincidencia de datos retorna None
        return None

    def actualizar_usuario(self, usuario):
        return self.repository.actualizar_usuario(usuario)

    def crear_usuario(self, nombres, apellidos, password, rol):
         # Generar ID simple
        usuarios = self.repository.obtener_todos()
        if usuarios:
            new_id = str(max([int(u.id) for u in usuarios]) + 1)
        else:
            new_id = "1"
        
        # Generar username: 2 primeras letras nombre + id
        username = f"{nombres[:2].upper()}{new_id}"
        
        # Crear usuario (primer ingreso True por defecto)
        nuevo_usuario = Usuario(new_id, nombres, apellidos, username, password, rol, "True")
        self.repository.usuarios.append(nuevo_usuario)
        self.repository.guardar_usuarios()
        return nuevo_usuario