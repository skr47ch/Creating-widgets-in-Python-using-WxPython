import wx
import FixResolution

APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        menubar = wx.MenuBar()
        file_menu =  wx.Menu()
        menubar.Append(file_menu, '&File')

        quit_menu_item = wx.MenuItem(file_menu, APP_EXIT, '&Quit\tCtrl+Q')
        file_menu.Append(quit_menu_item)
        self.Bind(wx.EVT_MENU, self.on_quit, id=APP_EXIT)

        self.SetMenuBar(menubar)


    def  on_quit(self, e):
        self.Close()

def main():
    app = wx.App()
    example = Example(None)
    example.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()