 # -*- coding: utf-8 -*-
import os
from _ctypes import Array

def get_all_file_in_dir(dir):
    all_files = {}
    for parent,dirnames,filenames in os.walk(dir):   
        for filename in filenames :
            all_files[filename]=(os.path.join(parent,filename))                  
            #print os.path.join(parent,filename)
    return all_files