import os
import shutil
path ="./"
files = os.walk(path)
if not os.path.exists('./doc&xls'):
    os.makedirs('doc&xls')
if not os.path.exists('./ppt&pdf'):
    os.makedirs('ppt&pdf')

# 找出所有文件
file_list = []
for root,dirs,file in files:
        for file_s in file:
           file_path = os.path.join(root,file_s)
           file_list.append(file_path)
print(file_list)

### 移动文件
##for f in file_list:           
##    if 'doc' in f or 'xls' in f:
##       shutil.move(f,'./doc&xls')
##    if 'ppt' in f or 'pdf' in f:
##       shutil.move(f,'./ppt&pdf')

# 找出空文件夹
files_new = os.listdir(path)
for file in files_new:
    print(file)
    if os.path.isdir(file):  #如果是文件夹
        if not os.listdir(file): #如果子文件夹为空
            os.rmdir(file)      # 删除空的文件夹
    
