import os
import re

def walk_change_table(dir='./'):
    for root,dirs,files in os.walk(dir):
        for cur_file in files:
            file_content = []
            with open(cur_file,'r',encoding='UTF-8') as f:
                file_content = f.read()
            file_content = file_content.replace('\t-',' -')
            with open(cur_file,'w',encoding='UTF-8') as f:
                f.write(file_content)

if __name__ == '__main__':
    walk_change_table()

