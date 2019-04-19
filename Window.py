import wx

def main():
    app = wx.App()
    frame = wx.Frame(None, title='Simple application')
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()