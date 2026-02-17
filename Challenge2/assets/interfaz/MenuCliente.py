class MenuCliente:
    def __init__(self, servicio_autenticacion):
        self.servicio_autenticacion = servicio_autenticacion

    def iniciar(self):
        while True:
            print("SISTEMA DE SUPERMERCADO PYTHON")
            print("1. Ver productos") 
            print("2. Mis compras")
            print("3. Salir")          
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Listado de productos... (Pendiente)")
            elif opcion == "2":
                print("Historial de compras... (Pendiente)")
            elif opcion == "3":
                print("Cerrando sesión cliente...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")