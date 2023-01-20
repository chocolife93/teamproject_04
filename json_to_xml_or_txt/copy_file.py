import shutil
import os
import xml.etree.ElementTree as ET
import pandas as pd
# import cv2
import json
import glob
import math

def copy_file(from_path,to_path):
    file_paths = glob.glob(from_path)
    for file_path in file_paths:
        shutil.copyfile(file_path, to_path)

# source = r"D:\Image\i1.png"
#
# destination = r"D:\Image1\i1.png"
#
# shutil.copyfile(source, destination)

path = 'D:/falldown/'
# T_or_V = ['Training', 'Validation']
T_or_V = ['Validation']
img_or_vid = ['image', 'video']
to_folder = 'C:/Users/ASIAE-12/Desktop/img2/'

for t_or_v_01 in T_or_V:
    img_path_01 = '{}{}/image/'.format(path, t_or_v_01)
    img_path_01_names = os.listdir(img_path_01)
    removed_img_path_01_name = []
    for i in img_path_01_names:
        if 'image_' in i:
            removed_img_path_01_name.append(i)
        for img_path_name in removed_img_path_01_name:
            img_path_02 = img_path_01 + img_path_name + '/'
            # print(img_path_02)
            img_path_02_names = os.listdir(img_path_02)
            for img_path_02_name in img_path_02_names:
                img_path_03 = img_path_02 + img_path_02_name + '/'
                # print(img_path_03)
                img_jpg_paths = glob.glob(img_path_03 + '*.jpg')
                for img_jpg_path in img_jpg_paths:
                    img_name = img_jpg_path[-44:]
                    # print('img_name',img_name)
                    to_path = to_folder + img_name
                    print(img_jpg_path)
                    print(to_path)
                    shutil.copyfile(img_jpg_path, to_path)



