from datetime import datetime
from assets.dominio.Factura import Factura
from assets.dominio.DetalleFactura import DetalleFactura

class CompraService:
    def __init__(self, producto_service, factura_repo, detalle_repo):
        self.producto_service = producto_service
        self.factura_repo = factura_repo
        self.detalle_repo = detalle_repo

    def procesar_compra(self, cliente, carrito):
        # 1. Calcular total y generar ID de factura
        total_compra = sum(item['subtotal'] for item in carrito)
        # Generar ID (puedes usar la lógica de max(id)+1 que ya conoces)
        nueva_factura_id = self.factura_repo.generar_nuevo_id()
        
        # Generar resumen de items
        items_str = " | ".join([f"{i['producto'].nombre} (x{i['cantidad']})" for i in carrito])

        nueva_factura = Factura( # Creamos la factura
            id_factura=nueva_factura_id,
            fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Generamos la fecha con formato YYYY-MM-DD HH:MM:SS
            id_cliente=cliente.id,
            total=total_compra,
            items=items_str
        )

        # Guardar la factura (
        self.factura_repo.agregar(nueva_factura)

        # Procesar cada producto del carrito
        for item in carrito:
            producto = item['producto']
            cantidad = item['cantidad']

            # Bajar stock en el objeto y persistir en productos.csv
            producto.stock = str(int(producto.stock) - cantidad)
            self.producto_service.repository.actualizar(producto)

            # Crear y guardar el detalle
            nuevo_detalle = DetalleFactura(
                id=self.detalle_repo.generar_nuevo_id(),
                id_factura=nueva_factura_id,
                id_producto=producto.id,
                cantidad=cantidad,
                precio_unitario=producto.precio
            )
            self.detalle_repo.agregar(nuevo_detalle)

        return nueva_factura

    def obtener_historial_cliente(self, id_cliente): # Obtenemos el historial de compras de un cliente
        return self.factura_repo.obtener_por_cliente(id_cliente)