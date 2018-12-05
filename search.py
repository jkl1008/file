import os
import shutil
path ="./"
files = os.listdir(path)
for f in files:
    if f != 'search.py' :
        folder_name = './' + f.split('.')[-1][:3]
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            shutil.move(f, folder_name)
        else:
            shutil.move(f, folder_name)