import os   
import os.path   
rootdir = "D:/myCodes/codes/Python3/resources/"  
for parent,dirnames,filenames in os.walk(rootdir):   
    # case 1:   
    for dirname in dirnames:   
       print ( "parent is:" + parent)   
       print ( " dirnames is:" + dirname)   
    # case 2:   
    for filename in filenames:   
       print ( " parent is:" + parent)   
       print ( " filename with full path:" + os.path.join(parent,filename)) 

def getFileText(fileName):
    fileName = rootdir+'/JTracTSGPRD-55136.htm'
    print(fileName)
    file = open(fileName,'r')
    try:
        fileText = file.read();
#     list_of_all_the_lines = file.readlines()
#     print(list_of_all_the_lines)
    finally:
        file.close()
    return fileText
# for line in list_of_all_the_lines:
#     print(line)