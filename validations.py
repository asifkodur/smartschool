class validate():
    
    def __init__(self):
        pass
        
    def validate_uid(self,uid):
        if not uid:# uid is not manadtory
            return [True]
        if not uid.isdigit() or len(uid)!=12:
            return False,"Invalid  UID"
        return [True]

    def validate_admission_no(self,ad_no):
        if not ad_no.isdigit():
            return False,"Admission Number Should be a Number"
        
        return [True]
            
    def validate_roll(self,roll):
        if not roll:
            return [True]
        if not roll.isdigit():
            return False,"Invalid Roll Number"
        return [True]
        
    def validate_mobile(self,mobile):
        if not mobile:# Mobile not manadtory
            
            return [True]
        if not mobile.isdigit():
            
            return False,"Invalid Mobile Number"
        if len(mobile)!=10:
            
            return False, "Mobile Number Must Contain Exactly 10 digits or it can be empty"
        
        return [True]
        
    def validate_email(self,email):
        import re
        if not email:
            return [True]
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)


        if match == None:
           
            #raise ValueError('Bad Syntax')
            return False,"Invalid email. The filed can be empty"
        return [True]
    def validate_date(self,mydate):
        
        if not mydate:
            return [True]
        import datetime
        
        splt=mydate.split("/")
        if len(splt[0])!=2 or len(splt[1])!=2 or len(splt[2])!=4:
            
            return False,"  Invalid Date or Format.The field can be empty"

        try:
            datetime.datetime.strptime(mydate,'%d/%m/%Y')
        except ValueError:

            return False," Invalid Date or Format. The field can be empty"
        return [True]
    def validate_photo(self,path):
        import wx

        img = wx.Image(path, wx.BITMAP_TYPE_ANY)
            # scale the image, preserving the aspect ratio
        W=img.GetWidth()
        H=img.GetHeight()
        if W>120 or H>120 or W<100 or H<100:
            return False," Image Height and Width must be between 100-120 pixels"
        
        return [True]

