
import requests
import operator
from lxml import html
import string
from requests.exceptions import ConnectionError
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from dboperations import db_operations



#from parse_sampoona import html_parser 

#NEXT PAGE= http://sampoorna.itschool.gov.in/6540/reports/show/278310?page=7


class sampoorna_reports():
    # Updates the database in sync with sampoorna
    def __init__(self):
        
        
        self.report_name=""
        self.session_request = requests.session()
        self.token=''
        self.class_=''
        self.year=''

    def find_show_link(self,xml): # finds out the link that leads to show a particular reprt. With this other
        #links like delete report can be fetched
        
        pos=xml.find(self.report_name)# checking if report already exists
        newpos=xml.find('<a href=',pos)
        newpos2=xml.find('"',newpos)
        newpos3=xml.find('"',newpos2+1)        
        link=xml[newpos2+1:newpos3]   
        
        
        link="http://sampoorna.itschool.gov.in"+link
        return link

    def get_report_index_page(self):# old get_xml

        # this function loads the sampoorna page that shows the list of all the custom reports
        url='http://sampoorna.itschool.gov.in/'+self.school_code+'/reports/index/student'

        result = self.session_request.get(url)

        xml=str(result.content)
        return xml
    def delete_report(self):
        
        xml=self.get_report_index_page()
       
        pos=xml.find(self.report_name)# checking if report already exists
        
        if (pos==-1):
            print " no report named",self.report_name
            return [True]
            
        else:
            
            link=self.find_show_link(xml)       
            link=link.replace('show','delete')# finds the link to show and change it to delete
            
            
            try:
                self.session_request.get(link)
                return [True]
            except ConnectionError as e:    # This is the correct syntax
               return False, " Check your Internet Connection"
            
    def get_show_report_link(self):# old showreport
        # Return the link that refers to the first page(if added page=1) of the report
        xml=self.get_report_index_page()
        link=self.find_show_link(xml)
        
        return link
    def get_page_wise_data(self,link):  

        # Receives links to pages of a single report extended over multiple pages
        
        # Open & Clsoe to solve data type errors

        result=self.session_request.get(link)
        f=open("/tmp/.output.html",'wb')

        f.write(result.content)
        f.close()
        import codecs
        f=codecs.open("/tmp/.output.html",encoding='utf-8')

        data= f.read()
        f.close
        return data
                
    def create_report(self):
        
        
        
        # before creating new report name check if rportpage if the name is unique, if not delete that report
        url='http://sampoorna.itschool.gov.in/'+self.school_code+'/reports/generate/student'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        
        report_field='course'
        col_name='course'
        table_name='Student'
        criteria='in'
        col_type='association'
        class_=self.class_
        
        title1='Class'
        method1='course'
        position1='1'
        destroy1='0'
        
        title2='Division'
        method2='batch'
        position2='2'
        destroy2='0'
        
        title3='Admission_No'
        method3='admission_no'
        position3='3'
        
        title4='Name'
        method4='full_name'
        position4='4'
        
        title5='UID'
        method5='uid'
        
        title6='Gender'
        method6='gender'
        
        title7='DOB'
        method7='date_of_birth'
        
        title8='Category'
        method8='reservation_group'
        
        title9='Religion'
        method9='religion'
        
        title10='Caste'
        method10='caste_name'
        
        title11='First_Language'
        method11='first_language'
        
        title12='Father'
        method12='father_full_name'
        
        title13='Mother'
        method13='mother_full_name'
        
        title14='Phone'
        method14='phone1'
        
        login_data =  {'authenticity_token':self.token,'report[name]':self.report_name, 'report[model]':'Student',
        'report_fields[course][]':report_field,'report[report_queries_attributes][67][column_name]':col_name,
        'report[report_queries_attributes][67][table_name]':table_name, 
        'report[report_queries_attributes][67][criteria]':criteria,
        'report[report_queries_attributes][67][column_type]':col_type,
        'report[report_queries_attributes][67][query][]':class_,
        
        'report[report_columns_attributes][30][title]':title1,
        'report[report_columns_attributes][30][method]':method1,
        'report[report_columns_attributes][30][position]':position1,
        'report[report_columns_attributes][30][_destroy]':destroy1,
        
        'report[report_columns_attributes][31][title]':title2,
        'report[report_columns_attributes][31][method]':method2,
        'report[report_columns_attributes][31][position]':position2,
        'report[report_columns_attributes][31][_destroy]':'0',
        
        'report[report_columns_attributes][9][title]':title3,
        'report[report_columns_attributes][9][method]':method3,
        'report[report_columns_attributes][9][position]':position3,
        'report[report_columns_attributes][9][_destroy]':'0',
        
        'report[report_columns_attributes][2][title]':title4,
        'report[report_columns_attributes][2][method]':method4,
        'report[report_columns_attributes][2][position]':position4,
        'report[report_columns_attributes][2][_destroy]':'0',
        
        'report[report_columns_attributes][1][title]':title5,
        'report[report_columns_attributes][1][method]':method5,
        'report[report_columns_attributes][1][position]':'5',
        'report[report_columns_attributes][1][_destroy]':'0',
        
        'report[report_columns_attributes][4][title]':title6,
        'report[report_columns_attributes][4][method]':method6,
        'report[report_columns_attributes][4][position]':'6',
        'report[report_columns_attributes][4][_destroy]':'0',
        
        'report[report_columns_attributes][27][title]':title7,
        'report[report_columns_attributes][27][method]':method7,
        'report[report_columns_attributes][27][position]':'7',
        'report[report_columns_attributes][27][_destroy]':'0',
        
        'report[report_columns_attributes][43][title]':title8,
        'report[report_columns_attributes][43][method]':method8,
        'report[report_columns_attributes][43][position]':'8',
        'report[report_columns_attributes][43][_destroy]':'0',
        
        'report[report_columns_attributes][33][title]':title9,
        'report[report_columns_attributes][33][method]':method9,
        'report[report_columns_attributes][33][position]':'9',
        'report[report_columns_attributes][33][_destroy]':'0',
        
        'report[report_columns_attributes][13][title]':title10,
        'report[report_columns_attributes][13][method]':method10,
        'report[report_columns_attributes][13][position]':'10',
        'report[report_columns_attributes][13][_destroy]':'0',
        
        'report[report_columns_attributes][36][title]':title11,
        'report[report_columns_attributes][36][method]':method11,
        'report[report_columns_attributes][36][position]':'11',
        'report[report_columns_attributes][36][_destroy]':'0',
        
        'report[report_columns_attributes][17][title]':title12,
        'report[report_columns_attributes][17][method]':method12,
        'report[report_columns_attributes][17][position]':'12',
        'report[report_columns_attributes][17][_destroy]':'0',
        
        'report[report_columns_attributes][16][title]':title13,
        'report[report_columns_attributes][16][method]':method13,
        'report[report_columns_attributes][16][position]':'13',
        'report[report_columns_attributes][16][_destroy]':'0',
        
        
        'report[report_columns_attributes][8][title]':title14,
        'report[report_columns_attributes][8][method]':method14,
        'report[report_columns_attributes][8][position]':'14',
        'report[report_columns_attributes][8][_destroy]':'0',
        'commit':'Save'}
        result = self.session_request.post(
        url, 
        data = login_data, 
        
        headers = headers
        )
        
        if result.content.find("Report Created successfully ")!=-1:
            return [True]
        return False, "Failed to create report"
        
    
    def login(self,user='',passw=''):
        
        

        url="http://sampoorna.itschool.gov.in/"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        




        
        try:
            result = self.session_request.get(url)
                        
            tree = html.fromstring(result.text)
            self.token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
            login_data =  {'authenticity_token':self.token, 'user[username]':user, 'user[password]':passw,'commit':'Login'}
            

            result = self.session_request.post(
                url, 
                data = login_data, 
                #headers = dict(referer=url)
                headers = headers)
            check=self.check_login(result.text)
            if check[0]:
                self.school_code= result.url.split('/')[3]
                return [True]
            return check # return [False, "Error details"]
            
        except ConnectionError as e:    # This is the correct syntax
               return False, "Check your Internet Connection"
               r = "No response"
    def check_login(self,text):
        
        if text.find("Invalid username")==-1:
            
            return [True]
        return False,"Invalid Username Password combination"
        
    def make_report_name(self,std): # oldget_report_data
        
        #Just Creates names for reports
        
        self.class_=std
        if std=='8':
            self.report_name="smart_school_8"
        elif std=='9':
            self.report_name="smart_school_9"
        elif std=='10':
            
            self.report_name="smart_school_10"
            
        return html    
   
    def sort_by_div(self,list):
        
        
                    
        new_list=[]
        i=0
        
        
      
        count=0
        for i in list:
            new_i=[]
            for j in i:
                
                new_j=str(j)
                new_i.append(new_j)
                
                if count<10:
                    #print "newj ",new_j
                    pass
                    
                count+=1
            new_list.append(new_i)
        #print "stringed list\n"
        #
        #print new_list
        
        splitted_list=[]
        
        for i in new_list:
            # class div year '10 M 2016-2017' comb to division
            
            if i!=[] and i!='[]':
                             
                    
                
                
                div=i[2].split(" ")[1]
                self.year=i[2].split(" ")[2].split("-")[0]
                i[2]=(div)
               
                splitted_list.append(i)            
        
        
        sorted_list=sorted(splitted_list, key=operator.itemgetter(2, 4))
        return sorted_list
    
  
class insert_to_db():
    
    def __init__(self):
        
        
        self.insert_count=0
        self.update_count=0
        
        self.DB=db_operations()
        
    def update_student(self,year,student_details):
        self.update_count+=1
        # Roll is appended as the last item, becasue this DB function is used by othr classses in this format
        self.DB.Update_Student_Full(year,student_details,commit=False)
        
        
    def insert_student(self,year,list,email=''):

        #['8', '9', 'A', '12431', 'ABHAY DAS P', '600756142234', 'M', '14/10/2002', 'SC', 'Hindu', 'Valluva', 'Malayalam ', 'SIVADASAN', 'SHEEBA', '9846249576']
        roll=1
        div=list[0][2]
        for item in list:
            if div!=item[2]:# Roll number is automatically assigned. Restarts on new division
                roll=1
                div=item[2]
                
            if self.DB.Student_Exists(item[3]):

                self.update_student(year,item+[email,roll])
                
            else:
                self.DB.Add_Student_Full(year,item+[email,roll],commit=False)
                self.insert_count+=1
            
                
                
            roll+=1
            
