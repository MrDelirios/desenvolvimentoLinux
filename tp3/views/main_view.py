from views import Gtk
from views.pages import InsertPage, SearchPage, UpdatePage, DeletePage, CreateProduto, CreateCliente, CreateVenda, SearchCliente, SearchProduto, SearchVenda, UpdateCliente, UpdateProduto, DeleteCliente, DeleteProduto

class MainView(Gtk.Window):
    def __init__(self, controller):
        super().__init__(title="XINFRIN SYSTEMS")
        self.controller = controller
        self.set_default_size(640, 480)
        self.set_border_width(10)
        # Stack -> Widget do Gtk em que montaremos nossas views
        self.stack = Gtk.Stack()
        self.add(self.stack)

        # Adiciona as páginas no Stack
        self.stack.add_named(self.create_home_page(), "home")
        self.stack.add_named(InsertPage(controller), "insert")
        self.stack.add_named(SearchPage(controller), "search")
        self.stack.add_named(UpdatePage(controller), "update")
        self.stack.add_named(DeletePage(controller), "delete")
        self.stack.add_named(CreateCliente(controller), "customer_create")
        self.stack.add_named(CreateProduto(controller), "product_create")
        self.stack.add_named(CreateVenda(controller), "deal_create")
        self.stack.add_named(SearchCliente(controller), "customer_search")
        self.stack.add_named(SearchProduto(controller), "product_search")
        self.stack.add_named(SearchVenda(controller), "deal_search")
        self.stack.add_named(UpdateCliente(controller), "customer_update")
        self.stack.add_named(UpdateProduto(controller), "product_update")
        self.stack.add_named(DeleteCliente(controller), "customer_delete")
        self.stack.add_named(DeleteProduto(controller), "product_delete")

    def create_home_page(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        # Botões de Navegação
        for label, page_name in [
            ("Inserir Registro", "insert"),
            ("Pesquisar Registro", "search"),
            ("Atualizar Registro", "update"),
            ("Apagar Registro", "delete"),
        ]:
            button = Gtk.Button(label = label)
            button.connect("clicked", lambda _, p=page_name: self.controller.navigate(p))
            box.pack_start(button, True, True, 0)

        return box
    
    def switch_page(self, page_name):
        # Muda a página visível no Stack
        self.stack.set_visible_child_name(page_name)

