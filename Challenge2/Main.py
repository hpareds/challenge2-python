
# importamos los repositorios y servicios
from assets.infraestructura.UsuarioRepository import UsuarioRepository
from assets.infraestructura.ProductoRepository import ProductoRepository
from assets.infraestructura.CategoriaRepository import CategoriaRepository
from assets.aplicacion.AutenticacionService import AutenticacionService
from assets.aplicacion.ProductoService import ProductoService
from assets.aplicacion.CategoriaService import CategoriaService
from assets.aplicacion.CompraService import CompraService
from assets.infraestructura.FacturaRepository import FacturaRepository
from assets.infraestructura.DetalleFacturaRepository import DetalleFacturaRepository
from assets.interfaz.MenuPrincipal import MenuPrincipal

def main():
    # instanciamos los repositorios
    usuario_repo = UsuarioRepository("db/usuarios.csv")
    producto_repo = ProductoRepository("db/productos.csv")
    categoria_repo = CategoriaRepository("db/categorias.csv")
    factura_repo = FacturaRepository("db/facturas.csv")
    detalle_repo = DetalleFacturaRepository("db/item_facturas.csv")
    servicio_autenticacion = AutenticacionService(usuario_repo)
    servicio_producto = ProductoService(producto_repo)
    servicio_categoria = CategoriaService(categoria_repo)
    servicio_compra = CompraService(servicio_producto, factura_repo, detalle_repo)
    menu = MenuPrincipal(servicio_autenticacion, servicio_producto, servicio_categoria, servicio_compra)
    
    menu.iniciar()
    

if __name__ == "__main__":
    main()
