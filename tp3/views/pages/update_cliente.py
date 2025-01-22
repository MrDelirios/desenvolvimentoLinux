from views.pages.notification_page import NotificationPage
from views import Gtk

class UpdateCliente(Gtk.Box):
    def __init__(self, controller):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.controller = controller
        label = Gtk.Label(label="Página de Atualização de Cliente")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text("Nome do Cliente")
        self.cpf_entry = Gtk.Entry()
        self.cpf_entry.set_text("CPF do Cliente")
        self.end_entry = Gtk.Entry()
        self.end_entry.set_text("Novo Endereço do Cliente")
        back_button = Gtk.Button(label="Cancelar")
        back_button.connect("clicked", lambda _: self.controller.navigate("home"))
        ok_button = Gtk.Button(label="Confirmar")
        ok_button.connect("clicked", self.on_button_clicked)

        self.pack_start(label, True, True, 0)
        self.pack_start(self.name_entry, True, True, 0)
        self.pack_start(self.cpf_entry, True, True, 0)
        self.pack_start(self.end_entry, True, True, 0)
        self.pack_start(back_button, False, False, 0)
        self.pack_start(ok_button, False, False, 0)


    def on_button_clicked(self, button):
        nome = self.name_entry.get_text()
        cpf = self.cpf_entry.get_text()
        endereco = self.end_entry.get_text()
        message = self.controller.update_cliente(nome, cpf, endereco)
        dialog = NotificationPage(
            self.get_toplevel(),
            message
        )

        dialog.run_notification()
        self.controller.navigate("home")