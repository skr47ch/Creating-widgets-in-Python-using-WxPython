import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 200))
        self.Center()

def main():
    app = wx.App()
    example = Example(None, title='Example window')
    example.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()