import os

class MenuAdmin:
    def __init__(self, usuario_service, producto_service, categoria_service):
        self.usuario_service = usuario_service
        self.producto_service = producto_service
        self.categoria_service = categoria_service

    def mostrar_menu(self):
        while True:
            print("--- PANEL DE ADMINISTRADOR ---\n")
            print("1. Crear nuevo usuario")
            print("2. Gestión de productos")
            print("3. Informe de productos")
            print("4. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1": #crear usuario
                self.pantalla_crear_usuario()
            elif opcion == "2": #gestión de productos
                self.pantalla_gestion_productos()
            elif opcion == "3": #informe de productos
                self.pantalla_informes()
            elif opcion == "4": #cerrar sesión
                print("Cerrando sesión de administrador...")
                break
            else:
                print("Opción no válida.")

    # CREACIÓN DE USUARIOS
    def pantalla_crear_usuario(self): #solicita datos para crear usuario
        print("\n--- REGISTRO DE NUEVO USUARIO ---")
        nombres = input("Nombres: ") 
        apellidos = input("Apellidos: ") 
        password = input("Contraseña inicial: ") 
        
        print("Roles disponibles: 1. Cliente, 2. Administrador") #seleccionar rol de nuevo usuario
        rol_opc = input("Seleccione el rol: ")
        rol = "Administrador" if rol_opc == "2" else "Cliente" 

        if not nombres or not apellidos or not password: #validar campos vacios
            print("Error: Todos los campos son obligatorios.") 
            return

        # La lógica de generar ID y Username (Siglas+ID) debe estar en el Service
        nuevo_user = self.usuario_service.crear_usuario(nombres, apellidos, password, rol)
        print(f"\n¡Usuario creado con éxito!")
        print(f"Username generado: {nuevo_user.username}") #mensaje de usuario creado

    def mostrar_categorias(self):
        print("\nCategorías disponibles:")
        categorias = self.categoria_service.obtener_todas()
        for c in categorias:
            print(f"{c.id}. {c.nombre}")

    def solicitar_categoria_valida(self):
        self.mostrar_categorias()
        while True:
            id_categoria = input("ID Categoría (o 'cancelar'): ")
            if id_categoria.lower() == 'cancelar':
                return None
            if self.categoria_service.existe_categoria(id_categoria):
                return id_categoria
            print("ID de categoría no válido. Intente nuevamente.")

    # GESTIÓN DE PRODUCTOS (CRUD) 
    def pantalla_gestion_productos(self):
        while True:
            print("\n--- GESTIÓN DE PRODUCTOS ---")
            print("1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Volver")
            
            opc = input("Seleccione: ")

            if opc == "1":
                print("\n--- AGREGAR PRODUCTO ---")
                nombre = input("Nombre: ")
                precio = input("Precio: ")
                stock = input("Stock: ")
                
                id_categoria = self.solicitar_categoria_valida()
                if not id_categoria:
                    print("Operación cancelada.")
                    continue

                # Validar que no esten vacios
                if nombre and precio and stock and id_categoria:
                    self.producto_service.crear_producto(nombre, precio, stock, id_categoria)
                    print("Producto agregado con éxito.")
                else:
                     print("Error: Todos los campos son obligatorios.")

            elif opc == "2":
                print("\n--- ACTUALIZAR PRODUCTO ---")
                id_prod = input("ID del producto a actualizar: ")
                nombre = input("Nuevo Nombre: ")
                precio = input("Nuevo Precio: ")
                stock = input("Nuevo Stock: ")
                
                id_categoria = self.solicitar_categoria_valida()
                if not id_categoria:
                     print("Operación cancelada.")
                     continue
                
                if self.producto_service.actualizar_producto(id_prod, nombre, precio, stock, id_categoria):
                    print("Producto actualizado con éxito.")
                else:
                    print("Error: Producto no encontrado.")

            elif opc == "3":
                print("\n--- ELIMINAR PRODCUTO ---")
                id_prod = input("ID del producto a eliminar: ")
                if self.producto_service.desactivar_producto(id_prod):
                     print("Producto eliminado (desactivado) con éxito.")
                else:
                    print("Error: Producto no encontrado.")

            elif opc == "4":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida.")

    # INFORME DE PRODUCTOS 
    def pantalla_informes(self):
        print("\n--- INFORME DE INVENTARIO ---")
        # Listado general 
        productos = self.producto_service.obtener_todos()
        
        #imprime el listado general de productos en la consola en formato tabla 
        print(f"{'ID':<5} {'Nombre':<20} {'ID Cat':<15} {'Precio':<10} {'Stock':<5}") #encabezado
        for p in productos: #recorre la lista de productos e imprime
            print(f"{p.id:<5} {p.nombre:<20} {p.id_categoria:<15} ${p.precio:<9} {p.stock:<5}")

        # Productos agotados 
        print("\n--- PRODUCTOS AGOTADOS ---")
        agotados = [p for p in productos if str(p.stock) == "0"] #filtra los productos agotados (stock viene como string del csv)
        if not agotados: #si no hay productos agotados
            print("No hay productos agotados.")
        else: #si hay productos agotados
            for a in agotados: #recorre la lista de productos agotados e imprime
                print(f"- {a.nombre} (Cat: {a.id_categoria})")