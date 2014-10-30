 # -*- coding: utf-8 -*-
import wx
import os
import common_util
import wx.grid


ID_MENU_FILE = 1001
ID_EDITOR    = 1002
ID_HELP      = 1003

ID_MENU_ITEM_SOURCE = 2001

ID_SOURCE_GRID      = 3001

class MainFrame(wx.Frame):

    def __init__(self, parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,600))
        self.init_menu_bar()
        
        self.Show(True)
        
    def init_menu_bar(self):
        self.menu_bar = wx.MenuBar()
        menu_bar_file_ = wx.Menu()
        menu_bar_file_.Append(ID_MENU_ITEM_SOURCE,u"导入素材文件夹",u"导入素材文件夹")
        wx.EVT_MENU(self, ID_MENU_ITEM_SOURCE, self.dispatch_event)  
        #menu_bar_file_.Append(ID_EDITOR,u"编辑",u"编辑")
        #menu_bar_file_.Append(ID_HELP,u"帮助",u"帮助")
        
        
        self.menu_bar.Append(menu_bar_file_,u'文件')
        self.SetMenuBar(self.menu_bar)
                #

        #self.menu_bar_editor_ = wx.MenuBar()
        #self.menu_bar_help_ = wx.MenuBar()  
    def dispatch_event(self,event):
        print "recive message from %d"%event.Id
        
        if event.Id == ID_MENU_ITEM_SOURCE :
            print "open the source folder"
            self.open_file_select()
        else:
            print "unkown event!"
        
    def open_file_select(self):
        file_select = wx.DirDialog(self,"open dir",os.getcwd(),style=wx.OPEN)
        dir_selected = ''
        if file_select.ShowModal() == wx.ID_OK: 
            dir_selected = file_select.GetPath()
            all_files = common_util.get_all_file_in_dir(dir_selected)
           
        file_select.Destroy()
        #pos_ = wx.Point(1,1)
        self.map_grid_ = wx.grid.Grid(self,ID_SOURCE_GRID,size=(300,1000))
        table_base = wx.grid.GridStringTable(0,2)
        table_base.SetColLabelValue(0,u'文件名')
        #table_base.AppendRows()
        index = 0
        for key ,value in all_files.items():
            print key
            table_base.AppendRows(1)
            table_base.SetValue(index,0,key)
            index = index + 1
            
        print table_base.GetColsCount(),table_base.GetRowsCount()
        print table_base.GetNumberCols(),table_base.GetNumberRows()
        self.map_grid_.SetTable(table_base)
        #self.map_grid_.AutoSize()
        #self.map_grid_.Show(False)
        
        
        
        
        
        
        