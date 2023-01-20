import os
import shutil
import glob

dir = 'D:/work/python/datasets/falldown/images/train/' #옮길 폴더
src00 = 'D:/falldown/Training/image/Abnormal_Behavior_Falldown/'
labels = ['H11H21H31', 'H11H21H32', 'H11H21H33', 'H11H22H31',
                         'H11H22H32', 'H11H22H33', 'H12H21H31', 'H12H21H32',
                         'H12H21H33', '12H22H31', 'H12H22H32', 'H12H22H33']
def src_path_list(src00):
    src_list = []
    folder_list00 = os.listdir(src00)
    for folder_name in folder_list00:
        if folder_name in labels:
            src01 = src00 + folder_name + '/'
            folder_list01 = os.listdir(src01)
            for folder_name in folder_list01:
                src02 = src01 + folder_name + '/'
                # print(src02)
                src_list.append(src02)
    return src_list
# print(src_path_list(src00))

for src in src_path_list(src00):
    file_list = os.listdir(src)
    file_list = [file for file in file_list if file.endswith('.jpg')]
    # print(file_list)
    for filename in file_list:
        shutil.move(src + filename, dir + filename)





