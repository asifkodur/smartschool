import wx
import os,sys

class About(wx.Frame):
    def __init__(self, parent, id, title):
        
        
        wx.Frame.__init__(self, parent, id, title, size=(260, 200))
        
        self.ShowMe()
        self.Centre()
        
    def ShowMe(self):
        licence=""
        cur_dir=os.path.dirname(os.path.abspath((sys.argv[0])))
        description ="Smart School is a digital solution to school exam and result managemnt. It is part of an initiative to digitize the whole school activities"
        
        f=open(cur_dir+"/licences/licence",'r')
        for i in f.readlines():
            licence=licence+i
            
        
        

        info = wx.AboutDialogInfo()
        path=cur_dir+'/Resources/img/me.jpg'
        
        if os.path.exists(path):
            
            info.SetIcon(wx.Icon(path, wx.BITMAP_TYPE_JPEG))
        info.SetName('Smart School')
        info.SetVersion('2.0')
        info.SetDescription(description)
        info.SetCopyright('Copy Left')
        info.SetWebSite('asif.kodur@gmail.com')
        info.SetLicence(licence)
        info.AddDeveloper('Muhammed Asif Kodur\nGHSS Vythiri\nemail:<asif.kodur@gmail.com>')
        #info.AddDeveloper('\n\nGratitude to\nMaths Blog<http://mathematicsschool.blogspot.in/>')
        
        wx.AboutBox(info)
        self.Close()
        

if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    main_frame = About(None, wx.ID_ANY, "")
    app.SetTopWindow(main_frame)
    main_frame.Show()
    app.MainLoop()
