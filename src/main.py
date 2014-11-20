 # -*- coding: utf-8 -*-
import wx
from MainFrame import * 
    

if __name__ == '__main__':
    print "start appliaction"
    app = wx.App(False)
    main_frame = MainFrame(None,"map editor")
    main_frame.Show()
    app.MainLoop()
    pass
