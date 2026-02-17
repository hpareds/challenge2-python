import csv
import sys
import os

# Agregamos la carpeta raíz del proyecto al path de Python si se ejecuta directamente
if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)

from assets.dominio.Usuario import Usuario

class UsuarioRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.usuarios = [] # Lista para cargar los datos al iniciar 
        self.cargar_desde_csv()
    
    def obtener_todos(self):
        return self.usuarios

    def cargar_desde_csv(self): #carga los usuarios desde el archivo csv

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.usuarios.append(Usuario(*row))

    def cargar_usuarios(self): #carga los usuarios desde el archivo csv
        with open('db/usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.usuarios.append(Usuario(*row))

    def guardar_usuarios(self): #guarda los usuarios en el archivo csv
        with open('db/usuarios.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nombres', 'apellidos', 'username', 'password', 'rol', 'primer_ingreso'])
            for usuario in self.usuarios:
                writer.writerow([usuario.id, usuario.nombres, usuario.apellidos, usuario.username, usuario.password, usuario.rol, usuario.primer_ingreso])

    def obtener_usuario_por_username(self, username): #obtiene el usuario por username
        for usuario in self.usuarios:
            if usuario.username == username: #Compara el username del usuario con el username proporcionado
                return usuario
        return None

    def actualizar_usuario(self, usuario): #actualiza el usuario
        for i, u in enumerate(self.usuarios): #Recorre la lista de usuarios
            if u.id == usuario.id: #Compara el id del usuario con el id proporcionado
                self.usuarios[i] = usuario
                self.guardar_usuarios()
                return True
        return False

# Bloque de prueba
if __name__ == "__main__":
    # Ruta relativa desde la raíz del proyecto, asumiendo que el script ajustó el path
    # Pero para cargar el archivo, necesitamos la ruta correcta relativa a donde se ejecuta o absoluta
    # Si ejecutamos este archivo directamente, la ruta 'db/usuarios.csv' debe ser relativa a CWD (Challenge2)
    # Como el CWD es Challenge2, funcionará.
    
    try:
        repo = UsuarioRepository("db/usuarios.csv")
        print("\n--- Usuarios Cargados ---")
        for u in repo.obtener_todos():
            print(f"User: {u.username}, Rol: {u.rol}, Nombre: {u.nombres}")
    except Exception as e:
        print(f"Error cargando usuarios: {e}")

