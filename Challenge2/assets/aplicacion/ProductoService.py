
from assets.dominio.Producto import Producto

"dentro de esta clase esta el CRUD de productos"

class ProductoService:
    def __init__(self, producto_repository):
        self.repository = producto_repository

    def obtener_todos(self): #obtiene todos los productos
        return self.repository.obtener_todos()

    def crear_producto(self, nombre, precio, stock, id_categoria): #crea un producto
        # Generar ID simple (max id + 1)
        productos = self.repository.obtener_todos()
        if productos:
            new_id = str(max([int(p.id) for p in productos]) + 1) #obtiene el maximo id y le suma 1
        else:
            new_id = "1"
        
        # Activo por defecto True
        nuevo_producto = Producto(new_id, nombre, precio, stock, id_categoria, "True")
        self.repository.agregar(nuevo_producto)
        return nuevo_producto

    def desactivar_producto(self, id): #desactiva un producto
        for producto in self.repository.obtener_todos():
            if producto.id == id:
                producto.activo = "False" # asignar comom falso 
                self.repository.actualizar(producto)
                return True
        return False

    def actualizar_producto(self, id, nombre, precio, stock, id_categoria): #actualiza un producto
        for producto in self.repository.obtener_todos(): #recorre la lista de producto y cambia cada dato
            if producto.id == id:
                producto.nombre = nombre
                producto.precio = precio
                producto.stock = stock
                producto.id_categoria = id_categoria
                self.repository.actualizar(producto)
                return True
        return False
