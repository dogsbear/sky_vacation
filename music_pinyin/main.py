import os
import glob
from pypinyin import pinyin, lazy_pinyin, Style

print(os.getcwd())

all_mp3 = glob.glob('C:\\Users\\dogsb\\Music\\test1\\*.mp3')

fileExt = r".mp3"

target_dir = 'C:\\Users\\dogsb\\Music\\test1\\'
path = os.listdir(target_dir)

for fd in path:
    if fd.endswith(fileExt) == False:
        continue
    print("Org name:", fd)
    new_name_list = lazy_pinyin(fd)
    for i in range(len(new_name_list) - 1):
        new_name_list[i] = new_name_list[i].title()
    new_name = "".join(new_name_list)
    print("New name:", new_name)
    
    os.rename(os.path.join(target_dir, fd), os.path.join(target_dir, new_name))

for music in all_mp3:
    base_name = os.path.basename(music)
    #print(base_name)
    result = lazy_pinyin(base_name)
    #print(result)

    for i in range(len(result) - 1):
        result[i] = result[i].title()
        
    new_string = "".join(result)
    #print(new_string)