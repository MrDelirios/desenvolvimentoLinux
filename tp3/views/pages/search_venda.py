from views.pages.notification_page import NotificationPage
from views import Gtk

class SearchVenda(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.controller = controller
        label = Gtk.Label(label="Pesquisa de Venda")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text("Nome do Cliente")
        back_button = Gtk.Button(label="Cancelar")
        self.prod_name_entry = Gtk.Entry()
        self.prod_name_entry.set_text("Nome do Produto")
        back_button.connect("clicked", lambda _: self.controller.navigate("home"))
        ok_button = Gtk.Button(label="Confirmar")
        ok_button.connect("clicked", self.on_button_clicked)

        self.pack_start(label, True, True, 0)
        self.pack_start(self.name_entry, True, True, 0)
        self.pack_start(self.prod_name_entry, True, True, 0)
        self.pack_start(back_button, False, False, 0)
        self.pack_start(ok_button, False, False, 0)


    def on_button_clicked(self, button):
        nome = self.name_entry.get_text()
        nome_produto = self.prod_name_entry.get_text()
        result = self.controller.read_venda(nome, nome_produto)
        if result == []:
            message = "Venda não Encontrada"
        else:
            id_venda = result[0][0]
            qtde = result[0][1]
            valor_total = result[0][2]
            id_cliente = result[0][3]
            id_produto = result[0][4]
            message = f"Resultado da pesquisa \nId: {id_venda}\nQuantidade Comprada: {qtde}\nValor total: {valor_total}\nCliente: {nome}, id: {id_cliente}\nProduto Comprado: {nome_produto}, id: {id_produto}"
        dialog = NotificationPage(
            self.get_toplevel(),
            message
        )

        dialog.run_notification()
        self.controller.navigate("home")