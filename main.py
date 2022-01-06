import wx
import os

class mainFrame(wx.Frame):
    def __init__(self, parent=None, title="test",size=(640,480)):
        # Create a basic frame here, cannot put stuffs
        wx.Frame.__init__(self,parent=parent,title=title,size=size)
        self.SetBackgroundColour(wx.Colour(255,255,255))

        # Create a basic container to put things
        panel = wx.Panel(self)

        # Based on the basic container, we can put things
        # wx.EXPAND: helps to fill up the max value

        # Panel1
        panel1 = wx.Panel(panel,pos=(0,0),size=(640/2,wx.EXPAND))
        panel1.SetBackgroundColour("yellow")

        # Panel2 with a message displayed
        panel2 = wx.Panel(panel,pos=(320,0),size=(wx.EXPAND,wx.EXPAND))
        # Panel2 message
        panel2_msg = wx.StaticText(parent=panel2, label="i am pannel 2",pos=(30,100))
        panel2_font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        panel2_msg.SetFont(panel2_font)

        # Panel2 background
        panel2.SetBackgroundColour("green")

if __name__ == "__main__":
    app = wx.App()
    frame = mainFrame()
    frame.Show()
    app.MainLoop()