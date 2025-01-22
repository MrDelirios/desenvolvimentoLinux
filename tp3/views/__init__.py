# Importação da biblioteca gráfica
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Importação das views
from .main_view import MainView
from .pages import InsertPage, SearchPage, UpdatePage, DeletePage, NotificationPage, CreateCliente, CreateProduto, CreateVenda, SearchCliente, SearchProduto, SearchVenda, UpdateCliente, UpdateProduto, DeleteCliente, DeleteProduto
__all__ = ["MainView", 
           "InsertPage", 
           "SearchPage", 
           "UpdatePage", 
           "DeletePage", 
           "Gtk", 
           "NotificationPage", 
           "CreateCliente", 
           "CreateProduto", 
           "CreateVenda",
           "SearchCliente",
           "SearchProduto",
           "SearchVenda",
           "UpdateCliente", 
           "UpdateProduto",
           "DeleteCliente",
           "DeleteProduto"]