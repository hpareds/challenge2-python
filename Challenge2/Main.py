import sys
import os

# Agregamos la carpeta raíz del proyecto al path de Python
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Ahora sí, tus imports normales
from assets.infraestructura.UsuarioRepository import UsuarioRepository
from assets.infraestructura.ProductoRepository import ProductoRepository
from assets.infraestructura.CategoriaRepository import CategoriaRepository
from assets.aplicacion.AutenticacionService import AutenticacionService
from assets.aplicacion.ProductoService import ProductoService
from assets.aplicacion.CategoriaService import CategoriaService
from assets.interfaz.MenuPrincipal import MenuPrincipal

def main():
    usuario_repo = UsuarioRepository("db/usuarios.csv")
    producto_repo = ProductoRepository("db/productos.csv")
    categoria_repo = CategoriaRepository("db/categorias.csv")
    
    servicio_autenticacion = AutenticacionService(usuario_repo)
    servicio_producto = ProductoService(producto_repo)
    servicio_categoria = CategoriaService(categoria_repo)
    
    # IMPORTANTE: Asegurate de pasar TODOS los servicios aquí
    menu = MenuPrincipal(servicio_autenticacion, servicio_producto, servicio_categoria)
    menu.iniciar()
    

if __name__ == "__main__":
    main()