#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Fri Sep 16 01:10:20 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
 
from threading import Thread
from wx.lib.pubsub import Publisher

from sampoorna import  sampoorna_reports,insert_to_db
 
########################################################################
class sampoorna_thread(Thread):
    
    #----------------------------------------------------------------------
    def __init__(self,user,passw,classes):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.user=user
        self.passw=passw
        self.classes=classes
        
        self.start()    # start the thread
 
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        SM=sampoorna_reports()
        login=SM.login(self.user,self.passw)
        if login[0]:
            wx.CallAfter(Publisher().sendMessage, "update","successful login")
            #print "successful login"
            SM.make_report_name("10")
            print SM.delete_report()
            print SM.create_report()

            first_page_link= SM.get_show_report_link()
            
            first_page_data=SM.get_page_wise_data(first_page_link)
            
            parser = html_parser()
            parser.feed_html(first_page_data,first_page=True)
            
            total_pages= parser.get_no_page() # returns the number of pages that report contains
            
            FULL_TABLE=[]

            parser.TABLE.remove([])
            FULL_TABLE=parser.TABLE
            
            # Downloading in Loop
            for i in range(1,total_pages+1,1): # This loops passes the other pages link to be processed and they will be appended to the table
                link=first_page_link+"?page="+str(i)
                
                parser.TABLE=[]
                data=SM.get_page_wise_data(link)
                
                parser.feed_html(data)
                
                table=parser.TABLE
                
                if table!=[]:
                
                    for item in table:
                        if item!=[]:
                            
                            FULL_TABLE.append(item)
            count=0

            
            sorted_list=SM.sort_by_div(FULL_TABLE)
            
            insert=insert_to_db()
            
            
            insert.insert_student(SM.year,sorted_list)
            print "newly inserted",insert.insert_count
            print "updated",insert.update_count
            insert.DB.Commit()
            SM.delete_report()
                        
                                
                            
                            
        else:
            print login[1]
            
            wx.CallAfter(Publisher().sendMessage, "update", "Thread finished!")
     
    #----------------------------------------------------------------------
    def postTime(self, amt):
        """
        Send time to GUI
        """
        amtOfTime = (amt + 1) * 10
        Publisher().sendMessage("update", amtOfTime)
 

class sampoorna_win(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: sampoorna_win.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.login_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_login = wx.Panel(self.login_pane, wx.ID_ANY)
        self.label_1 = wx.StaticText(self.panel_login, wx.ID_ANY, _("Warning: Always backup your database before you proceed to avoid potential data loss !!!"))
        self.label_2 = wx.StaticText(self.panel_login, wx.ID_ANY, _("This software does not save Sampoorna credentials. It is used for one time login"))
        self.panel_1 = wx.Panel(self.panel_login, wx.ID_ANY, style=wx.SUNKEN_BORDER | wx.RAISED_BORDER | wx.TAB_TRAVERSAL)
        self.label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Sampoorna Username"))
        self.text_ctrl_user = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER | wx.NO_BORDER)
        self.label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Sampoorna Password"))
        self.text_ctrl_passw = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD | wx.NO_BORDER)
        self.button_next = wx.Button(self.panel_login, wx.ID_ANY, _("Next >>"))
        self.standard_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.standard_pane, wx.ID_ANY, style=wx.SUNKEN_BORDER | wx.RAISED_BORDER | wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.checkbox_8 = wx.CheckBox(self.panel_3, wx.ID_ANY, _("8 Standard"))
        self.checkbox_9 = wx.CheckBox(self.panel_3, wx.ID_ANY, _("9 Standard"))
        self.checkbox_10 = wx.CheckBox(self.panel_3, wx.ID_ANY, _("10 Standard"))
        self.button_previous = wx.Button(self.standard_pane, wx.ID_ANY, _("<<Previous"))
        self.button_proceed = wx.Button(self.standard_pane, wx.ID_ANY, _("Proceed >>"))
        self.report_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_2 = wx.Panel(self.report_pane, wx.ID_ANY)
        self.label_7 = wx.StaticText(self.panel_2, wx.ID_ANY, _("Progress"))
        self.progresss_total = wx.Gauge(self.panel_2, wx.ID_ANY, range=100)
        self.progress_each = wx.Gauge(self.panel_2, wx.ID_ANY, range=100)
        self.label_satus = wx.StaticText(self.panel_2, wx.ID_ANY, _("Status"))
        self.list_ctrl_1 = wx.ListCtrl(self.panel_2, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_ALIGN_LEFT | wx.SUNKEN_BORDER | wx.NO_BORDER)
        self.button_finished = wx.Button(self.panel_2, wx.ID_ANY, _("Finished"))

        self.__set_properties()
        self.__do_layout()
        
        self.Bind(wx.EVT_TEXT, self.on_user_pass_text, self.text_ctrl_passw)
        self.Bind(wx.EVT_TEXT, self.on_user_pass_text, self.text_ctrl_user)
        self.Bind(wx.EVT_BUTTON, self.on_next, self.button_next)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.checkbox_8)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.checkbox_9)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.checkbox_10)
        self.Bind(wx.EVT_BUTTON, self.on_previous, self.button_previous)
        self.Bind(wx.EVT_BUTTON, self.on_proceed, self.button_proceed)
        self.Bind(wx.EVT_BUTTON, self.on_finished, self.button_finished)
        
        # create a pubsub receiver
        Publisher().subscribe(self.updateDisplay, "update")
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: sampoorna_win.__set_properties
        self.SetTitle(_("Import from Sampoorna"))
        self.SetSize((894, 640))
        self.label_1.SetForegroundColour(wx.Colour(204, 50, 50))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_2.SetForegroundColour(wx.Colour(95, 159, 159))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_3.SetForegroundColour(wx.Colour(185, 115, 45))
        self.label_3.SetFont(wx.Font(11, wx.DEFAULT, wx.ITALIC, wx.BOLD, 0, ""))
        self.text_ctrl_user.SetMinSize((250, 35))
        self.label_4.SetForegroundColour(wx.Colour(185, 115, 45))
        self.label_4.SetFont(wx.Font(11, wx.DEFAULT, wx.ITALIC, wx.BOLD, 0, ""))
        self.text_ctrl_passw.SetMinSize((250,35))
        self.panel_1.SetBackgroundColour(wx.Colour(193, 193, 255))
        self.button_next.SetMinSize((100, 35))
        self.login_pane.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.login_pane.SetFocus()
        self.checkbox_8.SetMinSize((100, 30))
        self.checkbox_9.SetMinSize((100, 30))
        self.checkbox_10.SetMinSize((120, 30))
        self.panel_3.SetBackgroundColour(wx.Colour(193, 193, 255))
        self.button_previous.SetMinSize((100, 35))
        self.button_proceed.SetMinSize((100, 35))
        self.standard_pane.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.standard_pane.Hide()
        self.progresss_total.SetMinSize((400, 30))
        self.progress_each.SetMinSize((400, 30))
        self.button_finished.SetMinSize((100, 35))
        self.panel_2.SetBackgroundColour(wx.Colour(193, 193, 255))
        self.report_pane.SetBackgroundColour(wx.Colour(249, 249, 248))
        '''self.report_pane.Hide()
        self.button_finished.Hide()
        self.button_next.Disable()
        self.button_proceed.Disable()
        '''
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: sampoorna_win.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(1, 3, 0, 0)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        sizer_2.Add(self.label_1, 1, wx.ALIGN_BOTTOM, 0)
        sizer_2.Add(self.label_2, 1, wx.ALIGN_BOTTOM, 1)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.text_ctrl_user, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.text_ctrl_passw, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_1.SetSizer(grid_sizer_1)
        sizer_4_copy.Add(self.panel_1, 2, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_4_copy, 3, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.button_next, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_login.SetSizer(sizer_2)
        sizer_1.Add(self.panel_login, 1, wx.ALL | wx.EXPAND, 20)
        self.login_pane.SetSizer(sizer_1)
        grid_sizer_2.Add(self.checkbox_8, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_9, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_10, 0, 0, 0)
        self.panel_3.SetSizer(grid_sizer_2)
        sizer_5.Add(self.panel_3, 1, wx.ALL | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_9.Add(self.button_previous, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 40)
        sizer_9.Add(self.button_proceed, 0, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 40)
        sizer_8.Add(sizer_9, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_8, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.standard_pane.SetSizer(sizer_5)
        sizer_11.Add(self.label_7, 0, 0, 0)
        sizer_7.Add(self.progresss_total, 0, wx.LEFT | wx.BOTTOM, 20)
        sizer_7.Add(self.progress_each, 0, wx.LEFT, 20)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_11.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_10.Add(sizer_11, 1, wx.EXPAND, 2)
        sizer_10.Add(self.label_satus, 0, wx.BOTTOM, 10)
        sizer_10.Add(self.list_ctrl_1, 3, wx.EXPAND, 0)
        sizer_13_copy.Add(self.button_finished, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(sizer_13_copy, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(sizer_12, 1, wx.EXPAND, 0)
        self.panel_2.SetSizer(sizer_10)
        sizer_13.Add(self.panel_2, 1, wx.ALL | wx.EXPAND, 20)
        self.report_pane.SetSizer(sizer_13)
        self.notebook_1.AddPage(self.login_pane, _("Login"))
        self.notebook_1.AddPage(self.standard_pane, _("Select Standards"))
        self.notebook_1.AddPage(self.report_pane, _("Reports"))
        sizer_4.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def on_password_enter(self, event):  # wxGlade: sampoorna_win.<event_handler>
        print "Event handler 'on_password_enter' not implemented!"
        event.Skip()

    
    def on_next(self, event):  # wxGlade: sampoorna_win.<event_handler>
        self.report_pane.Hide()
        self.login_pane.Hide()
        self.standard_pane.Show()
        event.Skip()

    def on_check(self, event):  # wxGlade: sampoorna_win.<event_handler>
        
        if self.checkbox_8.IsChecked() or self.checkbox_9.IsChecked() or self.checkbox_10.IsChecked():
            self.button_proceed.Enable()
        else:
            self.button_proceed.Disable()
        event.Skip()

    def on_previous(self, event):  # wxGlade: sampoorna_win.<event_handler>
        self.report_pane.Hide()
        self.login_pane.Show()
        self.standard_pane.Hide()
        event.Skip()

    def on_proceed(self, event):  # wxGlade: sampoorna_win.<event_handler>
        self.report_pane.Show()
        self.login_pane.Hide()
        self.standard_pane.Hide()       
        event.Skip()

    def on_finished(self, event):  # wxGlade: sampoorna_win.<event_handler>
        self.Close()
        event.Skip()# end of class sampoorna_win
        
    def on_user_pass_text(self,event):
        print "text"
        if self.text_ctrl_passw.Value and self.text_ctrl_user.Value:
            self.button_next.Enable()
        else:
            self.button_next.Disable()
    def updateDisplay(self, msg):
        """
        Receives data from thread and updates the display
        """
        t = msg.data
        '''if isinstance(t, int):
            self.displayLbl.SetLabel("Time since thread started: %s seconds" % t)
        else:
            self.displayLbl.SetLabel("%s" % t)
            self.btn.Enable()
        '''
        self.label_satus.SetLabel(str(t))

# end of class sampoorna_win
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    main_frame = sampoorna_win(None, wx.ID_ANY, "")
    app.SetTopWindow(main_frame)
    main_frame.Show()
    app.MainLoop()