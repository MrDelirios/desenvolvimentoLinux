from views.pages.notification_page import NotificationPage
from views import Gtk

class CreateVenda(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.controller = controller
        label = Gtk.Label(label="Página de Inserção")
        self.qtde_entry = Gtk.Entry()
        self.qtde_entry.set_text("Quantidade Comprada")
        self.valor_total_entry = Gtk.Entry()
        self.valor_total_entry.set_text("Subtotal")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text("Nome do Cliente")
        self.prod_name_entry = Gtk.Entry()
        self.prod_name_entry.set_text("Nome do Produto")
        back_button = Gtk.Button(label="Cancelar")
        back_button.connect("clicked", lambda _: self.controller.navigate("home"))
        ok_button = Gtk.Button(label="Confirmar")
        ok_button.connect("clicked", self.on_button_clicked)

        self.pack_start(label, True, True, 0)
        self.pack_start(self.qtde_entry, True, True, 0)
        self.pack_start(self.valor_total_entry, True, True, 0)
        self.pack_start(self.name_entry, True, True, 0)
        self.pack_start(self.prod_name_entry, True, True, 0)
        self.pack_start(back_button, False, False, 0)
        self.pack_start(ok_button, False, False, 0)


    def on_button_clicked(self, button):
        qtde = self.qtde_entry.get_text()
        valor_total = self.valor_total_entry.get_text()
        nome = self.name_entry.get_text()
        prod_nome = self.prod_name_entry.get_text()
        message = self.controller.create_venda(qtde, valor_total, nome, prod_nome)
        dialog = NotificationPage(
            self.get_toplevel(),
            message
        )

        dialog.run_notification()
        self.controller.navigate("home")