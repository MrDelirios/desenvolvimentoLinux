import gi
from view import View
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self):
        super().__init__()
   
class Home(Gtk.Window):
    @staticmethod
    def get_home_page():
        listbox = Gtk.ListBox()
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        insert_button = Gtk.Button(label="Inserir Registro")
        insert_button.connect("clicked", self.on_insert_button_clicked)
        container.pack_start(insert_button, True, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        search_button = Gtk.Button(label="Pesquisar Registro")
        search_button.connect("clicked", self.on_search_button_clicked)
        container.pack_start(search_button, True, True, 0)
        listbox.add(row) 
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        update_button = Gtk.Button(label="Atualizar Registro")
        update_button.connect("clicked", self.on_update_button_clicked)
        container.pack_start(update_button, True, True, 0)
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        delete_button = Gtk.Button(label="Apagar Registro")
        delete_button.connect("clicked", self.on_delete_button_clicked)
        container.pack_start(delete_button, True, True, 0)
        listbox.add(row)
        
        return listbox
        
    def on_page_button_cliecked(self, message):
        pass

    def on_search_button_clicked(self, message):
        print("botão clicado") 

    def on_update_button_clicked(self, message):
        print("botão clicado")

    def on_delete_button_clicked(self, message):
        print("botão clicado")

                
win = Home()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

       
