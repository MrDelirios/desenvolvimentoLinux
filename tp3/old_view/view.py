import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="XINFRIN SYSTEMS")
        self.set_default_size(640, 480)
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        self.page_home = self.create_home_page()
        self.page_insert = self.create_insert_page()
        self.page_search = self.create_search_page()
        self.page_update = self.create_update_page()
        self.page_delete = self.create_delete_page()
        
        self.current_page = self.page_home
        self.add(self.current_page)

    def create_home_page(self):
        listbox = Gtk.ListBox()
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        insert_button = Gtk.Button(label="Inserir Registro")
        insert_button.connect("clicked", lambda _: self.switch_page(self.page_insert))
        container.pack_start(insert_button, True, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        search_button = Gtk.Button(label="Pesquisar Registro")
        search_button.connect("clicked", lambda _: self.switch_page(self.page_search))
        container.pack_start(search_button, True, True, 0)
        listbox.add(row) 
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        update_button = Gtk.Button(label="Atualizar Registro")
        update_button.connect("clicked", lambda _: self.switch_page(self.page_update))
        container.pack_start(update_button, True, True, 0)
        listbox.add(row)
        
        row = Gtk.ListBoxRow()
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(container)
        delete_button = Gtk.Button(label="Apagar Registro")
        delete_button.connect("clicked", lambda _: self.switch_page(self.page_delete))
        container.pack_start(delete_button, True, True, 0)
        listbox.add(row)
        
        return listbox

    def create_insert_page(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Esta é a Página Sobre.")
        button = Gtk.Button(label="Voltar para a Página Principal")
        button.connect("clicked", lambda _: self.switch_page(self.page_home))

        box.pack_start(label, True, True, 0)
        box.pack_start(button, False, False, 0)
        return box

    def create_search_page(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Esta é a Página Sobre.")
        button = Gtk.Button(label="Voltar para a Página Principal")
        button.connect("clicked", lambda _: self.switch_page(self.page_home))

        box.pack_start(label, True, True, 0)
        box.pack_start(button, False, False, 0)
        return box
    
    def create_update_page(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Esta é a Página Sobre.")
        button = Gtk.Button(label="Voltar para a Página Principal")
        button.connect("clicked", lambda _: self.switch_page(self.page_home))

        box.pack_start(label, True, True, 0)
        box.pack_start(button, False, False, 0)
        return box

    def create_delete_page(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Esta é a Página Sobre.")
        button = Gtk.Button(label="Voltar para a Página Principal")
        button.connect("clicked", lambda _: self.switch_page(self.page_home))

        box.pack_start(label, True, True, 0)
        box.pack_start(button, False, False, 0)
        return box
    
    def switch_page(self, new_page):
        self.remove(self.current_page)
        self.current_page = new_page
        self.add(self.current_page)
        self.show_all()

