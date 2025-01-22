from views.pages.notification_page import NotificationPage
from views import Gtk

class SearchProduto(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.controller = controller
        label = Gtk.Label(label="Pesquisa de Cliente")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text("Nome do Produto")
        back_button = Gtk.Button(label="Cancelar")
        back_button.connect("clicked", lambda _: self.controller.navigate("home"))
        ok_button = Gtk.Button(label="Confirmar")
        ok_button.connect("clicked", self.on_button_clicked)

        self.pack_start(label, True, True, 0)
        self.pack_start(self.name_entry, True, True, 0)
        self.pack_start(back_button, False, False, 0)
        self.pack_start(ok_button, False, False, 0)


    def on_button_clicked(self, button):
        nome = self.name_entry.get_text()
        result = self.controller.read_produto(nome)
        if result == []:
            message = "Produto não Encontrado"
        else:
            id_produto = result[0][0]
            valor = result[0][2]
            message = f"Resultado da pesquisa \nId: {id_produto}\nNome: {nome}\nValor: {valor}"
        dialog = NotificationPage(
            self.get_toplevel(),
            message
        )

        dialog.run_notification()
        self.controller.navigate("home")