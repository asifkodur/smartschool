#from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer,Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch,cm
from reportlab.platypus import PageBreak
from reportlab.lib.styles import getSampleStyleSheet





 



#I = Image('Resources/BS.jpeg')
#I.drawHeight =1*inch


school="CEHNNAMANGALLUR HSS"


name=year=class_=roll_no=admission_no=""



#SCHOOL=NAME=ADMISSION_NO=YEAR=ROLL_NO=

styleSheet = getSampleStyleSheet()



class Report_T2_Score_Only():
 

   
    
    def __init__(self,mypagesize=(18*cm,22*cm)):
        
        self.path="/tmp/report_t2_only.pdf"
        
        self.name="TEST"
        self.year="TEST"
        self.class_="TEST"
        self.roll_no="TEST"
        self.admission_no="TEST"
        self.school="test"
        styleSheet = getSampleStyleSheet()
        self.mypagesize=mypagesize
        self.elements = []
        self.doc = SimpleDocTemplate(self.path, pagesize=mypagesize,title="Performance Report",topMargin=.4*inch,bottomMargin=.3*inch,author="Asif Kodur")
        self.Set_Content()
        
                                            
       
                                                

        
        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/5.25
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/26.8
        
        

        #end of measurement
        
    def Set_Content(self):
        
        global year,class_,name,roll_no,admission_no
        #SCORE TABLE CONTENT STARTS
        self.SCHOOL = Paragraph('''
        <para align=center spaceb=3><b>
        <font size=16>%s

        </font> <br/>Chennamangallur</b>
        </para>'''% (self.school),
        styleSheet["BodyText"])
            
        self.NAME=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=15><i>Performance Card of : %s</i>
            
           </font> </b>
            </para>'''%(self.name),
            styleSheet["BodyText"])
            
            
        self.ADMISSION_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Admission No : %s</i>
            
           </font> </b>
            </para>'''%(self.admission_no),
            styleSheet["BodyText"])
            
        self.YEAR=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Year : %s</i>
            
           </font> </b>
            </para>'''%(self.year),
            styleSheet["BodyText"]) 

            
        self.ROLL_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Roll No : %s</i>
            
           </font> </b>
            </para>'''%(self.roll_no),
            styleSheet["BodyText"])
           
        self.CLASS_=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Class : %s</i>
            
           </font> </b>
            </para>'''%(self.class_),
            styleSheet["BodyText"])


        self.SUBJECT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=13><i>SUBJECT</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])

        self.TERM1=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Term I </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.TERM2=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Term II </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
            
        self.CE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>CE </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
        self.TE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>TE </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
        self.TOTAL=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Total </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
        self.GRADE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Grade </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
            
        self.LANG=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Language I</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.MAL=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Malayalam II</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.ENG=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>English</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.HIND=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Hindi</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.SS=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Social Science</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.PHY=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Physics</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.CHEM=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Chemistry</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.BIO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Biology</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.MATHS=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Mathematics</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.IT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>I.T</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
            
        #SCORE TABLE CONTENT ENDS


        #ATTENDANCE TABLE CONETNT STARTS
        self.ATTENDANCE_=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=12>Attendance
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])

        self.ATTENDANCE_TOT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=8>Total
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.ATTENDANCE_PRESENT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=8>Present
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.HM_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Headmaster
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.TEACHER_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Class Teacher
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.PARENT_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Parent
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
        #End ATTENDANCE CONTENT
        
        
        self.Score_Data=   [['',  '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['','', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['', '',  '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['', '', '', '','','','', '',''],
                                    ['',  '', '', '','','','', '','']]
                                    
                                    
                                    
        
        
        self.Attendance_Data=[['','','','',''],
                                            ['','','','',''],
                                            ['','','','',''],
                                            ['','','','',''],
                                            ['','','','','']]
                                            
        
    def SetTable_Style(self):
        
        #Starts Score Table
        self.Score_T_Style=[#('BOX',(0,0),(-1,-1),1.7,colors.black),
        
                                #('GRID',(0,0),(-1,-1),1,colors.black),#
                                
                                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                                ('FONTname',(0,0),(-1,-1),'Helvetica-Bold'),
                                ('SPAN',(0,0),(-1,0)), # SCHOOL
                                ('ALIGN',(0,0),(-1,0),'CENTER'),
                                ('SPAN',(0,1),(-1,1)), # PERFORMANCE CARD OF
                                ('SPAN',(0,2),(4,2)),   #ADM NOO
                                ('SPAN',(5,2),(-1,2)),  # YEAR
                                ('ALIGN',(2,0),(3,-1),'LEFT'),
                                ('SPAN',(0,3),(4,3)), # ROLL NO
                                ('SPAN',(5,3),(-1,3)),   #CLASS    
                                ('SPAN',(0,4),(0,5)),     #SUBJECT LABEL  
                                ('SPAN',(1,4),(4,4)),       #TERM1
                                ('ALIGN',(1,4),(4,4),'CENTER'),
                                ('SPAN',(5,4),(-1,4)),      #TERM2
                                ('ALIGN',(5,4),(-1,4),'CENTER'),
                                #('BOX',(1,4),(4,-1),1.5,colors.black),
                                #('BOX',(5,4),(-1,-1),1.5,colors.black),
                                ('ALIGN',(2,5),(-1,5),'CENTER'), 
                                ('ALIGN',(1,6),(-1,-1),'CENTER')
                                ]
        #End of Score Table                        
                        
        #Starts Attendance Tabke style
        self.Attendance_T_Style=[
                                            #('GRID',(0,0),(-1,-1),1,colors.black),
                                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

                                            ('SPAN',(0,0),(0,1)),
                                            
                                            ('SPAN',(1,2),(2,2)),
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(1,4),(2,4))
                                            
                                            #('BOX',(0,0),(-1,-1),2,colors.black)
                                            ]
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,sheet,Term_index=0):
        
        global year,class_,name,roll_no,admission_no
        
        Loop=1
        #Get Name,Adm No,Roll No, Class,etc
        
        self.year="2013"
        self.class_=sheet.name
        self.school="CHENNAMANGALLUR HSS"
        
        
        
        for row in range(1,sheet.nrows,1):
            
            self.name=sheet.cell(row,2).value
            self.roll_no=str(sheet.cell(row,1).value).split(".")[0] 
            self.admission_no=str(sheet.cell(row,0).value).split(".")[0] 
            if self.name=="" and self.roll_no=="" and self.admission_no=="":
                continue
            self.Set_Content()
             
            # Term II Begins
            
            
            #Term II
                
            L_Bound=3+41
            U_Bound=L_Bound+41
            self.Score_Data[6][5]=self.Score_Data[6][6]=self.Score_Data[6][7]=self.Score_Data[6][8]=''
            Data_Col=6 # CE,TE score starts in the 7th inner tuple of tthe score table data
            col=L_Bound
            #for col in range(L_Bound,U_Bound,1):
            
            while(col<=U_Bound):
                
                if sheet.cell(row,L_Bound).value!="":   #skips all entries if I lang is empty
                    
                    
                    
                    
                    self.Score_Data[Data_Col-1][5]=str(sheet.cell(row,col+0).value).split(".")[0]                 
                    self.Score_Data[Data_Col-1][6]=str(sheet.cell(row,col+1).value).split(".")[0]                    
                    self.Score_Data[Data_Col-1][7]=str(sheet.cell(row,col+2).value).split(".")[0]                 
                    #self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+3).value).split(".")[0]
                    
                    
                    self.Score_Data[Data_Col-1][8]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=9><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(sheet.cell(row,col+3).value).split(".")[0]),
                        styleSheet["BodyText"]) 
                    
                    
                    
                
                Data_Col+=1
                col+=4
                    
                if col+4>U_Bound:
                    
                    break
            
            
            self.Attendance_Data[0][4]=str(sheet.cell(row,U_Bound-1).value).split(".")[0]#Total
            
            self.Attendance_Data[1][4]=str(sheet.cell(row,U_Bound-1).value).split(".")[0]#Present
            
            
            self.AddPage()
                
           
        
    def AddPage(self):
        self.Score_Table=Table(self.Score_Data,[self.cW1*cm]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])          
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        self.elements.append(self.Score_Table)
        self.elements.append(Spacer(1, 15))
        self.elements.append(self.Attendance_Table)
        self.elements.append(PageBreak())
        
    def Save(self):
        
        

        import subprocess
                
                        
        
        self.doc.build(self.elements)
        
        try:
                subprocess.call(["xdg-open",self.path])
        except:
            
            print "pdf opening oeeror"
            
            
            
#Basic Science Img
import os,sys

dir = os.path.split(sys.argv[0])[0]
I = Image(dir+'/Resources/BS.gif')
"""I.drawHeight =1*inch
I.drawWidth=.3*inch
"""
#end BS img
    
class Report_8():
    
    
    def __init__(self,mypagesize=(18*cm,22*cm)):
        
        self.name="TEST"
        self.year="TEST"
        self.class_="TEST"
        self.roll_no="TEST"
        self.admission_no="TEST"
        self.school="test"
        styleSheet = getSampleStyleSheet()
        self.mypagesize=mypagesize
        self.elements = []
        self.doc = SimpleDocTemplate("/tmp/report.pdf", pagesize=mypagesize,title="Performance Report",topMargin=.4*inch,bottomMargin=.3*inch,author="Asif Kodur")
        self.Set_Content()
        
                                            
       
                                                

        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/5.25
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/27
        
        

        #end of measurement

    def Set_Content(self):
        
        global year,class_,name,roll_no,admission_no
        #SCORE TABLE CONTENT STARTS
        self.SCHOOL = Paragraph('''
        <para align=center spaceb=3><b>
        <font size=16>%s

        </font> <br/>Chennamangallur</b>
        </para>'''% (self.school),
        styleSheet["BodyText"])
            
        self.NAME=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=15><i>Performance Card of : %s</i>
            
           </font> </b>
            </para>'''%(self.name),
            styleSheet["BodyText"])
            
            
        self.ADMISSION_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Admission No : %s</i>
            
           </font> </b>
            </para>'''%(self.admission_no),
            styleSheet["BodyText"])
            
        self.YEAR=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Year : %s</i>
            
           </font> </b>
            </para>'''%(self.year),
            styleSheet["BodyText"]) 

            
        self.ROLL_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Roll No : %s</i>
            
           </font> </b>
            </para>'''%(self.roll_no),
            styleSheet["BodyText"])
           
        self.CLASS_=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Class : %s</i>
            
           </font> </b>
            </para>'''%(self.class_),
            styleSheet["BodyText"])


        self.SUBJECT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=13><i>SUBJECT</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])

        self.TERM1=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Term I </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.TERM2=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Term II </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
            
        self.CE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>CE </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
        self.TE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>TE </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
        self.TOTAL=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Total </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
        self.GRADE=Paragraph('''
            <para align=center spaceb=3><b>
            <font size=11><i>Grade </i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])   
            
            
        self.LANG=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Language I</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.MAL=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Malayalam II</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.ENG=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>English</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.HIND=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Hindi</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.SS=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Social Science</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.PHY=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Physics</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.CHEM=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Chemistry</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.BIO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Biology</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.MATHS=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Mathematics</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.IT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>I.T</i>
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
            
        #SCORE TABLE CONTENT ENDS


        #ATTENDANCE TABLE CONETNT STARTS
        self.ATTENDANCE_=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=12>Attendance
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])

        self.ATTENDANCE_TOT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=8>Total
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.ATTENDANCE_PRESENT=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=8>Present
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.HM_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Headmaster
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.TEACHER_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Class Teacher
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
            
        self.PARENT_SIGN=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=9>Signature of Parent
            
           </font> </b>
            </para>''',
            styleSheet["BodyText"])
        #End ATTENDANCE CONTENT
        
        
        
        self.Score_Data=   [[self.SCHOOL, '', '', '','','','','','',''],
                                    [self.NAME,  '', '','', '','','','', '',''],
                                    [self.ADMISSION_NO, '', '', '', '','',self.YEAR,'', '',''],
                                    [self.ROLL_NO, '', '', '', '','',self.CLASS_,'', '',''],
                                    [self.SUBJECT,'',self.TERM1, '', '','',self.TERM2,'', '',''],
                                    ['','',  self.CE, self.TE, self.TOTAL,self.GRADE,self.CE,self.TE, self.TOTAL,self.GRADE],
                                    [self.LANG, '', '', '', '','','','', '',''],
                                    [self.MAL,  '', '','', '','','','', '',''],
                                    [self.ENG, '', '','', '','','','', '',''],
                                    [self.HIND, '', '','', '','','','', '',''],
                                    [self.SS, '', '','', '','','','', '',''],
                                    [ I,self.PHY, '', '', '','','','', '',''],
                                    ['',self.CHEM, '',  '', '','','','', '',''],
                                    ['',self.BIO, '', '', '','','','', '',''],
                                    [self.MATHS,'', '', '', '','','','', '',''],
                                    [self.IT,  '', '', '','','','','', '','']]
                                    
                                    
                                    
        
        
        self.Attendance_Data=[[self.ATTENDANCE_,self.ATTENDANCE_TOT,'75',self.ATTENDANCE_TOT,''],
                                            ['',self.ATTENDANCE_PRESENT,'',self.ATTENDANCE_PRESENT,''],
                                            [self.TEACHER_SIGN,'','','',''],
                                            [self.HM_SIGN,'','','',''],
                                            [self.PARENT_SIGN,'','','','']]
                                            
                                            
    def SetTable_Style(self):
        
        #Starts Score Table
        self.Score_T_Style=[('BOX',(0,0),(-1,-1),2,colors.black),
                       ('GRID',(0,0),(-1,-1),1,colors.black),#
                    
                     ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                    ('FONTname',(0,0),(-1,-1),'Helvetica-Bold'),
                    ('SPAN',(0,0),(-1,0)), # SCHOOL
                    ('ALIGN',(0,0),(-1,0),'CENTER'),
                    ('SPAN',(0,1),(-1,1)), # PERFORMANCE CARD OF
                    ('SPAN',(0,2),(5,2)),   #ADM NOO
                    ('SPAN',(6,2),(-1,2)),  # YEAR
                    ('ALIGN',(2,0),(3,-1),'LEFT'),
                    ('SPAN',(0,3),(5,3)), # ROLL NO
                    ('SPAN',(6,3),(-1,3)),   #CLASS    
                    ('SPAN',(0,4),(1,5)),     #SUBJECT LABEL  
                    ('SPAN',(2,4),(5,4)),       #TERM1
                    ('ALIGN',(2,4),(5,4),'CENTER'),
                    ('SPAN',(6,4),(-1,4)),      #TERM2
                    ('ALIGN',(6,4),(-1,4),'CENTER'),
                    ('SPAN',(0,6),(1,6)),       #LANG I
                    ('SPAN',(0,7),(1,7)),       #MAL II
                    ('SPAN',(0,8),(1,8)),      #ENGL
                    ('SPAN',(0,9),(1,9)),      #HINDI
                    ('SPAN',(0,10),(1,10)),     #SS
                    ('SPAN',(0,14),(1,14)),    # MATHS
                    ('SPAN',(0,15),(1,15)),        #IT                    
                    ('SPAN',(0,11),(0,13)),     # BASIC sc
                    ('SPAN',(4,11),(4,13)),     #bs Total   T1
                    ('SPAN',(5,11),(5,13)),         #bs grADE T1
                    ('SPAN',(8,11),(8,13)),         #bs  tot term2
                    ('SPAN',(9,11),(9,13)),         #bs grade term2
                    ('BOX',(2,4),(5,-1),1.5,colors.black),
                    ('BOX',(6,4),(-1,-1),1.5,colors.black),
                    ('ALIGN',(2,6),(-1,-1),'CENTER') # Score center
                    
                    
                    ]
        #End of Score Table                        
                        
        #Starts Attendance Tabke style
        self.Attendance_T_Style=[('GRID',(0,0),(-1,-1),1,colors.black),
                                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

                                            ('SPAN',(0,0),(0,1)),
                                            
                                            ('SPAN',(1,2),(2,2)),
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(1,4),(2,4)),
                                            
                                            ('BOX',(0,0),(-1,-1),2,colors.black)]
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,sheet,Term_index=0):
        
        global year,class_,name,roll_no,admission_no
        
        Loop=1
        
        #Get Name,Adm No,Roll No, Class,etc
        
        self.year="2013"
        self.class_=sheet.name
        self.school="CHENNAMANGALLUR HSS"
        
        
        
        for row in range(1,sheet.nrows,1):
            
            self.name=sheet.cell(row,2).value
            self.roll_no=str(sheet.cell(row,1).value).split(".")[0] 
            self.admission_no=str(sheet.cell(row,0).value).split(".")[0] 
            if self.name=="" and self.roll_no=="" and self.admission_no=="":
                continue
            self.Set_Content()
            
            
            L_Bound=3+Term_index*39
            U_Bound=L_Bound+39#only one term
            self.Score_Data[6][2]=self.Score_Data[6][3]=self.Score_Data[6][4]=self.Score_Data[6][5]=''
            Data_Col=6 # CE,TE score starts in the 7th inner tuple of tthe score table data
            col=L_Bound
            #for col in range(L_Bound,U_Bound,1):
            while(col<=U_Bound):
                
                #if sheet.cell(row,L_Bound).value!="":
                    
                print col,   str(sheet.cell(row,col+0).value).split(".")[0]
                if Data_Col==11: #Basic Sceince
                    
                    print "col==8"
                    self.Score_Data[Data_Col][2]=str(sheet.cell(row,col+0).value).split(".")[0]     #CE      phy      
                    self.Score_Data[Data_Col][3]=str(sheet.cell(row,col+1).value).split(".")[0]    #TE      phy
                                    
                    self.Score_Data[Data_Col+1][2]=str(sheet.cell(row,col+2).value).split(".")[0]       #CE Chem          
                    self.Score_Data[Data_Col+1][3]=str(sheet.cell(row,col+3).value).split(".")[0]        #TE Chem
                    
                    self.Score_Data[Data_Col+2][2]=str(sheet.cell(row,col+4).value).split(".")[0]        #CE Bio      
                    self.Score_Data[Data_Col+2][3]=str(sheet.cell(row,col+5).value).split(".")[0]           #TE Bio
                    
                    self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+8).value).split(".")[0]      #Tot       
                    #self.Score_Data[Data_Col][5]=str(sheet.cell(row,col+9).value).split(".")[0]          #Grade
                    self.Score_Data[Data_Col][5]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=11><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(sheet.cell(row,col+9).value).split(".")[0]),
                        styleSheet["BodyText"])   #Grade
                    
                    col+=6  #additional for BS
                    Data_Col+=2 #additional move downwards
                    
                else:
                
                    self.Score_Data[Data_Col][2]=str(sheet.cell(row,col+0).value).split(".")[0]     #CE            
                    self.Score_Data[Data_Col][3]=str(sheet.cell(row,col+1).value).split(".")[0]    #TE          
                    self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+2).value).split(".")[0]    #Tot
                                 
                    self.Score_Data[Data_Col][5]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=11><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(sheet.cell(row,col+3).value).split(".")[0]),
                        styleSheet["BodyText"])   #Grade
                    
                
                
                
                
                
                Data_Col+=1
                col+=4
                    
                if col+4>U_Bound:
                    
                    break
            
            self.Attendance_Data[1][2]=str(sheet.cell(row,U_Bound-1).value).split(".")[0]
            self.AddPage()
                
           
        
    def AddPage(self):
        #self.Score_Table=Table(self.Score_Data,[.3*inch]+[1*inch]+8*[0.6*inch], [.8*inch]+[.6*inch]+14*[0.35*inch])   
        
        self.Score_Table=Table(self.Score_Data,[.3*inch]+[(self.cW1*cm)-.3*inch]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])   
               
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        self.elements.append(self.Score_Table)
        self.elements.append(Spacer(1, 15))
        self.elements.append(self.Attendance_Table)
        self.elements.append(PageBreak())
        
    def Save(self):
        
        

        import subprocess
                
                        
        
        self.doc.build(self.elements)
        
        try:
                subprocess.call(["xdg-open","/tmp/report.pdf"])
        except:
            
            print "pdf opening oeeror"
                                            
   
class Consolidated():
    
    def __init__(self,mypagesize=(18*cm,22*cm)):
        
        styleSheet = getSampleStyleSheet()
        
        self.doc = SimpleDocTemplate("/tmp/Consolidated_report.pdf", pagesize=mypagesize,title="Performance Report",topMargin=.4*inch,bottomMargin=.3*inch,author="Asif Kodur")


    
if __name__ == "__main__":
        
    pass
