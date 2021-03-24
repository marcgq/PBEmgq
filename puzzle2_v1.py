import gi
from puzzle1_v1 import RfidReader
import threading
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib

      
class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10) 
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        logo_buf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename='LogoPuzzle2.png', width=400, height=400, preserve_aspect_ratio=True)
        self.logo = Gtk.Image.new_from_pixbuf(logo_buf)
        self.label = Gtk.Label()
        self.label.set_name("main_label")
        self.label.set_markup("Please, login with your university card")
        
        self.label2 = Gtk.Label()
        self.label2.set_name("name_label")
        self.label2.set_text("Marc Garcia Quirantes. PBE 2021")
        
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clear_window)
        vbox.pack_start(self.logo, True, True, 0)
        vbox.pack_start(self.label, True, True, 0)
        vbox.pack_start(self.button, True, True, 0)
        vbox.pack_start(self.label2, True, True, 0)
        
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("puzzle2.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
      
    def clear_window(self, button):
        self.label.set_markup("Please, login with your university card")
        global thread
        if not thread.isAlive():
            thread = threading.Thread(target=read_from_card)
            thread.start()
        
def read_from_card ():
    rf = RfidReader()
    uid = rf.read_uid()
    GLib.idle_add(window.label.set_markup, "UID: <b>"+uid+"</b>")

if __name__ == "__main__":
    thread = threading.Thread(target=read_from_card)
    thread.start()
    
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
    
