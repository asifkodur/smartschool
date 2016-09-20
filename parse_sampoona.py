

from HTMLParser import HTMLParser



def get_table_html():
    import codecs
    f=codecs.open("/home/kkv/Desktop/output.html",encoding='utf-8')

    html=f.read()
    beg_pos= html.find("<table")
    end_pos=html.find("</table>")
    table_data= html[beg_pos:end_pos].encode('utf-8')+"</table>".encode('utf-8')

    f.close()
    return html













class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.F_DATA=[]   #KEEPS WHOLE TABLE DATA OF THE WEBPAGE
        self.TABLE=[]
        self.ROW=[]


        
        self.table_no=0
        self.row_no=0
        self.col_no=0
        self.current_table=0
        self.current_row=0
        self.current_col=0
        self.print_flag=False
        self.col_data=''
        self.pagination=False
        
        self.first_page=False# sets true only if processing the first page of the output for it is from that
        #page the links of next pages of reports are fetched
        self.page_link_list=[] # Stores total pages found in the first page"
        

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            
            self.current_table+=1
            
            
        elif tag=='tr':
            self.current_row+=1
            
        elif tag=='td':
            
            self.current_col+=1
            self.print_flag=True
            
        elif tag=='div':
            if len(attrs[0])>1:
                if attrs[0][1]==u'pagination':
                    
                    self.pagination=True
                
        elif tag=='a':
            
            
            if self.pagination and self.first_page:
               
                self.page_link_list.append(attrs[0][1].split('=')[1]) # gets page numer from attribs like "reports/show/677258?page=19"


    def handle_data(self, data):
        
        if self.print_flag:
            
            self.col_data+=data
            
        
            
        #print data

    def handle_endtag(self, tag):
        if tag=="table":
            
            self.current_row=0
            self.current_col=0
            self.F_DATA.append(self.TABLE)
            #self.TABLE=[]
            
            
        elif tag=='tr':
            
            self.current_col=0
            self.TABLE.append(self.ROW)
            self.ROW=[]
        elif tag=='td':
            
            
            self.ROW.append(self.col_data)
            self.print_flag=False
            self.col_data=''
            
        elif tag=='div':
            if self.pagination==True:
                self.pagination=False
                
        
    def feed_html(self,html,first_page=False):
        
        self.first_page=first_page
        self.feed(html)
    def get_no_page(self):
        return sorted(map(int,self.page_link_list)).pop()# returns the last item (max number) in sorted list
'''
parser = html_parser()

import codecs
f=codecs.open("/home/kkv/Desktop/output.html",encoding='utf-8')

html=f.read()
#print text
print parser.TABLE
parser.feed(html)

for row in parser.TABLE:
    
    if row!=[]:
        print row,"\n"
        
        
'''