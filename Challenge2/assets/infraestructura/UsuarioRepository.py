import csv
import os

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
                return True
        return False



