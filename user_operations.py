import wx
from lib import gate

from dboperations import db_operations

import hashlib



class user_operations():
    
    
    def __init__(self,parent):
        
        self.parent=parent
        self.Secret_Key="You cannot bypass this, lol"
        self.DB=db_operations()
        #self.DB.con.create_function('encrypt', 1, self.Encrypt_Password)# Custom pyfunction to sql
        #self.DB.con.create_function('encrypt', 1, self.Encrypt_Password)# Custom pyfunction to sql
    
   
    def Login_Check(self,user,password):
        
        print "login check"
        passw=self.Encrypt_Password(self.Secret_Key+password)
        query="SELECT PASSWORD FROM USER WHERE USER='%s' AND PASSWORD='%s'" %(user,passw)  
        #self.DB.cur.execute(query,(user,self.Secret_Key+password,))
        self.DB.cur.execute(query)
        #self.DB.con.commit()
        
        row=self.DB.cur.fetchone()
        
        
        if row:
            
            print "Success"
            return True
        else:
            dlg = wx.MessageDialog(self.parent, 'Incorrect Password', '',wx.OK | wx.ICON_INFORMATION)                  
            dlg.ShowModal()
            dlg.Destroy()
            
            return False
    def ChangePassword(self,username,password):
        
        query="UPDATE USER SET PASSWORD=encrypt(?) WHERE USER=?"
        
        self.DB.cur.execute(query,(self.Secret_Key+password,username))
        self.DB.con.commit()
    def Encrypt_Password(self,password):
        
        # Do not use this algorithm in a real environment
        encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
        return encrypted_pass
 
class win_chng_pass(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: chng_pass.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, -1, "Username")
        self.combo_box_1 = wx.ComboBox(self, -1, choices=['Select','admin','teacher'], style=wx.CB_DROPDOWN | wx.CB_SIMPLE | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_4 = wx.StaticText(self, -1, "Current Password")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.label_5 = wx.StaticText(self, -1, "New Password")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.label_6 = wx.StaticText(self, -1, "Confirm New Password")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.button_1 = wx.Button(self, -1, "Cancel")
        self.button_2 = wx.Button(self, -1, "Save")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_combo, self.combo_box_1)
        self.Bind(wx.EVT_TEXT, self.on_password_1, self.text_ctrl_1)
        self.Bind(wx.EVT_TEXT, self.on_password_2, self.text_ctrl_2)
        self.Bind(wx.EVT_TEXT, self.on_password_3, self.text_ctrl_3)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_save, self.button_2)
        self.UO=user_operations(self)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: chng_pass.__set_properties
        self.SetTitle("Change Password")
        self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_1.SetMinSize((180, 32))
        self.combo_box_1.SetSelection(0)
        self.label_4.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_1.SetMinSize((180, 33))
        self.label_5.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_2.SetMinSize((180, 33))
        self.label_6.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_3.SetMinSize((180, 33))
        self.button_1.SetMinSize((85, 33))
        self.button_2.SetMinSize((85, 33))
        self.button_2.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: chng_pass.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.TOP, 10)
        grid_sizer_1.Add(self.combo_box_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.TOP, 10)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, wx.TOP, 10)
        grid_sizer_1.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, wx.TOP, 10)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_1, 0, wx.LEFT, 80)
        sizer_3.Add(self.button_2, 0, wx.LEFT, 30)
        sizer_2.Add(sizer_3, 0, wx.TOP | wx.EXPAND, 20)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 20)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def on_combo(self, event):  # wxGlade: chng_pass.<event_handler>
        self.text_ctrl_1.Value=''
        self.text_ctrl_2.Value=''
        self.text_ctrl_3.Value=''
        event.Skip()

    def on_password_1(self, event):  # wxGlade: chng_pass.<event_handler>
        if self.combo_box_1.Value!='Select' and self.text_ctrl_1.Value!='' and  self.text_ctrl_2.Value!='' and  self.text_ctrl_3.Value!='':
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_password_2(self, event):  # wxGlade: chng_pass.<event_handler>
        if self.combo_box_1.Value!='Select' and self.text_ctrl_1.Value!='' and  self.text_ctrl_2.Value!='' and  self.text_ctrl_3.Value!='':
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_password_3(self, event):  # wxGlade: chng_pass.<event_handler>
        if self.combo_box_1.Value!='Select' and self.text_ctrl_1.Value!='' and  self.text_ctrl_2.Value!='' and  self.text_ctrl_3.Value!='':
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_cancel(self, event):  # wxGlade: chng_pass.<event_handler>
        self.Close()
        event.Skip()

    def on_save(self, event):  # wxGlade: chng_pass.<event_handler>
        if self.validate_pass():
            self.UO.ChangePassword(self.combo_box_1.Value,self.text_ctrl_2.Value)
            dlg = wx.MessageDialog(self, 'Password Changed!', '',wx.OK | wx.ICON_INFORMATION)                  
            dlg.ShowModal()
            dlg.Destroy()
            self.Close()
        else:
            self.text_ctrl_1.Value=''
            self.text_ctrl_2.Value=''
            self.text_ctrl_3.Value=''
        event.Skip()
        
        
    def validate_pass(self):
        
        if not self.UO.Login_Check(self.combo_box_1.Value,self.text_ctrl_1.Value):
            return False
        
        if len(self.text_ctrl_2.Value)<5:
            dlg = wx.MessageDialog(self, 'Password must be of at least five characters', '',wx.OK | wx.ICON_ERROR)                  
            dlg.ShowModal()
            dlg.Destroy()
            return False
        if self.text_ctrl_2.Value!=self.text_ctrl_3.Value:
            dlg = wx.MessageDialog(self, 'Passwords do not match', '',wx.OK | wx.ICON_ERROR)                  
            dlg.ShowModal()
            dlg.Destroy()
            return False
        
        return True

