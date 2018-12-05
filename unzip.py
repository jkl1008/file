import os
import shutil
zip_file = []

# 找出所有压缩文件
def scan():
    files = os.walk('./')
    for root,dirs,name in files:
        for f in name:
            if (os.path.splitext(f)[1][1:] in ['zip'])  or ('8z' in os.path.splitext(f)[1][1:]) :
                f_path = os.path.join(root,f)
                zip_file.append(f_path)
    return zip_file
print(scan())
#解压文件到以压缩文件名命名的文件内

def unzip(zip_file):
    for f in zip_file:
        target_path = os.path.splitext(f)[0]
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        shutil.unpack_archive(f, target_path)


def delete(zip_file):
    for f in zip_file:
        if os.path.exists(f):
            os.remove(f)

while True:
    zip_file = scan()
    if  len(zip_file) >0 :
        unzip(zip_file)
        delete(zip_file)

