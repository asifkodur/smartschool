#from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer,Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4,A3
from reportlab.lib.units import inch,cm
from reportlab.platypus import PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from dboperations import db_operations




class Rotated_BS(Paragraph):
    
        
    def draw(self):
        self.canv.saveState()
        self.canv.translate(20,-5)# 23,-10
        self.canv.rotate(90)
        Paragraph.draw(self)

        self.canv.restoreState()




#I = Image('Resources/BS.jpeg')
#I.drawHeight =1*inch


school="CHENNAMANGALLUR HIGHER SECONDARY SCHOOL"


name=year=class_=roll_no=admission_no=""



#SCHOOL=NAME=ADMISSION_NO=YEAR=ROLL_NO=

styleSheet = getSampleStyleSheet()



class Report():
 

   
    
    def __init__(self,mypagesize=(21*cm,25*cm)):
        
        
        self.path="/tmp/report.pdf"
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
        
        self.DB=db_operations()
        
        self.Set_Content()
        
                                            
       
                                                

        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/4.8
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/25
        
        

        #end of measurement
    def footer(self,canvas, doc):
        Title = ""
        pageinfo = "generated using '=smart school software.For more details visit www.mysite.com"
        
        
        PAGE_WIDTH,PAGE_HEIGHT=self.mypagesize

        canvas.saveState()
        canvas.setFont('Times-Bold',16)
        canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
        canvas.setFont('Times-Roman',7)
        canvas.drawString(inch, 0.25 * inch, pageinfo)
        canvas.restoreState()

        
    def Set_Content(self):
        
        #global year,class_,name,roll_no,admission_no
        #SCORE TABLE CONTENT STARTS
        self.SCHOOL = Paragraph('''
        <para align=center spaceb=3><b>
        <font size=16>%s

        </font> <br/><br/><font size=13>Chennamangallur</font></b>
        </para>'''% (self.school),
        styleSheet["BodyText"])
            
        self.NAME=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=14><i>Performance Card of : %s</i>
            
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
        
        
        self.Score_Data=   [[self.SCHOOL,  '', '', '','','','', '',''],
                                    [self.NAME,  '', '', '','','','', '',''],
                                    [self.ADMISSION_NO,  '', '', '','',self.YEAR,'', '',''],
                                    [self.ROLL_NO,  '', '', '','',self.CLASS_,'', '',''],
                                    [self.SUBJECT,self.TERM1, '', '','',self.TERM2,'', '',''],
                                    ['',  self.CE, self.TE, self.TOTAL,self.GRADE,self.CE,self.TE, self.TOTAL,self.GRADE],
                                    [self.LANG,  '', '', '','','','', '',''],
                                    [self.MAL,  '', '', '','','','', '',''],
                                    [self.ENG, '', '', '','','','', '',''],
                                    [self.HIND, '', '', '','','','', '',''],
                                    [self.SS, '', '', '','','','', '',''],
                                    [ self.PHY, '', '', '','','','', '',''],
                                    [self.CHEM, '',  '', '','','','', '',''],
                                    [self.BIO, '', '', '','','','', '',''],
                                    [self.MATHS, '', '', '','','','', '',''],
                                    [self.IT,  '', '', '','','','', '','']]
                                    
                                    
                                    
        
        
        self.Attendance_Data=[[self.ATTENDANCE_,self.ATTENDANCE_TOT,'75',self.ATTENDANCE_TOT,''],
                                            ['',self.ATTENDANCE_PRESENT,'',self.ATTENDANCE_PRESENT,''],
                                            [self.TEACHER_SIGN,'','','',''],
                                            [self.HM_SIGN,'','','',''],
                                            [self.PARENT_SIGN,'','','','']]
                                            
        
    def SetTable_Style(self):
        
        #Starts Score Table
        self.Score_T_Style=[('BOX',(0,0),(-1,-1),1.7,colors.black),
        
                                ('GRID',(0,0),(-1,-1),1,colors.black),#
                                
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
                                ('BOX',(1,4),(4,-1),1.5,colors.black),
                                ('BOX',(5,4),(-1,-1),1.5,colors.black),
                                ('ALIGN',(2,5),(-1,5),'CENTER'), 
                                ('ALIGN',(1,6),(-1,-1),'CENTER')
                                ]
        #End of Score Table                        
                        
        #Starts Attendance Tabke style
        self.Attendance_T_Style=[('GRID',(0,0),(-1,-1),1,colors.black),
                                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

                                            ('SPAN',(0,0),(0,1)),
                                            
                                            ('SPAN',(1,2),(2,2)),
                                            ('SPAN',(3,2),(4,2)),
                                            
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(3,3),(4,3)),
                                            
                                            ('SPAN',(1,4),(2,4)),
                                            ('SPAN',(3,4),(4,4)),
                                            
                                            ('BOX',(0,0),(-1,-1),2,colors.black)]
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,YEAR,CLASS,DIV,TERM_INDEX):
        
       
        div_id=self.DB.Get_Div_Id(YEAR,CLASS,DIV)
        term=TERM_INDEX
        term1="1"
        term2="2"
        
        
        
        self.year=YEAR
        self.class_=CLASS+' '+DIV
        self.div=DIV
        #self.school="CHENNAMANGALLUR HIGHER SECONDARY SCHOOL"
        self.school=self.DB.Get_School_Name()
        
        working_days1=self.DB.Get_Working_Days(self.year,"1")
        working_days2=self.DB.Get_Working_Days(self.year,"2")
        
        #for term I
            
            
        LAN1=self.DB.Score_and_Roll(term1,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL1=self.DB.Score_and_Roll(term1,div_id,str(1))[1:] 
        ENG1=self.DB.Score_and_Roll(term1,div_id,str(2))[1:] 
        HND1=self.DB.Score_and_Roll(term1,div_id,str(3))[1:] 
        SS1=self.DB.Score_and_Roll(term1,div_id,str(4))[1:] 
        PHY1=self.DB.Score_and_Roll(term1,div_id,str(5))[1:] 
        CHM1=self.DB.Score_and_Roll(term1,div_id,str(6))[1:] 
        BIO1=self.DB.Score_and_Roll(term1,div_id,str(7))[1:] 
        MTH1=self.DB.Score_and_Roll(term1,div_id,str(8))[1:] 
        IT1=self.DB.Score_and_Roll(term1,div_id,str(9))[1:] 
        ATND1=self.DB.Score_and_Roll(term1,div_id,str(10))[1:] 
        
        
        SCORE1=[LAN1,MAL1,ENG1,HND1,SS1,PHY1,CHM1,BIO1,MTH1,IT1]  
        #Term II
        LAN2=self.DB.Score_and_Roll(term2,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL2=self.DB.Score_and_Roll(term2,div_id,str(1))[1:] 
        ENG2=self.DB.Score_and_Roll(term2,div_id,str(2))[1:] 
        HND2=self.DB.Score_and_Roll(term2,div_id,str(3))[1:] 
        SS2=self.DB.Score_and_Roll(term2,div_id,str(4))[1:] 
        PHY2=self.DB.Score_and_Roll(term2,div_id,str(5))[1:] 
        CHM2=self.DB.Score_and_Roll(term2,div_id,str(6))[1:] 
        BIO2=self.DB.Score_and_Roll(term2,div_id,str(7))[1:] 
        MTH2=self.DB.Score_and_Roll(term2,div_id,str(8))[1:] 
        IT2=self.DB.Score_and_Roll(term2,div_id,str(9))[1:] 
        ATND2=self.DB.Score_and_Roll(term2,div_id,str(10))[1:] 
        
        SCORE2=[LAN2,MAL2,ENG2,HND2,SS2,PHY2,CHM2,BIO2,MTH2,IT2]  
        #End of Term II

                  
            
        for n in range(len(LAN1)):
            
            self.name=LAN1[n][3]
            self.roll_no=LAN1[n][5]
            self.admission_no=LAN1[n][2]
            if self.name=="" and self.roll_no=="" and self.admission_no=="":
                continue
            self.Set_Content()
            
            
            Data_Col=6 
            self.Score_Data[Data_Col][1]=self.Score_Data[Data_Col][2]=self.Score_Data[Data_Col][3]=self.Score_Data[Data_Col][4]=''
            # CE,TE score starts in the 7th inner tuple of tthe score table data
            
            #for EACH_SUB in SCORE:
            for sub_index in range(len(SCORE1)):# this cud b erronious if roll no changes across terms
                
                max_ce,max_te=self.DB.Get_CE_TE(self.year,CLASS,sub_index)                
               
                
                #Term I    
                ad_no1=SCORE1[sub_index][n][2]
                ce1=SCORE1[sub_index][n][6]                
                te1=SCORE1[sub_index][n][8]   
                           
                tot1=grade1=''
                if ce1!=('' or None) and te1!=('' or None): 
                        
                    if ce1=='' or ce1==None:
                        ce1=0
                    if te1=='' or te1==None:
                        te1=0
                        
                          
                    tot1,grade1=self.Calculate_Grade(ce1,te1,max_ce,max_te)
                
                
                    
                
                #Term II
               
                
                ad_no2=SCORE2[sub_index][n][2]
                if ad_no1==ad_no2: # Making sure same student
                    
                    ce2=SCORE2[sub_index][n][6]
                    
                    te2=SCORE2[sub_index][n][8]                        
                    
                else:
                    
                    ce2=te2=0
                    for each_student in SCORE2[sub_index]:
                        if each_student[2]==ad_no1:
                            ce2=each_student[6]
                            
                            te2=each_student[8]                        
                            
                tot2=grade2=''            
                if ce2!=('' or None) and te2!=(''or None): 
                       
                    if ce2==''or ce2==None:
                        ce2=0
                    if te2=='' or te2==None:
                        te2=0
                        
                             
                            
                    tot2,grade2=self.Calculate_Grade(ce2,te2,max_ce,max_te)
                    
                    
                    
                    
                                 
                
                
                #term 1
                
                if ce1==0 and te1==0:
                    
                    ce1=te1=tot1=grade1=''
                
                self.Score_Data[Data_Col][1]=str(ce1)               
                self.Score_Data[Data_Col][2]=str(te1)              
                self.Score_Data[Data_Col][3]=str(tot1)             
                #self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+3).value).split(".")[0]
                
                
                self.Score_Data[Data_Col][4]= Paragraph('''
                    <para align=center spaceb=3><b>
                    <font size=12><i>%s</i>
                    
                   </font> </b>
                    </para>'''%(str(grade1)),
                    styleSheet["BodyText"]) 
                
                
                
                
                
                
                #Term 1 Ends
                #Term II
                if ce2==0 and te2==0:
                    
                    ce2=te2=tot2=grade2=''
                        
                self.Score_Data[Data_Col][5]=str(ce2)               
                self.Score_Data[Data_Col][6]=str(te2)              
                self.Score_Data[Data_Col][7]=str(tot2)             
                #self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+3).value).split(".")[0]
                
                
                self.Score_Data[Data_Col][8]= Paragraph('''
                    <para align=center spaceb=3><b>
                    <font size=12><i>%s</i>
                    
                   </font> </b>
                    </para>'''%(str(grade2)),
                    styleSheet["BodyText"]) 
                    
                    
                Data_Col+=1
                sub_index+=1
                    
                
                    
            
            
            
            present1=ATND1[n][6]    
            present2=ATND2[n][6]
            self.Attendance_Data[0][2]=working_days1# Total            
            self.Attendance_Data[1][2]=str(present1)# Present
            
            self.Attendance_Data[0][4]=working_days2#Total            
            self.Attendance_Data[1][4]=str(present2)#Present
            
            self.AddPage()
            n+=1
    def Calculate_Grade(self,ce,te,max_ce,max_te):
        
        try:
            max_tot=int(max_ce)+int(max_te)
            tot=int(ce)+int(te)
            
            if int(tot)>=(max_tot)*90/100:
                Grd="A+"
            elif int(tot)>=(max_tot)*80/100:
               Grd="A"
            elif int(tot)>=(max_tot)*70/100:
                Grd="B+"
                
            elif int(tot)>=(max_tot)*60/100:
                Grd="B"
            elif int(tot)>=(max_tot)*50/100:
                Grd="C+"
            elif int(tot)>=(max_tot)*40/100:
                Grd="C"
            elif int(tot)>=(max_tot)*30/100:
                Grd="D+"
            elif int(tot)>=(max_tot)*20/100:
                Grd="D"
            else:
                Grd="E"
        except:
            
            print 'Base not 10 error adding in Calculate Grade()'
            tot=Grd=''
            
        return tot,Grd
       
    def AddPage(self):
        
        self.Score_Table=Table(self.Score_Data,[self.cW1*cm]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])          
        #self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW1*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        self.elements.append(self.Score_Table)
        self.elements.append(Spacer(1, 15))
        self.elements.append(self.Attendance_Table)
        self.elements.append(PageBreak())
        
    def Save(self):
        
        
        import subprocess
                
                        
        
        self.doc.build(self.elements,onFirstPage=self.footer, onLaterPages=self.footer)
        
        try:
                subprocess.call(["xdg-open",self.path])
        except:
            
            print "pdf opening error"
            
            
            
#Basic Science Img
import os,sys

dir = os.path.split(sys.argv[0])[0]

#end BS img
    
class Report_8():
    
    
    def __init__(self,mypagesize=(21*cm,25*cm)):
        
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
        self.DB=db_operations()
        
        
        self.Set_Content()
        
                                            
       
                                                

        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/5.25
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/25
        
        

        #end of measurement

    def Set_Content(self):
        
        global year,class_,name,roll_no,admission_no
        #SCORE TABLE CONTENT STARTS
        self.SCHOOL = Paragraph('''
        <para align=center spaceb=3><b>
        <font size=16>%s

        </font> <br/><br/><font size=13>Chennamangallur</font></b>
        </para>'''% (self.school),
        styleSheet["BodyText"])
            
        self.NAME=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=14><i>Performance Card of : %s</i>
            
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
        
        style = getSampleStyleSheet()
        normal = style["Normal"]
        BS_=Rotated_BS('<font size=10><b>  Basic Science<b></font>', normal)
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
                                    [ BS_,self.PHY, '', '', '','','','', '',''],
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
                                            ('SPAN',(3,2),(4,2)),
                                            
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(3,3),(4,3)),
                                            
                                            ('SPAN',(1,4),(2,4)),
                                            ('SPAN',(3,4),(4,4)),
                                            
                                            ('BOX',(0,0),(-1,-1),2,colors.black)]
                                            
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,YEAR,CLASS,DIV,TERM_INDEX):
        
        div_id=self.DB.Get_Div_Id(YEAR,CLASS,DIV)
        strength=self.DB.Get_Class_Strength(YEAR,CLASS,DIV)
        term=TERM_INDEX
        term1="1"
        term2="2"
        
        #Get Name,Adm No,Roll No, Class,etc
        
        self.year=YEAR
        self.class_=CLASS+' '+DIV
        self.div=DIV
        #self.school="CHENNAMANGALLUR HIGHER SECONDARY SCHOOL"
        self.school=self.DB.Get_School_Name()
        
        working_days1=self.DB.Get_Working_Days(self.year,"1")
        working_days2=self.DB.Get_Working_Days(self.year,"2")
        
        #for term I
            
            
        LAN1=self.DB.Score_and_Roll(term1,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL1=self.DB.Score_and_Roll(term1,div_id,str(1))[1:] 
        ENG1=self.DB.Score_and_Roll(term1,div_id,str(2))[1:] 
        HND1=self.DB.Score_and_Roll(term1,div_id,str(3))[1:] 
        SS1=self.DB.Score_and_Roll(term1,div_id,str(4))[1:] 
        PHY1=self.DB.Score_and_Roll(term1,div_id,str(5))[1:] 
        CHM1=self.DB.Score_and_Roll(term1,div_id,str(6))[1:] 
        BIO1=self.DB.Score_and_Roll(term1,div_id,str(7))[1:] 
        MTH1=self.DB.Score_and_Roll(term1,div_id,str(8))[1:] 
        IT1=self.DB.Score_and_Roll(term1,div_id,str(9))[1:] 
        ATND1=self.DB.Score_and_Roll(term1,div_id,str(10))[1:] 
        
        
        SCORE1=[LAN1,MAL1,ENG1,HND1,SS1,PHY1,CHM1,BIO1,MTH1,IT1]  
        
        #End of Term I
        #Term II
        LAN2=self.DB.Score_and_Roll(term2,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL2=self.DB.Score_and_Roll(term2,div_id,str(1))[1:] 
        ENG2=self.DB.Score_and_Roll(term2,div_id,str(2))[1:] 
        HND2=self.DB.Score_and_Roll(term2,div_id,str(3))[1:] 
        SS2=self.DB.Score_and_Roll(term2,div_id,str(4))[1:] 
        PHY2=self.DB.Score_and_Roll(term2,div_id,str(5))[1:] 
        CHM2=self.DB.Score_and_Roll(term2,div_id,str(6))[1:] 
        BIO2=self.DB.Score_and_Roll(term2,div_id,str(7))[1:] 
        MTH2=self.DB.Score_and_Roll(term2,div_id,str(8))[1:] 
        IT2=self.DB.Score_and_Roll(term2,div_id,str(9))[1:] 
        ATND2=self.DB.Score_and_Roll(term2,div_id,str(10))[1:] 
        
        SCORE2=[LAN2,MAL2,ENG2,HND2,SS2,PHY2,CHM2,BIO2,MTH2,IT2]  
        #End of Term II
        for student_no in range(strength):
            
            
            self.name=SCORE1[0][student_no][3]
            self.roll_no=SCORE1[0][student_no][5]
            self.admission_no=SCORE1[0][student_no][2]
            if self.name=="" and self.roll_no=="" and self.admission_no=="":
                continue
            self.Set_Content()
        
            Data_Col=6
            
            
            for sub_index in range(len(SCORE1)):# this cud b erronious if roll no changes across terms
                
                max_ce,max_te=self.DB.Get_CE_TE(self.year,CLASS,sub_index)
                print "sub indx,ce,te",sub_index,max_ce,max_te              
               
                
                #Term I    
                if sub_index==5:# Physics of Basic Science
                    ad_no1=SCORE1[sub_index][student_no][2]
                    
                    ce1_p=SCORE1[5][student_no][6]
                    te1_p=SCORE1[5][student_no][8]                                        
                    ce1_c=SCORE1[6][student_no][6]
                    te1_c=SCORE1[6][student_no][8]
                    
                    ce1_b=SCORE1[7][student_no][6]
                    te1_b=SCORE1[7][student_no][8]
                    tot1=grade1=''
                    ce_tot1=te_tot1=0
                    try:
                        ce_tot1+=int(ce1_p)
                    except:
                        pass
                    try:
                        te_tot1+=int(te1_p)
                    except:
                        pass
                    try:
                        ce_tot1+=int(ce1_c)
                    except:
                        pass
                    try:
                        te_tot1+=int(te1_c)
                    except:
                        pass
                    try:
                        ce_tot1+=int(ce1_b)
                    except:
                        pass
                    try:
                        te_tot1+=int(te1_b)
                    except:
                        pass
                    
                    tot1,grade1=self.Calculate_Grade(ce_tot1,te_tot1,int(max_ce)*3,int(max_te)*3)
                    
                    
                elif sub_index==6:
                    continue
                elif sub_index==7:
                    continue
                else:
                    ad_no1=SCORE1[sub_index][student_no][2]
                    ce1=SCORE1[sub_index][student_no][6]                
                    te1=SCORE1[sub_index][student_no][8]                
                    tot1=grade1=''
                    if ce1!=('' or None) and te1!=(''or None): 
                           
                        if ce1==''or ce1==None:
                            ce1=0
                        if te1=='' or te1==None:
                            te1=0
                            
                        tot1,grade1=self.Calculate_Grade(ce1,te1,max_ce,max_te)
                    
                      #change here  
                    
                #Term II
                ad_no2=SCORE2[sub_index][student_no][2]
                if ad_no1==ad_no2: # Making sure same student
                    
                    ce2=SCORE2[sub_index][student_no][6]
                    
                    te2=SCORE2[sub_index][student_no][8]                        
                    
                else:
                    ce2=te2=0
                    for each_student in SCORE2[sub_index]:
                        if each_student[2]==ad_no1:
                            ce2=each_student[6]
                            
                            te2=each_student[8]                        
                            
                tot2=grade2=''            
                if ce2!=('' or None) and te2!=(''or None): 
                       
                    if ce2==''or ce2==None:
                        ce2=0
                    if te2=='' or te2==None:
                        te2=0
                        
                
               
                if sub_index==5:# Physics of Basic Science
                    ad_no2=SCORE2[sub_index][student_no][2]
                    
                    ce2_p=SCORE2[5][student_no][6]
                    te2_p=SCORE2[5][student_no][8]
                                        
                    ce2_c=SCORE2[6][student_no][6]
                    te2_c=SCORE2[6][student_no][8]
                    
                    ce2_b=SCORE2[7][student_no][6]
                    te2_b=SCORE2[7][student_no][8]
                    tot2=grade2=''
                    ce_tot2=te_tot2=0
                    try:
                        ce_tot2+=int(ce2_p)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_p)
                    except:
                        pass
                    try:
                        ce_tot2+=int(ce2_c)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_c)
                    except:
                        pass
                    try:
                        ce_tot2+=int(ce2_b)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_b)
                    except:
                        pass
                    
                    tot2,grade2=self.Calculate_Grade(ce_tot2,te_tot2,int(max_ce)*3,int(max_te)*3)
                    
                    
                elif sub_index==6:
                    continue
                elif sub_index==7:
                    continue
                else:
                    ad_no2=SCORE2[sub_index][student_no][2]
                    ce2=SCORE2[sub_index][student_no][6]                
                    te2=SCORE2[sub_index][student_no] [8]               
                    tot2=grade2=''
                    if ce2!=('' or None) and te2!=(''or None): 
                           
                        if ce2==''or ce2==None:
                            ce2=0
                        if te2=='' or te2==None:
                            te2=0
                            
                        tot2,grade2=self.Calculate_Grade(ce2,te2,max_ce,max_te)
                                    
                             
                            
                   
                if Data_Col==11: #Basic Sceince
                    
                    # TermI
                    if ce1_p=='' and te1_p=='' and ce1_c=='' and te1_c=='' and ce1_b=='' and te1_b=='':
                        ce1_p=te1_p=ce1_c=te1_c=ce1_b=te1_b=tot1=grade1=''
                        print 't1 empty'
                    self.Score_Data[Data_Col][2]=str(ce1_p)     #CE      phy      
                    self.Score_Data[Data_Col][3]=str(te1_p)    #TE      phy
                                    
                    self.Score_Data[Data_Col+1][2]=str(ce1_c)       #CE Chem          
                    self.Score_Data[Data_Col+1][3]=str(te1_c)       #TE Chem
                    
                    self.Score_Data[Data_Col+2][2]=str(ce1_b)      #CE Bio      
                    self.Score_Data[Data_Col+2][3]=str(te1_b)        #TE Bio
                    
                    self.Score_Data[Data_Col][4]=str(tot1)      #Tot       
                    self.Score_Data[Data_Col][5]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade1)),
                        styleSheet["BodyText"])   #Grade
                    
                    #End of Term I
                    
                    # TermII
                   
                    
                    if ce2_p=='' and te2_p=='' and ce2_c=='' and te2_c=='' and ce2_b=='' and te2_b=='':
                        ce2_p=te2_p=ce2_c=te2_c=ce2_b=te2_b=tot2=grade2=''
                        
                    self.Score_Data[Data_Col][6]=str(ce2_p)     #CE      phy      
                    self.Score_Data[Data_Col][7]=str(te2_p)    #TE      phy
                                    
                    self.Score_Data[Data_Col+1][6]=str(ce2_c)       #CE Chem          
                    self.Score_Data[Data_Col+1][7]=str(te2_c)       #TE Chem
                    
                    self.Score_Data[Data_Col+2][6]=str(ce2_b)      #CE Bio      
                    self.Score_Data[Data_Col+2][7]=str(te2_b)        #TE Bio
                    
                    self.Score_Data[Data_Col][8]=str(tot2)      #Tot       
                    self.Score_Data[Data_Col][9]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade2)),
                        styleSheet["BodyText"])   #Grade
                    
                    
                    Data_Col+=2 #additional move downwards
                    
                else:
                    #termI
                    
                    if ce1==0 and te1==0:
                        
                        ce1=te1=tot1=grade1=''
                    
                    self.Score_Data[Data_Col][2]=str(ce1)     #CE            
                    self.Score_Data[Data_Col][3]=str(te1)    #TE          
                    self.Score_Data[Data_Col][4]=str(tot1)    #Tot
                                 
                    self.Score_Data[Data_Col][5]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade1)),
                        styleSheet["BodyText"])   #Grade
                    
                
                
                    #End of Term I
                    #TermII
                    
                    
                    if ce2==0 and te2==0:
                        
                        ce2=te2=tot2=grade2=''
                        
                    self.Score_Data[Data_Col][6]=str(ce2)     #CE            
                    self.Score_Data[Data_Col][7]=str(te2)    #TE          
                    self.Score_Data[Data_Col][8]=str(tot2)    #Tot
                                 
                    self.Score_Data[Data_Col][9]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade2)),
                        styleSheet["BodyText"])   #Grade
                        
                    # End of TermII
                    
                
                Data_Col+=1
                
                    
               
            
            
           
                    
                    
                    
                                 
                
                
                
            
            present1=ATND1[student_no][6]    
            present2=ATND2[student_no][6]
            self.Attendance_Data[0][2]=working_days1# Total            
            self.Attendance_Data[1][2]=str(present1)# Present
            
            self.Attendance_Data[0][4]=working_days2#Total            
            self.Attendance_Data[1][4]=str(present2)#Present
            
            self.AddPage()
            student_no+=1

        
           
    def Calculate_Grade(self,ce,te,max_ce,max_te):
        
        max_tot=int(max_ce)+int(max_te)
        tot=int(ce)+int(te)
        
        if int(tot)>=(max_tot)*75/100:
            Grd="A"
        elif int(tot)>=(max_tot)*60/100:
           Grd="B"
        elif int(tot)>=(max_tot)*45/100:
            Grd="C"
            
        elif int(tot)>=(max_tot)*33/100:
            Grd="D"
        
        else:
            Grd="E"
            
        print "returning total, grage",tot,Grd
        return tot,Grd
       
    
    
    
        
    def AddPage(self):
        #self.Score_Table=Table(self.Score_Data,[.3*inch]+[1*inch]+8*[0.6*inch], [.8*inch]+[.6*inch]+14*[0.35*inch])   
        
        self.Score_Table=Table(self.Score_Data,[.5*inch]+[(self.cW1*cm)-.5*inch]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])   
               
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        self.elements.append(self.Score_Table)
        self.elements.append(Spacer(1, 18))
        self.elements.append(self.Attendance_Table)
        self.elements.append(PageBreak())
        
    def Save(self):
        
        

        import subprocess
                
                        
        
        self.doc.build(self.elements)
        
        try:
                subprocess.call(["xdg-open","/tmp/report.pdf"])
        except:
            
            print "pdf opening error"
                                            
 
class Partial_Report():
 

   
    
    def __init__(self,mypagesize=(21*cm,25*cm)):
        
        
        self.path="/tmp/report.pdf"
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
        
        self.DB=db_operations()
        
        self.Set_Content()
        
                                            
       
                                                

        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/4.8
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/25
        
        

        #end of measurement
        
    def Set_Content(self):
        
        
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
        self.Score_T_Style=[
                                
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
                                
                                ('ALIGN',(2,5),(-1,5),'CENTER'), 
                                ('ALIGN',(1,6),(-1,-1),'CENTER')
                                ]
        #End of Score Table                        
                        
        #Starts Attendance Tabke style
        self.Attendance_T_Style=[
                                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

                                            ('SPAN',(0,0),(0,1)),
                                            
                                            ('SPAN',(1,2),(2,2)),
                                            ('SPAN',(3,2),(4,2)),
                                            
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(3,3),(4,3)),
                                            
                                            ('SPAN',(1,4),(2,4)),
                                            ('SPAN',(3,4),(4,4))]
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,YEAR,CLASS,DIV,TERM_INDEX):
        
       
        div_id=self.DB.Get_Div_Id(YEAR,CLASS,DIV)
        term=TERM_INDEX
        term1="1"
        term2="2"
        
        #Get Name,Adm No,Roll No, Class,etc
        
        self.year=YEAR
        self.class_=CLASS+' '+DIV
        self.div=DIV
        #self.school="CHENNAMANGALLUR HIGHER SECONDARY SCHOOL"
        
        
        
        working_days2=self.DB.Get_Working_Days(self.year,"2")
        
        #Term II
        LAN2=self.DB.Score_and_Roll(term2,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL2=self.DB.Score_and_Roll(term2,div_id,str(1))[1:] 
        ENG2=self.DB.Score_and_Roll(term2,div_id,str(2))[1:] 
        HND2=self.DB.Score_and_Roll(term2,div_id,str(3))[1:] 
        SS2=self.DB.Score_and_Roll(term2,div_id,str(4))[1:] 
        PHY2=self.DB.Score_and_Roll(term2,div_id,str(5))[1:] 
        CHM2=self.DB.Score_and_Roll(term2,div_id,str(6))[1:] 
        BIO2=self.DB.Score_and_Roll(term2,div_id,str(7))[1:] 
        MTH2=self.DB.Score_and_Roll(term2,div_id,str(8))[1:] 
        IT2=self.DB.Score_and_Roll(term2,div_id,str(9))[1:] 
        ATND2=self.DB.Score_and_Roll(term2,div_id,str(10))[1:] 
        
        SCORE2=[LAN2,MAL2,ENG2,HND2,SS2,PHY2,CHM2,BIO2,MTH2,IT2]  
        #End of Term II

                  
            
        for n in range(len(LAN2)):
            
            
           
            self.Set_Content()
            
            
            Data_Col=6 
            self.Score_Data[Data_Col][1]=self.Score_Data[Data_Col][2]=self.Score_Data[Data_Col][3]=self.Score_Data[Data_Col][4]=''
            # CE,TE score starts in the 7th inner tuple of tthe score table data
            
            #for EACH_SUB in SCORE:
            for sub_index in range(len(SCORE2)):# this cud b erronious if roll no changes across terms
                
                max_ce,max_te=self.DB.Get_CE_TE(self.year,CLASS,sub_index)                
               
                
                #Term II
               
                
                ad_no2=SCORE2[sub_index][n][2]
                if ad_no2==ad_no2: # Making sure same student
                    
                    ce2=SCORE2[sub_index][n][6]
                    
                    te2=SCORE2[sub_index][n][8]                        
                    
                else:
                    ce2=te2=0
                    for each_student in SCORE2[sub_index]:
                        if each_student[2]==ad_no1:
                            ce2=each_student[6]
                            
                            te2=each_student[8]                        
                            
                tot2=grade2=''            
                if ce2!=('' or None) and te2!=(''or None): 
                       
                    if ce2==''or ce2==None:
                        ce2=0
                    if te2=='' or te2==None:
                        te2=0
                        
                             
                            
                    tot2,grade2=self.Calculate_Grade(ce2,te2,max_ce,max_te)
                    
                    
                    
                    
                                 
                
                
                
            #Term II
                self.Score_Data[Data_Col][5]=str(ce2)               
                self.Score_Data[Data_Col][6]=str(te2)              
                self.Score_Data[Data_Col][7]=str(tot2)             
                #self.Score_Data[Data_Col][4]=str(sheet.cell(row,col+3).value).split(".")[0]
                
                
                self.Score_Data[Data_Col][8]= Paragraph('''
                    <para align=center spaceb=3><b>
                    <font size=12><i>%s</i>
                    
                   </font> </b>
                    </para>'''%(str(grade2)),
                    styleSheet["BodyText"]) 
                    
                    
                Data_Col+=1
                sub_index+=1
                
            
            
            
               
            present2=ATND2[n][6]
            
            
            self.Attendance_Data[0][4]=working_days2#Total            
            self.Attendance_Data[1][4]=str(present2)#Present
            
            self.AddPage()
            n+=1
    def Calculate_Grade(self,ce,te,max_ce,max_te):
        try:
            max_tot=int(max_ce)+int(max_te)
            tot=int(ce)+int(te)
            
            if int(tot)>=(max_tot)*90/100:
                Grd="A+"
            elif int(tot)>=(max_tot)*80/100:
               Grd="A"
            elif int(tot)>=(max_tot)*70/100:
                Grd="B+"
                
            elif int(tot)>=(max_tot)*60/100:
                Grd="B"
            elif int(tot)>=(max_tot)*50/100:
                Grd="C+"
            elif int(tot)>=(max_tot)*40/100:
                Grd="C"
            elif int(tot)>=(max_tot)*30/100:
                Grd="D+"
            elif int(tot)>=(max_tot)*20/100:
                Grd="D"
            else:
                Grd="E"
        except:
            print 'errorin calculate grade()'
            tot=Grd=''
            
        return tot,Grd
       
    def AddPage(self):
        
        self.Score_Table=Table(self.Score_Data,[self.cW1*cm]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])          
        #self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW1*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
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
            
            print "pdf opening error"
            
            
            
#Basic Science Img
import os,sys

dir = os.path.split(sys.argv[0])[0]
I = Image(dir+'/Resources/BS.gif')
"""I.drawHeight =1*inch
I.drawWidth=.3*inch
"""
#end BS img
    
class Partial_Report_8():
    
    
    def __init__(self,mypagesize=(21*cm,25*cm)):
        
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
        self.DB=db_operations()
        
        
        self.Set_Content()
        
                                            
       
                                                

        # Starts measurement

        self.cW1=(mypagesize[0]/cm)/5.25
        self.cW=(mypagesize[0]/cm)/11.6

        self.rH1=(mypagesize[1]/cm)/14
        self.rH2=(mypagesize[1]/cm)/19
        self.rH=(mypagesize[1]/cm)/25
        
        

        #end of measurement

    def Set_Content(self):
        
        
        self.Score_Data=   [['', '', '', '','','','','','',''],
                                    ['',  '', '','', '','','','', '',''],
                                    ['', '', '', '', '','','','', '',''],
                                    ['', '', '', '', '','','','', '',''],
                                    ['','','', '', '','','','', '',''],
                                    ['','',  '', '', '','','','', '',''],
                                    ['', '', '', '', '','','','', '',''],
                                    ['',  '', '','', '','','','', '',''],
                                    ['', '', '','', '','','','', '',''],
                                    ['', '', '','', '','','','', '',''],
                                    ['', '', '','', '','','','', '',''],
                                    [ '','', '', '', '','','','', '',''],
                                    ['','', '',  '', '','','','', '',''],
                                    ['','', '', '', '','','','', '',''],
                                    ['','', '', '', '','','','', '',''],
                                    ['',  '', '', '','','','','', '','']]
                                    
                                    
                                    
        
        
        self.Attendance_Data=[['','','','',''],
                                            ['','','','','',''],
                                            ['','','','',''],
                                            ['','','','',''],
                                            ['','','','','']]
                                            
                                            
    def SetTable_Style(self):
        
        #Starts Score Table
        self.Score_T_Style=[#
                    
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
                    
                    ('ALIGN',(2,6),(-1,-1),'CENTER') # Score center
                    
                    
                    ]
        #End of Score Table                        
                        
        #Starts Attendance Tabke style
        self.Attendance_T_Style=[
                                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

                                            ('SPAN',(0,0),(0,1)),
                                            
                                            ('SPAN',(1,2),(2,2)),
                                            ('SPAN',(3,2),(4,2)),
                                            
                                            ('SPAN',(1,3),(2,3)),
                                            ('SPAN',(3,3),(4,3)),
                                            
                                            ('SPAN',(1,4),(2,4)),
                                            ('SPAN',(3,4),(4,4))]
                                            
                                            
        #end of Attendance Table Style 
        
       
        
    def PopulateTables(self,YEAR,CLASS,DIV,TERM_INDEX):
        
        div_id=self.DB.Get_Div_Id(YEAR,CLASS,DIV)
        strength=self.DB.Get_Class_Strength(YEAR,CLASS,DIV)
        term=TERM_INDEX
        term1="1"
        term2="2"
        
        #Get Name,Adm No,Roll No, Class,etc
        self.year=YEAR
        self.class_=CLASS+' '+DIV
        self.div=DIV
        
        
       
        working_days2=self.DB.Get_Working_Days(self.year,"2")
        
       
        #Term II
        LAN2=self.DB.Score_and_Roll(term2,div_id,str(0))[1:] # Skipping first element as data start from the 2nd
        MAL2=self.DB.Score_and_Roll(term2,div_id,str(1))[1:] 
        ENG2=self.DB.Score_and_Roll(term2,div_id,str(2))[1:] 
        HND2=self.DB.Score_and_Roll(term2,div_id,str(3))[1:] 
        SS2=self.DB.Score_and_Roll(term2,div_id,str(4))[1:] 
        PHY2=self.DB.Score_and_Roll(term2,div_id,str(5))[1:] 
        CHM2=self.DB.Score_and_Roll(term2,div_id,str(6))[1:] 
        BIO2=self.DB.Score_and_Roll(term2,div_id,str(7))[1:] 
        MTH2=self.DB.Score_and_Roll(term2,div_id,str(8))[1:] 
        IT2=self.DB.Score_and_Roll(term2,div_id,str(9))[1:] 
        ATND2=self.DB.Score_and_Roll(term2,div_id,str(10))[1:] 
        
        SCORE2=[LAN2,MAL2,ENG2,HND2,SS2,PHY2,CHM2,BIO2,MTH2,IT2]  
        #End of Term II
        for student_no in range(strength):
            
            
            
            self.Set_Content()
        
            Data_Col=6
            
            
            for sub_index in range(len(SCORE2)):# this cud b erronious if roll no changes across terms
                
                max_ce,max_te=self.DB.Get_CE_TE(self.year,CLASS,sub_index)                
               
                
                #Term II
                ad_no2=SCORE2[sub_index][student_no][2]
                if ad_no2==ad_no2: # Making sure same student
                    
                    ce2=SCORE2[sub_index][student_no][6]
                    
                    te2=SCORE2[sub_index][student_no][8]                        
                    
                else:
                    ce2=te2=0
                    for each_student in SCORE2[sub_index]:
                        if each_student[2]==ad_no1:
                            ce2=each_student[6]
                            
                            te2=each_student[8]                        
                            
                tot2=grade2=''            
                if ce2!=('' or None) and te2!=(''or None): 
                       
                    if ce2==''or ce2==None:
                        ce2=0
                    if te2=='' or te2==None:
                        te2=0
                        
                
               
                if sub_index==5:# Physics of Basic Science
                    ad_no2=SCORE2[sub_index][student_no][2]
                    
                    ce2_p=SCORE2[5][student_no][6]
                    te2_p=SCORE2[5][student_no][8]
                                        
                    ce2_c=SCORE2[6][student_no][6]
                    te2_c=SCORE2[6][student_no][8]
                    
                    ce2_b=SCORE2[7][student_no][6]
                    te2_b=SCORE2[7][student_no][8]
                    tot2=grade2=''
                    ce_tot2=te_tot2=0
                    try:
                        ce_tot2+=int(ce2_p)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_p)
                    except:
                        pass
                    try:
                        ce_tot2+=int(ce2_c)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_c)
                    except:
                        pass
                    try:
                        ce_tot2+=int(ce2_b)
                    except:
                        pass
                    try:
                        te_tot2+=int(te2_b)
                    except:
                        pass
                    
                    tot2,grade2=self.Calculate_Grade(ce_tot2,te_tot2,int(max_ce)*3,int(max_te)*3)
                    
                    
                elif sub_index==6:
                    continue
                elif sub_index==7:
                    continue
                else:
                    ad_no2=SCORE2[sub_index][student_no][2]
                    ce2=SCORE2[sub_index][student_no][6]                
                    te2=SCORE2[sub_index][student_no] [8]               
                    tot2=grade2=''
                    if ce2!=('' or None) and te2!=(''or None): 
                           
                        if ce2==''or ce2==None:
                            ce2=0
                        if te2=='' or te2==None:
                            te2=0
                            
                        tot2,grade2=self.Calculate_Grade(ce2,te2,max_ce,max_te)
                                    
                             
                            
                   
                if Data_Col==11: #Basic Sceince
                    
                    
                    # TermII
                    self.Score_Data[Data_Col][6]=str(ce2_p)     #CE      phy      
                    self.Score_Data[Data_Col][7]=str(te2_p)    #TE      phy
                                    
                    self.Score_Data[Data_Col+1][6]=str(ce2_c)       #CE Chem          
                    self.Score_Data[Data_Col+1][7]=str(te2_c)       #TE Chem
                    
                    self.Score_Data[Data_Col+2][6]=str(ce2_b)      #CE Bio      
                    self.Score_Data[Data_Col+2][7]=str(te2_b)        #TE Bio
                    
                    self.Score_Data[Data_Col][8]=str(tot2)      #Tot       
                    self.Score_Data[Data_Col][9]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade2)),
                        styleSheet["BodyText"])   #Grade
                    
                    
                    Data_Col+=2 #additional move downwards
                    
                else:
                    #TermII
                    self.Score_Data[Data_Col][6]=str(ce2)     #CE            
                    self.Score_Data[Data_Col][7]=str(te2)    #TE          
                    self.Score_Data[Data_Col][8]=str(tot2)    #Tot
                                 
                    self.Score_Data[Data_Col][9]= Paragraph('''
                        <para align=center spaceb=3><b>
                        <font size=12><i>%s</i>
                        
                       </font> </b>
                        </para>'''%(str(grade2)),
                        styleSheet["BodyText"])   #Grade
                        
                    # End of TermII
                    
                
                Data_Col+=1
                
                    
             
                
            present2=ATND2[student_no][6]
            
            
            self.Attendance_Data[0][4]=working_days2#Total            
            self.Attendance_Data[1][4]=str(present2)#Present
            
            self.AddPage()
            student_no+=1

        
           
    def Calculate_Grade(self,ce,te,max_ce,max_te):
        
        max_tot=int(max_ce)+int(max_te)
        tot=int(ce)+int(te)
        
        if int(tot)>=(max_tot)*75/100:
            Grd="A"
        elif int(tot)>=(max_tot)*60/100:
           Grd="B"
        elif int(tot)>=(max_tot)*45/100:
            Grd="C"
            
        elif int(tot)>=(max_tot)*33/100:
            Grd="D"
        
        else:
            Grd="E"
        
        return tot,Grd
       
    
    
    
        
    def AddPage(self):
        #self.Score_Table=Table(self.Score_Data,[.3*inch]+[1*inch]+8*[0.6*inch], [.8*inch]+[.6*inch]+14*[0.35*inch])   
        
        self.Score_Table=Table(self.Score_Data,[.5*inch]+[(self.cW1*cm)-.5*inch]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])   
               
        self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        self.elements.append(self.Score_Table)
        self.elements.append(Spacer(1, 18))
        self.elements.append(self.Attendance_Table)
        self.elements.append(PageBreak())
        
    def Save(self):
        
        

        import subprocess
                
                        
        
        self.doc.build(self.elements)
        
        try:
                subprocess.call(["xdg-open","/tmp/report.pdf"])
        except:
            
            print "pdf opening error"
                                            
 
 