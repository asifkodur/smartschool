#!/usr/bin/env python2
import wx,os,sys
import gettext
from login import login
from disclaimer import disclaimer_win


if __name__ == "__main__":
    
    dir = os.path.split(sys.argv[0])[0]
    path=dir+'/.first_use'
    print path
    if  os.path.exists(path):
        
        dis_win=disclaimer_win(None,-1,'')
        dis_win.ShowModal()
        agree=dis_win.agree
        dis_win.Destroy()
        if not agree:
            sys.exit(0)
            
        else:
            os.remove(path)
            dis_win.Destroy()
            
            

    
    path="/tmp/.smart-lock"
    
    
    if not os.path.exists(path):
        
        open(path,'w')
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_1 = login(None, -1, "")
        app.SetTopWindow(frame_1)
        frame_1.Show()
        app.MainLoop()
        
        
       
    else:
        
        
        app = wx.PySimpleApp(0)
       
        dlg = wx.MessageDialog(None, 'Another instance of E-asy Exam Already Running.', '',wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
