from views import Gtk

class DeletePage(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Menu de Inserção")
        customer_button = Gtk.Button(label = "Apagar Cliente")
        customer_button.connect("clicked", lambda _: controller.navigate("customer_delete"))
        product_button = Gtk.Button(label = "Apagar Produto")
        product_button.connect("clicked", lambda _: controller.navigate("product_delete"))
        # deal_button = Gtk.Button(label = "Apagar Venda")
        # deal_button.connect("clicked", lambda _: controller.navigate("deal_delete"))
        back_button = Gtk.Button(label="Voltar para Home")
        back_button.connect("clicked", lambda _: controller.navigate("home"))

        self.pack_start(label, True, True, 0)
        self.pack_start(customer_button, True, True, 0)
        self.pack_start(product_button, True, True, 0)
        # self.pack_start(deal_button, True, True, 0)
        self.pack_start(back_button, False, False, 0)
