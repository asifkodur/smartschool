
import wx
from dboperations import db_operations
#from import_excel import import_excel_operations
import xlrd
from xlrd import open_workbook

import wx

class import_excel_operations():
    
    def __init__(self,parent,year,class_,div):
        self.parent=parent
        self.year=year
        self.class_=class_
        self.div=div
        
        
    def do(self):
        #app = wx.PySimpleApp(0)
        
        
        wcd="Excel Files(*.xls)|*.xls|"
        dir = "/home"
        save_dlg = wx.FileDialog(self.parent, message='Choose File to be Imported', defaultDir=dir, defaultFile= '', wildcard=wcd, style=wx.OPEN)
        if save_dlg.ShowModal() == wx.ID_OK:
            path = save_dlg.GetPath()
 
        
            self.book = open_workbook(path)
            self.current_sheet=self.book.sheet_by_index(0)
            self.rown=self.current_sheet.nrows
            self.DB=db_operations()
            self.write_to_db()
        save_dlg.Destroy()
        print "extd"
    def write_to_db(self):
        
        error_list=[]
        for j in range(1,self.rown,1):        
            
            
            roll=str(self.current_sheet.cell(j,0).value)
            roll=roll.split(".")[0]
            ad_no=str(self.current_sheet.cell(j,1).value)
            ad_no=ad_no.split(".")[0]
            name=str(self.current_sheet.cell(j,2).value)
            
            if self.Validate_Roll_No(roll)==0 or self.Validate_Adm_No(ad_no)==0 or self.Validate_Name(name)==0:
                error_list.append([roll,ad_no,name])
                continue
            else:
                self.DB.Add_Student(roll,ad_no,name,self.year,self.class_,self.div)
            
            
            
            
           
                
                    
        
        no=0 
        txt=''
        for err in error_list:
            no+=1
            txt+=err[0]+"       "+err[1]+'      '+err[2]+'\n'     
            
        if txt!='':
            txt='The Following student/s not added\n\n' +txt
            dlg = wx.MessageDialog(None, txt, 'Error Adding',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            
        else:
            
            dlg = wx.MessageDialog(None, 'Successfully Imported', 'Imported',wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
                        
                        
                        
    def Validate_Roll_No(self,value):
        
        if not value.isdigit() and value !="":
            '''dlg = wx.MessageDialog(None, 'Roll No should be integer', '',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            '''
            return 0
        
        else:
            return 1
        
    def Validate_Adm_No(self,value):
        
        
        if not value.isdigit() and value!="":
            '''dlg = wx.MessageDialog(None, 'Admission No should be integer', '',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            '''
            return 0
        
        else: # if admission no already exists
            
          
           if self.DB.Admission_Exists(value)!=False:
                print 'Admission No: ',value,' is already allotted to', self.DB.Admission_Exists(value)[1]
                  
                return 0
                        
                        
        return 1
    
    
    def Validate_Name(self,value):
        if value=="" or value=="Name":
            '''dlg = wx.MessageDialog(None, 'Name should not be empty', '',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            '''
            return 0
        return 1
    
    
    def __del__(self):
        self.book=None
        self.DB=None
        print 'del'

class import_excel(wx.Dialog):
    def __init__(self, *args, **kwds):
        # Constructor
        
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        
        
        self.label_1 = wx.StaticText(self, -1, "Year", style=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE)
        self.combo_box_1 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)

        
        self.label_2 = wx.StaticText(self, -1, "Standard", style=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE)
        
        self.combo_box_2 = wx.ComboBox(self, -1, choices=[ 'Select',"8", "9", "10"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_3 = wx.StaticText(self, -1, "Division", style=wx.ALIGN_CENTRE)
        self.combo_box_3 = wx.ComboBox(self, -1, choices=['Select'], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        #self.label_4 = wx.StaticText(self, -1, "Term", style=wx.ALIGN_CENTRE)
        #self.button_3 = wx.Button(self, -1, "Import File")
        
        #self.combo_box_4 = wx.ComboBox(self, -1, choices=[ "Term 1", "Term 2", "Annual"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        
       
        self.button_2 = wx.Button(self, -1, "Import")
        self.button_1 = wx.Button(self, -1, "Close")
        
       
        #self.SetMenu()

        self.__set_properties()
        self.__do_layout()
        
        self.Bind(wx.EVT_COMBOBOX, self.on_year, self.combo_box_1)
        self.Bind(wx.EVT_COMBOBOX, self.on_class, self.combo_box_2)
        self.Bind(wx.EVT_COMBOBOX, self.on_division, self.combo_box_3)

        self.Bind(wx.EVT_BUTTON, self.ok_clicked, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.cancel_clicked, self.button_1)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
        #self.CalcSheet=SpreadSheet(self)
        self.YEAR=''
        self.DB=db_operations()
        self.load_year()
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Import from Spreadsheet")
        self.SetSize((450, 350))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_1.SetSelection(0)
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_2.SetSelection(0)
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_3.SetSelection(0)        
        self.button_1.SetMinSize((90, 35))
        self.button_2.SetMinSize((90, 35))
        self.button_2.Enable(False)
        #self.label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        #self.combo_box_4.SetSelection(0)
        
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        
        grid_sizer_1.Add(self.label_1, 0, wx.LEFT|wx.TOP, 20)
        grid_sizer_1.Add(self.combo_box_1, 0, wx.TOP, 20)
        
        grid_sizer_1.Add(self.label_2, 0, wx.LEFT|wx.TOP, 20)
        grid_sizer_1.Add(self.combo_box_2, 0, wx.TOP, 20)
        grid_sizer_1.Add(self.label_3, 0, wx.LEFT|wx.TOP, 20)
        grid_sizer_1.Add(self.combo_box_3, 0, wx.RIGHT|wx.TOP, 20)
        #grid_sizer_1.Add(self.button_3, 0, wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND, 20)
        #grid_sizer_1.Add(self.combo_box_4, 0, wx.RIGHT|wx.TOP|wx.BOTTOM, 20)
        grid_sizer_1.Add(self.button_1, 0, wx.TOP|wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.LEFT, 30)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
    def load_year(self):
                    
        self.combo_box_1.Clear() #year combo
        self.combo_box_3.Clear()# div combo
        self.combo_box_3.Append("Select Division")
        
        years=self.DB.get_academic_year_list()
        years.insert(0,"Select Year")

        
        
        for item in years:
            self.combo_box_1.Append(str(item))
            
            
        self.combo_box_1.SetSelection(0) 
        self.combo_box_2.SetSelection(0) 
        self.combo_box_3.SetSelection(0) 
    def on_close(self,event):
        
        event.Skip()
        
    def cancel_clicked(self,event):
        self.Close(True)
        #
        
    def ok_clicked(self,event):
        
        msg='The spreadsheet must have data in 3 columns in the order of Roll No, Admission No, Name.'
        msg+=' It assumes first row carries headings and student data begins only from the second row.Do you want to proceed ?'
        dlg = wx.MessageDialog(self, msg,"Excel Format", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()# == wx.ID_YES
        if result==wx.ID_YES:
            
        
            self.I=import_excel_operations(self,self.YEAR,self.CLASS,self.DIV)
            self.I.do()
            dlg.Destroy()
        else:
            self.Close()
    def on_year(self, event):  # wxGlade: add_div.<event_handler>
        self.combo_box_2.SetSelection(0)
       
        self.YEAR=self.combo_box_1.Value.split('-')[0]
        self.combo_box_2.SetSelection(0)
        self.combo_box_3.Clear()
        self.combo_box_3.Append('Select')  
        self.combo_box_3.SetSelection(0)
        self.button_2.Enable(False)
        event.Skip()

    def on_class(self, event):  # wxGlade: add_div.<event_handler>
        self.CLASS=self.combo_box_2.Value
        self.combo_box_3.Clear()
        
        self.load_div()
        self.combo_box_3.SetSelection(0)
        self.button_2.Enable(False)
    def on_division(self,event):
        if self.combo_box_3.Value!='Select':
            self.DIV=self.combo_box_3.Value
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
    def load_div(self):
        
        
        
        divs=self.DB.Get_Div(self.YEAR,self.CLASS)
        divs=['Select']+divs
        for item in divs:
            self.combo_box_3.Append(str(item))    
            
            


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 =import_excel(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.ShowModal()
    frame_1.Destroy()

    app.MainLoop()
