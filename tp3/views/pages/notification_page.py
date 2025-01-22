from views import Gtk

class NotificationPage(Gtk.MessageDialog):
    def __init__(self, parent, message):
        super().__init__(
            transient_for=parent,
            flags=0,
            buttons=Gtk.ButtonsType.OK,
            text=message
        )

    def run_notification(self):
        self.run()
        self.destroy()
        