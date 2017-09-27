import wx
import os,sys

class About(wx.Dialog):
    def __init__(self, *args, **kwds):#(self, parent, id, title):
        
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX  | wx.STAY_ON_TOP | wx.FRAME_FLOAT_ON_PARENT | wx.TAB_TRAVERSAL

        wx.Dialog.__init__(self, *args, **kwds)
        #wx.Dialog.__init__(self, parent, id, title, size=(260, 200))
        
        self.ShowMe()
        self.Centre()
        
    def get_version(self):
        dir = os.path.split(sys.argv[0])[0]
        version_file_path=dir+"/current_version"
        with open(version_file_path, 'r') as f:
            return f.readline()
        
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
        info.SetVersion(str(self.get_version()))
        info.SetDescription(description)
        info.SetCopyright('Copy Left')
        info.SetWebSite('https://asifkodur.github.io/smartschool/')
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
    main_frame.ShowModal()
    main_frame.Destroy()
    app.MainLoop()
