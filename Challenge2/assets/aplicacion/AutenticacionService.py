
from assets.dominio.Usuario import Usuario

class AutenticacionService:
    def __init__(self, usuario_repository):
        # Recibimos el repositorio para cumplir con la separación de capas
        self.repository = usuario_repository

    def login(self, username, password):
        # verificar campos vacios
        if not username.strip() or not password.strip(): #verificamos que los campos no esten vacios
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
        return self.repository.actualizar_usuario(usuario) # Actualizamos el usuario en el archivo

    def crear_usuario(self, nombres, apellidos, password, rol):
         # Generar ID simple
        usuarios = self.repository.obtener_todos()
        if usuarios:
            new_id = str(max([int(u.id) for u in usuarios]) + 1) # Generamos el nuevo ID
        else:
            new_id = "1"
        
        # Generar username: 2 primeras letras nombre + id
        username = f"{nombres[:2].upper()}{new_id}" # Generamos el username
        
        # Crear usuario (primer ingreso True por defecto)
        nuevo_usuario = Usuario(new_id, nombres, apellidos, username, password, rol, "True") # Creamos el nuevo usuario
        self.repository.usuarios.append(nuevo_usuario) # Agregamos el nuevo usuario a la lista
        self.repository.guardar_usuarios() # Guardamos el nuevo usuario en el archivo
        return nuevo_usuario