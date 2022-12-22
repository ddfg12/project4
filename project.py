import os
import shutil
from_dir="C:/Users/User/Downloads"
to_dir="C:/Users/User/Desktop/c-101/documents"
listoffiles=os.listdir(from_dir)
#print(listoffiles)
for file_name in listoffiles:
    name,extension = os.path.splitext (file_name)
    print(name)
    print(extension)
    if extension=='':
        continue
    if extension in ['.txt','.doc','.doxc','.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir + '/' + "Document_Files"
        path3=to_dir + '/' + "Document_Files" + '/' + file_name
if os.path.exists(path2):
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)        
else:
    os.makedirs(path2)
    print("Moving"+file_name+".....")
    shutil.move(path1,path3)