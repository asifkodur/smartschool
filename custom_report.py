import wx
from dboperations import db_operations
from xlwt import Workbook
import subprocess
            

class custom_report(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: consolidated_report.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.combo_box_1 = wx.ComboBox(self.panel_1, -1, choices=[], style=wx.CB_DROPDOWN | wx.CB_SIMPLE | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_2 = wx.ComboBox(self.panel_1, -1, choices=["Select Standard", "8", "9", "10"], style=wx.CB_DROPDOWN | wx.CB_SIMPLE | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_3 = wx.ComboBox(self.panel_1, -1, choices=["Select Division"], style=wx.CB_DROPDOWN | wx.CB_SIMPLE | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_4 = wx.ComboBox(self.panel_1, -1, choices=["Select Term","Term1","Term2","Annual"], style=wx.CB_DROPDOWN | wx.CB_SIMPLE | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1 = wx.StaticText(self.panel_1, -1, "Select What to Include")
        self.checkbox_1 = wx.CheckBox(self.panel_1, -1, "CE")
        self.checkbox_2 = wx.CheckBox(self.panel_1, -1, "TE")
        self.checkbox_3 = wx.CheckBox(self.panel_1, -1, "Total")
        self.checkbox_4 = wx.CheckBox(self.panel_1, -1, "Grade")
        self.checkbox_5 = wx.CheckBox(self.panel_1, -1, "CE Total")
        self.checkbox_6 = wx.CheckBox(self.panel_1, -1, "TE Total")
        self.checkbox_7 = wx.CheckBox(self.panel_1, -1, "Grand Total")
        
        allLoc = ['Select All']
        list2=['I Language','Malayalam','English','Hindi','S.S','Physics','Biology','Chemistry','Maths','IT']
        self.check_list_box_1 = wx.CheckListBox(self.panel_1, -1, (60, 50), (30,30), allLoc)
        self.check_list_box_2 = wx.CheckListBox(self.panel_1, -1, (60, 50), wx.DefaultSize, list2)
        self.button_1 = wx.Button(self.panel_1, -1, "Close")
        self.button_2 = wx.Button(self.panel_1, -1, "Proceed")

        self.__set_properties()
        self.__do_layout()
        
        self.Bind(wx.EVT_COMBOBOX, self.oncombo_year, self.combo_box_1)
        self.Bind(wx.EVT_COMBOBOX, self.oncombo_class, self.combo_box_2)
        self.Bind(wx.EVT_COMBOBOX, self.oncombo_div, self.combo_box_3)
        self.Bind(wx.EVT_COMBOBOX, self.oncombo_term, self.combo_box_4)
        
        self.Bind(wx.EVT_CHECKLISTBOX, self.on_check, self.check_list_box_1)
        self.Bind(wx.EVT_CHECKLISTBOX, self.on_check_2, self.check_list_box_2)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_proceed, self.button_2)
        
        self.Bind(wx.EVT_CHECKBOX, self.on_check_ce, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_te, self.checkbox_2)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_tota, self.checkbox_3)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_grade, self.checkbox_4)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_ce_total, self.checkbox_5)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_te_total, self.checkbox_6)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_grand, self.checkbox_7)
        self.checkedItems=()
        self.checkedItems_2=[0,1,2,3]
        self.DB=db_operations()
        
        self.Selected_Index=[]
        self.YEAR=''
        self.CLASS=''
        self.DIV=''
        self.TERM=''
        
        self.load_year()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: consolidated_report.__set_properties
        self.SetTitle("Consolidated Report")
        self.SetSize((420, 550))
        self.combo_box_1.SetSelection(0)
        self.combo_box_2.SetSelection(0)
        self.combo_box_3.SetSelection(0)
        self.combo_box_4.SetSelection(0)
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.check_list_box_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.button_1.SetMinSize((85, 32))
        self.button_2.SetMinSize((85, 32))
        
        self.checkbox_1.SetValue(1)
        self.checkbox_2.SetValue(1)
        self.checkbox_3.SetValue(1)
        self.checkbox_4.SetValue(1)
        self.button_2.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: consolidated_report.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(2, 4, 5, 5)
        grid_sizer_1 = wx.GridSizer(4, 1, 0, 10)
        grid_sizer_1.Add(self.combo_box_1, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 10)
        grid_sizer_1.Add(self.combo_box_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.combo_box_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.combo_box_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        sizer_6.Add(self.label_1, 0, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 10)
        grid_sizer_2.Add(self.checkbox_1, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_2, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_3, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_4, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_5, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_6, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_7, 0, 0, 0)
        sizer_6.Add(grid_sizer_2, 0, wx.EXPAND, 0)
        sizer_6.Add(self.check_list_box_1, 0, wx.EXPAND, 0)
        sizer_6.Add(self.check_list_box_2, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_1, 0, wx.RIGHT | wx.TOP | wx.BOTTOM | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_2, 0, wx.RIGHT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
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
    def oncombo_year(self, event):  # wxGlade: promote.<event_handler>
        self.YEAR=self.combo_box_1.Value.split('-')[0]
        self.combo_box_2.SetSelection(0)
        self.combo_box_3.Clear()
        self.combo_box_3.Append('Select Division')  
        self.combo_box_3.SetSelection(0)
        self.combo_box_4.SetSelection(0)
        
        self.button_2.Enable(False)
       
        self.uncheck_all()
        event.Skip()

    def oncombo_class(self, event):  # wxGlade: promote.<event_handler>
        self.CLASS=self.combo_box_2.Value
        self.combo_box_3.Clear()
        
        self.load_div()
        self.combo_box_3.SetSelection(0)
        self.combo_box_4.SetSelection(0)
        self.uncheck_all()
        self.button_2.Enable(False) 
        event.Skip()

    def oncombo_div(self, event):  # wxGlade: promote.<event_handler>
        if self.combo_box_3.Value!='Select Division':
            
            
            self.DIV=self.combo_box_3.Value
            
       
            
        self.uncheck_all()
        self.button_2.Enable(False) 
        self.combo_box_4.SetSelection(0)
        event.Skip()
        
    def oncombo_term(self,event):
        if self.combo_box_4.Value!='Select Term':
            self.TERM=self.combo_box_4.Value
            
       
            
        self.uncheck_all()
        self.button_2.Enable(False) 
       
    
    def on_check(self,event):
        
        
        
        if self.check_list_box_1.IsChecked(0):
            self.check_all()
            self.checkedItems = self.check_list_box_2.GetChecked()
        else:
            
            self.uncheck_all()
            self.checkedItems = self.check_list_box_2.GetChecked()
            
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
    def on_check_2(self,event):
        
        
        self.checkedItems = self.check_list_box_2.GetChecked()
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        
            
    def check_all(self):
        
        for i in range(self.check_list_box_2.GetCount()):
            self.check_list_box_2.Check(i)
    def uncheck_all(self):
        
        for i in range(self.check_list_box_2.GetCount()):
            self.check_list_box_2.Check(i,False)
    
    def on_check_ce(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(0)
        else:
            self.checkedItems_2.remove(0)
            
                        
        self.checkedItems_2.sort()
        
        
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_check_te(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(1)
        else:
            self.checkedItems_2.remove(1)
            
           
                        
        self.checkedItems_2.sort()
        
        
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
            
        
        event.Skip()

    def on_check_tota(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(2)
        else:
            self.checkedItems_2.remove(2)
            
           
                        
        self.checkedItems_2.sort()
        
            
            
        
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()
        
    def on_check_grade(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(3)
        else:
            self.checkedItems_2.remove(3)
            
            
            
           
                        
        self.checkedItems_2.sort()
        
        
            
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_check_ce_total(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(4)
        else:
            self.checkedItems_2.remove(4)
            
           
                        
        self.checkedItems_2.sort()
        
        
            
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_check_te_total(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(5)
        else:
            self.checkedItems_2.remove(5)
           
                        
        self.checkedItems_2.sort()
        
        
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    def on_check_grand(self, event):  # wxGlade: consolidated_report.<event_handler>
        if event.GetEventObject().IsChecked()==True:
            self.checkedItems_2.append(6)
        else:
            self.checkedItems_2.remove(6)
           
                        
        self.checkedItems_2.sort()
        
        
        if self.combo_box_4.Value!='Select Term' and self.checkedItems!=() and len(self.checkedItems_2)>0:
            
            self.button_2.Enable(True)
        else:
            self.button_2.Enable(False)
        event.Skip()

    
      
            
    def load_div(self):
        # token 1 for one set of combos...token 2 for the other set
        
         
         
        divs=self.DB.Get_Div(self.YEAR,self.CLASS)
        divs=['Select Division','All Divisions']+divs
        
        for item in divs:
            self.combo_box_3.Append(str(item))   
                
    def on_close(self,event):
        self.Close()
        event.Skip()
    def on_proceed(self,event):
        self.Selected_Index=self.checkedItems
        all_divs=[self.DIV]
        if self.DIV=='All Divisions':
            all_divs=self.DB.Get_Div(self.YEAR,self.CLASS)
           
        self.book = Workbook()
        
        for each_div in all_divs:
            
            sheet = self.book.add_sheet(self.CLASS+each_div)
            self.write_headings_to_excel(sheet)
            self.get_each_sub(sheet,each_div)
            
        self.save()
        self.Close()
        
    
    def get_each_sub(self,sheet,current_div):
        if self.TERM=='Term1':
            term='1'
        elif self.TERM=='Term2':
            term='2'
        elif self.TERM=='Term3':
            term='3'
        div_id=div_id=self.DB.Get_Div_Id(self.YEAR,self.CLASS,current_div)
        first_round_subj=True
        first_round=True
        ce_total=[]
        te_total=[]
        
        ncols=0
        
        for i in self.checkedItems:#carries sub index
            
            
            
            max_ce,max_te=self.DB.Get_CE_TE(self.YEAR,self.CLASS,i)
            score=self.DB.Score_and_Roll(term,div_id,i)
            score=score[1:]
            col_indx=ncols
            if ncols==0:
                ncols=2
                col_indx=2
            else:
                col_indx=col_indx
                pass
            row=1
            
            first_round=True
            for each_score in score:
                
                ce,te,total,grade='','','',''
                roll=each_score[5]
                ad_no=each_score[2]
                name=each_score[3]
                ce=each_score[6]
                te=each_score[8]
                if first_round_subj:
                    sheet.write(row,0,roll)
                    sheet.write(row,1,ad_no)
                    sheet.write(row,2,name)
                    #col_indx+=3
                    #ncols+=3
                #if  first_round_subj:
                #    ncols+=3
                if ce!=None and ce!='' and te!='' and te!=None:
                   
                    ce=int(ce)
                    te=int(te)
                    total=ce+te
                    grade=self.find_grade(total,int(max_ce)+int(max_te))
                
                
                if first_round_subj:
                    if ce!=None and ce!='':
                        ce_total.append(ce)
                    if te!='' and te!=None:
                        te_total.append(te)
                else:
                    if ce!=None and ce!='':
                        ce_total[row-1]=ce_total[row-1]+ce
                    if te!='' and te!=None:
                        te_total[row-1]=te_total[row-1]+te
                    
                ce_i,te_i,total_i,grade_i=0,0,0,0
                
                if self.checkbox_1.IsChecked():
                    sheet.write(row,col_indx+1,ce)
                    ce_i=1
                    if  first_round:
                        #ncols+=1
                        pass
                if self.checkbox_2.IsChecked():
                    sheet.write(row,col_indx+ce_i+1,te)
                    te_i=1
                    if  first_round:
                        #ncols+=1
                        pass
                if self.checkbox_3.IsChecked():
                   sheet.write(row,col_indx+ce_i+te_i+1,total)
                   total_i=1
                   if  first_round:
                        #ncols+=1
                        pass
                if self.checkbox_4.IsChecked():
                   sheet.write(row,col_indx+ce_i+te_i+total_i+1,grade)
                   if  first_round:
                        #ncols+=1
                        pass
                
                row+=1
                first_round=False
                
                
                
                
                
            if self.checkbox_1.IsChecked():
                   
                ncols+=1
            if self.checkbox_2.IsChecked():
            
                ncols+=1
            if self.checkbox_3.IsChecked():
                ncols+=1
            if self.checkbox_4.IsChecked():
                ncols+=1
            
            first_round_subj=False
        
        self.add_totals(sheet,ce_total,te_total,ncols)
    def write_headings_to_excel(self,sheet):
        
        
        SUBJ=["LANG","MAL","ENGLISH","HINDI","SS","PHYSICS","CHEMISTRY","BIOLOGY","MATHEMATICS","IT"]
        
        sheet.write(0,0,'Roll No')
        sheet.write(0,1,'Admission No')
        sheet.write(0,2,'Name')
        col_i=0
        for i in  self.checkedItems:
            sub=SUBJ[i]
            
            if self.checkbox_1.IsChecked():
                sheet.write(0,3+col_i,sub+' CE')
                col_i+=1
            if self.checkbox_2.IsChecked():
                sheet.write(0,3+col_i,sub+' TE')
                col_i+=1
            if self.checkbox_3.IsChecked():
                sheet.write(0,3+col_i,sub+' Total')
                col_i+=1
            if self.checkbox_4.IsChecked():
                sheet.write(0,3+col_i,sub+' Grade')
                col_i+=1
                
        if self.checkbox_5.IsChecked():
            sheet.write(0,3+col_i,'CE Total')
            col_i+=1
        if self.checkbox_6.IsChecked():
            sheet.write(0,3+col_i,'TE Total')
            col_i+=1
        if self.checkbox_7.IsChecked():
            sheet.write(0,3+col_i,'Grand Total')
            col_i+=1
    
    
    def save(self):
        filename="custom_report.xls"
        path=''
        wcd="Excel Files(*.xls)|*.xls|"
        dir = "/home"
        save_dlg = wx.FileDialog(None, message='Save file as...', defaultDir=dir, defaultFile= filename, wildcard=wcd, style=wx.SAVE | wx.OVERWRITE_PROMPT)
        if save_dlg.ShowModal() == wx.ID_OK:
            path = save_dlg.GetPath()
           
                
            self.book.save( path)
       
           
            subprocess.call(["xdg-open",path])
    def add_totals(self,sheet,ce_list,te_list,index):
        index+=1
        for row in range(len(ce_list)):
            ce_i,te_i,total_i=0,0,0
            total=''
            ce=ce_list[row]
            te=te_list[row]
            if ce=='' or ce==None:
                ce=0
            if te=='' or te==None:
                te=0
            total=ce+te
            
            if ce==0:
                ce=''
            if te==0:
                te=''
            if total==0:
                total=''
                
            if self.checkbox_5.IsChecked():
                sheet.write(row+1,index,ce)
                ce_i=1
            if self.checkbox_6.IsChecked():
                sheet.write(row+1,index+ce_i,te)
                te_i=1
            if self.checkbox_7.IsChecked():
                sheet.write(row+1,index+ce_i+te_i,total)
            
        
        
    def find_grade(self,mark,max_mark):
        
        if int(mark)>=(max_mark)*90/100:
            Grd="A+"
        elif int(mark)>=(max_mark)*80/100:
           Grd="A"
        elif int(mark)>=(max_mark)*70/100:
            Grd="B+"
            
        elif int(mark)>=(max_mark)*60/100:
            Grd="B"
        elif int(mark)>=(max_mark)*50/100:
            Grd="C+"
        elif int(mark)>=(max_mark)*40/100:
            Grd="C"
        elif int(mark)>=(max_mark)*30/100:
            Grd="D+"
        elif int(mark)>=(max_mark)*20/100:
            Grd="D"
        else:
            Grd="E"
        
        return Grd
# end of class consolidated_report

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = custom_report(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.ShowModal()
    frame_1.Destroy()

    app.MainLoop()