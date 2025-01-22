from views import Gtk

class SearchPage(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Menu de Inserção")
        customer_button = Gtk.Button(label = "Buscar Cliente")
        customer_button.connect("clicked", lambda _: controller.navigate("customer_search"))
        product_button = Gtk.Button(label = "Buscar Produto")
        product_button.connect("clicked", lambda _: controller.navigate("product_search"))
        deal_button = Gtk.Button(label = "Buscar Venda")
        deal_button.connect("clicked", lambda _: controller.navigate("deal_search"))
        back_button = Gtk.Button(label="Voltar para Home")
        back_button.connect("clicked", lambda _: controller.navigate("home"))

        self.pack_start(label, True, True, 0)
        self.pack_start(customer_button, True, True, 0)
        self.pack_start(product_button, True, True, 0)
        self.pack_start(deal_button, True, True, 0)
        self.pack_start(back_button, False, False, 0)
