import os

from assets.interfaz.MenuCliente import MenuCliente
from assets.utilidades import limpiar_pantalla

class MenuPrincipal:
    def __init__(self, servicio_autenticacion, servicio_producto, servicio_categoria, servicio_compra):
        self.servicio_autenticacion = servicio_autenticacion
        self.compra_service = servicio_compra
        self.user_service = servicio_autenticacion 
        self.prod_service = servicio_producto
        self.cat_service = servicio_categoria

    def iniciar(self):
        while True:
            print("\n---SISTEMA DE SUPERMERCADO PYTHON---")
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.pantalla_login() #login
            elif opcion == "2":
                print("¡Hasta luego!") #salir
                break
            else:
                print("\nOpción inválida. Intente nuevamente.")

    def pantalla_login(self):
        limpiar_pantalla()
        print("\n--- INICIO DE SESIÓN ---")
        usuario = input("Usuario: ")
        password = input("Contraseña: ") # El sistema solicita usuario y contraseña

        try:
            # compara contra los datos cargados del CSV en clase UsuarioRepository
            usuario_logueado = self.servicio_autenticacion.login(usuario, password)
            
            if usuario_logueado:
                print(f"\n¡Bienvenido {usuario_logueado.nombres}!") 
                if usuario_logueado.rol == "Administrador":
                    self.abrir_menu_admin(usuario_logueado)
                elif usuario_logueado.rol == "Cliente":
                    self.abrir_menu_cliente(usuario_logueado)
            else:
                # si los datos son incorrectos, permite intentar nuevamente
                print("Error: Usuario o contraseña incorrectos.")
        
        except ValueError as e:
            # Manejo de campos vacíos u otros errores de validación 
            print(f"Error de validación: {e}")

    def abrir_menu_cliente(self, cliente):

        if cliente.primer_ingreso == "True": #valida si es el primer ingreso dell usuario al sistema
            print("\n*** PRIMER INGRESO DETECTADO ***")
            print("Debe cambiar su contraseña antes de continuar.") # Obliga a cambiar contraseña
            self.cambiar_contraseña_obligatorio(cliente)
        
        # mostrar menu despues del logueo (o cambio de contraseña)
        menu_cliente = MenuCliente(self.servicio_autenticacion, self.prod_service, self.compra_service, cliente)
        menu_cliente.iniciar() #llama al menu del cliente y se ejecutan las funciones del metodo

    def cambiar_contraseña_obligatorio(self, cliente):
        while True:
            nueva_contra= input("Ingrese nueva contraseña: ") 
            confirmar_contra = input("Confirme nueva contraseña: ")
            
            if nueva_contra and nueva_contra == confirmar_contra:
                cliente.password = nueva_contra
                cliente.primer_ingreso = "False"
                self.servicio_autenticacion.actualizar_usuario(cliente)
                print("Contraseña actualizada con éxito.")
                break # No se permite continuar sin completar esto 
            else:
                print("Las contraseñas no coinciden o están vacías. Reintente.")

    def abrir_menu_admin(self, admin_logueado):
        from assets.interfaz.MenuAdmin import MenuAdmin
        
        print(f"\nAccediendo como Administrador: {admin_logueado.nombres}")
        
        # Enlazamos pasando los servicios que el Admin realmente usará
        menu_admin = MenuAdmin(self.user_service, self.prod_service, self.cat_service)
        menu_admin.mostrar_menu()