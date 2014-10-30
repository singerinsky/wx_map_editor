 # -*- coding: utf-8 -*-
import wx
from MainFrame import * 
    

if __name__ == '__main__':
    app = wx.App(False)
    main_frame = MainFrame(None,"map editor")
    app.MainLoop()
    pass