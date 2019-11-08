import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,-1, "Simple Menu Example")

        p = wx.Panel(self)

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(380,380 ), wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0|wx.HSCROLL|wx.VSCROLL )
        self.m_textCtrl4.SetMinSize( wx.Size( -1,220 ) )

        bSizer9.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )


        self.m_panel5.SetSizer( bSizer9 )
        self.m_panel5.Layout()

        menu1 = wx.Menu()
        simple = menu1.Append(-1, "Simple menu item")
        menu1.AppendSeparator()
        exit = menu1.Append(-1, "Exit")

        menu2 = wx.Menu()
        simple2 = menu2.Append(-1, "Simple menu item2")
        menu2.AppendSeparator()
        exit = menu2.Append(-1, "Exit2")


        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar = wx.MenuBar()
        menuBar.Append(menu1, "Simple Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self, event):
        wx.MessageBox("You selected the simple menu item")

    def OnExit(self, event):
        self.Close()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
