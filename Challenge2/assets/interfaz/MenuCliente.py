from assets.utilidades import limpiar_pantalla

class MenuCliente:
    def __init__(self, servicio_autenticacion, servicio_producto, servicio_compra, cliente):
        self.servicio_autenticacion = servicio_autenticacion
        self.producto_service = servicio_producto
        self.servicio_compra = servicio_compra
        self.cliente = cliente

    def iniciar(self):
        while True:
            print("\n---SISTEMA DE SUPERMERCADO PYTHON---")
            print("1. Ver productos") 
            print("2. Mis compras")
            print("3. Salir")          
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("\n---Listado de productos---")
                self.mostrar_listado()
                if input("\n¿Desea realizar una compra? (s/n): ").lower() == 's':
                    self.flujo_compra(self.cliente)
            
            elif opcion == "2":
                print("\n---Historial de compras---")
                facturas = self.servicio_compra.obtener_historial_cliente(self.cliente.id)
                if not facturas:
                    print("No has realizado compras aún.")
                else:
                    print(f"{'ID':<5} | {'Fecha':<20} | {'Total':<10} | {'Items'}")
                    print("-" * 80)
                    for f in facturas:
                        print(f"{f.id_factura:<5} | {f.fecha:<20} | ${f.total:<9} | {f.items}")
                input("Presione Enter para continuar...")
            elif opcion == "3":
                print("\nCerrando sesión cliente...")
                break
            else:
                print("\nOpción inválida. Intente nuevamente.")

        limpiar_pantalla()

    def mostrar_listado(self):
            print("\n--- LISTADO DE PRODUCTOS ---")
            # llamar metodo obtener_todos() producto_service
            productos = self.producto_service.obtener_todos()

            if not productos: #validar que haya productos
                print("No hay productos cargados en el sistema.")
                return

            # Imprimimos con formato para que se vea ordenado
            print(f"{'ID':<5} | {'Nombre':<20} | {'Precio':<10} | {'Stock':<5}")
            print("-" * 50)
            
            for p in productos:
                # mostrar solo si el producto está activo
                if p.activo == "True":
                    print(f"{p.id:<5} | {p.nombre:<20} | ${p.precio:<9} | {p.stock:<5}")

    def flujo_compra(self, cliente):
            carrito = []
            while True:
                id_prod = input("\nIngrese el ID del producto (o 'f' para finalizar): ")
                if id_prod.lower() == 'f': break

                # Buscar producto
                producto = next((p for p in self.producto_service.obtener_todos() if p.id == id_prod), None)
                
                if producto and producto.activo == "True":
                    try:
                        cantidad = int(input(f"Cantidad de {producto.nombre} (Stock: {producto.stock}): "))
                        if 0 < cantidad <= int(producto.stock):
                            subtotal = float(producto.precio) * cantidad
                            carrito.append({
                                'producto': producto,
                                'cantidad': cantidad,
                                'subtotal': subtotal
                            })
                            print(f"Agregado: {producto.nombre} x {cantidad} = ${subtotal}")
                        else:
                            print("Cantidad no válida o stock insuficiente.")
                    except ValueError:
                        print("Por favor, ingrese un número entero.")
                else:
                    print("Producto no encontrado.")

            if carrito:
                print("\n--- RESUMEN DE COMPRA ---")
                total = sum(item['subtotal'] for item in carrito)
                for i in carrito:
                    print(f"- {i['producto'].nombre} x {i['cantidad']}: ${i['subtotal']}")
                print(f"TOTAL A PAGAR: ${total}")

                if input("¿Confirmar pago? (s/n): ").lower() == 's':
                    factura = self.servicio_compra.procesar_compra(cliente, carrito)
                    print(f"\n¡Compra exitosa! ID de factura N° {factura.id_factura} generada.")
                    input("Presione Enter para continuar...")