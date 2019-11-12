
import wx

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Chat")
        panel = wx.Panel(self)

        my_sizer = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(panel, label="Input:")
        my_sizer.Add(lbl, 0, wx.ALL, 5)

        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    #----------------------------------------------------------------------
    def OnEnter(self, event):
        """"""
        text = self.txt.GetValue()
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
