#检查17年运动员被试文件是否确实
import pandas as pd
import os
from pathlib import Path 
def check_file(list_source,filedir_source):
    errorcheck_txt = open('Errorfile.txt','w')
    for list in os.listdir(list_source):
        print(list)
        errorcheck_txt.write(f"check for:{list}\n")
        data = pd.read_excel(Path(list_source)/list)
        for file in os.listdir(Path(filedir_source)/list):
            file = file.lower()
            file = file.replace('_','')
        for name in data["姓名"]:
            name = name.lower()
            name = name.replace('_','')
            print(name)
            if not os.path.exists(Path(filedir_source)/list/name):
                errorcheck_txt.write(f"name:{file}\n")
    errorcheck_txt.flush()
    errorcheck_txt.close()

if __name__ == '__main__':
    list_source = r'G:\GranduationProject\2018athlete\list\list_origin'
    filedir_source = r'E:\athlete2017\201637\rest'
    check_file(list_source,filedir_source)