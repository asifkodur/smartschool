
import os
ext=".py"


import os
def a():
    results = []

    for folder in gamefolders:
        for f in os.listdir(folder):
            if f.endswith(ext):
                results.append(f)

    print results

#results += [each for each in os.listdir(folder) if each.endswith(extension)]
#print results
def b():
    

    import os, re
    cfile = re.compile("^.*?\.py$")
    results = []
    lines=0
    total=0
    for name in os.listdir('/home/ghssvythiri/asif/smart_school'):
        if cfile.match(name):
            results.append(name)
            f=open("/home/ghssvythiri/asif/smart_school/"+name,'rb')
            lines=f.readlines()
            print name,"   ",len(lines)
            total+=len(lines)
    print "*****total lines=",total
            
    #print results
    
b()
            


