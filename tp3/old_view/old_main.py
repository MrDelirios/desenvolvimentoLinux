import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from views import view
from view import View

if __name__ == "__main__":
    app = View()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()
