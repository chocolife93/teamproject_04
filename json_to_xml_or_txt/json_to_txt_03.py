import os
import xml.etree.ElementTree as ET
import pandas as pd
# import cv2
import json
import glob


# json파일이 들어있는 폴더의 경로를 확인해보고 yolo_label_format_json2txt()의 label_name과 file_name의 인덱스를 수정해줘야 함

# folder_path = 'C:/Users/ASIA-03/Desktop/new/label_H11H21H31/FD_In_H11H21H31_0001_20210112_09.mp4/FD_In_H11H21H31_0001_20210112_09__000.0s.json'
# file_path = 'C:\Users\ASIAE-12\Desktop\label_1\1/FD_In_H11H21H31_0001_20210112_09__000.0s.json'
def yolo_label_format_json2txt(folder_path):
    file_list = os.listdir(folder_path)
    file_list = [file for file in file_list if file.endswith('.json')]
    # print('debug01')
    for file_name in file_list:
        file_path = folder_path + file_name
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
        label_name = list(map(str, file_path.split('/')))[-1]
        label_name = list(map(str, label_name.split('_')))[2]
        label = ['H11H21H31', 'H11H21H32', 'H11H21H33', 'H11H22H31',
                 'H11H22H32', 'H11H22H33', 'H12H21H31', 'H12H21H32',
                 'H12H21H33', '12H22H31', 'H12H22H32', 'H12H22H33']
        try:
            x1y1x2y2 = json_data['content']['object']['annotation']['bboxes'][0]
            x1,y1,x2,y2 = map(float, x1y1x2y2)
            # print('debug02', x1,y1,x2,y2)
            x = str((x1+x2)/2)
            y = str((y1+y2)/2)
            w = str(x2-x1)
            h = str(y2-y1)
            xywh = [x,y,w,h]
            # print('debug03', xywh)
            # label_name = list(map(str, file_path.split('/')))[-1]
            # label_name = list(map(str, label_name.split('_')))[2]
            # label = ['H11H21H31', 'H11H21H32', 'H11H21H33', 'H11H22H31',
            #          'H11H22H32', 'H11H22H33', 'H12H21H31', 'H12H21H32',
            #          'H12H21H33', '12H22H31', 'H12H22H32', 'H12H22H33']
            # # # label_num = [0,1,2,3,4,5,6,7,8,9,10,11]
            for i in range(len(label)):
                if label_name == label[i]:
                    xywh.insert(0, str(label.index(label[i])))
            labelxywh = ' '.join(xywh)
            file_name = list(map(str, file_path.split('/')))[-1][:-5]
            # save_path = 'C:/Users/ASIAE-12/Desktop/label_txt/'
            # 파일 w 모드로 열기 (파일 새로 만듦)
            f = open('{}{}.txt'.format(folder_path, file_name), 'w')
            f.write(labelxywh)
            f.close()
            print('save', '{}.txt'.format(file_name))
        except:
            xywh = ['0','0','0','0']
            # label_name = list(map(str, file_path.split('/')))[-1]
            # label_name = list(map(str, label_name.split('_')))[2]
            # label = ['H11H21H31', 'H11H21H32', 'H11H21H33', 'H11H22H31',
            #          'H11H22H32', 'H11H22H33', 'H12H21H31', 'H12H21H32',
            #          'H12H21H33', '12H22H31', 'H12H22H32', 'H12H22H33']
            # # # label_num = [0,1,2,3,4,5,6,7,8,9,10,11]
            for i in range(len(label)):
                if label_name == label[i]:
                    xywh.insert(0, str(label.index(label[i])))
            labelxywh = ' '.join(xywh)
            file_name = list(map(str, file_path.split('/')))[-1][:-5]
            # save_path = 'C:/Users/ASIAE-12/Desktop/label_txt/'
            # 파일 w 모드로 열기 (파일 새로 만듦)
            f = open('{}{}.txt'.format(folder_path, file_name), 'w')
            f.write(labelxywh)
            f.close()
            print('save', '{}.txt'.format(file_name))





for i in range(1, 173):
    print('folder', i)
    folder_path = 'D:/validation_label/{}/'.format(i)
    yolo_label_format_json2txt(folder_path)