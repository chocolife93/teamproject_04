import os
import xml.etree.ElementTree as ET
import pandas as pd
# import cv2
import json
import glob
import math


def x1y1x2y2_to_xywh(x1y1x2y2):
    x1, y1, x2, y2 = map(float, x1y1x2y2)
    x = str((x1+x2)/2)
    y = str((y1+y2)/2)
    w = str(x2-x1)
    h = str(y2-y1)
    xywh = [x,y,w,h]
    return xywh

def fps2sec(json_data):
    # print('json_data : ',json_data)
    fps = math.ceil(json_data['annotations']['fps'])
    # print('fps : ', fps)
    start_sec = math.floor(json_data['annotations']['object'][0]['startFrame']/fps)
    end_sec = math.ceil(json_data['annotations']['object'][0]['endFrame']/fps)
    #print('start_sec : ',start_sec)
    #print('end_sec : ',end_sec)
    return start_sec, end_sec



if __name__ == "__main__":
    labels = {'H11H21H31':'11',
             'H11H21H32':'12',
             'H11H21H33':'13',
             'H11H22H31':'14',
             'H11H22H32':'15',
             'H11H22H33':'16',
             'H12H21H31':'17',
             'H12H21H32':'18',
             'H12H21H33':'19',
             'H12H22H31':'20',
             'H12H22H32':'21',
             'H12H22H33':'22',
             'None':'8'}

    path = 'D:/falldown/'
    T_or_V = ['Training','Validation']
    img_or_vid = ['image', 'video']
    count = 0
    # 비디오 json파일 열기
    for t_or_v_01 in T_or_V:
        vid_path_01 = '{}{}/video/'.format(path,t_or_v_01)
        vid_path_01_names = os.listdir(vid_path_01)
        removed_vid_path_01_name = []
        for i in vid_path_01_names:
            if 'label_' in i:
                removed_vid_path_01_name.append(i)
        # print(removed_vid_path_01_name)
        for vid_path_name in removed_vid_path_01_name:
            vid_path_02 = vid_path_01 + vid_path_name + '/'
            vid_json_paths = glob.glob(vid_path_02+'*.json')
            for vid_json_path in vid_json_paths:
                print('|| vid_json_path || ',vid_json_path)
                with open(vid_json_path, "r") as vid_json_file:
                    vid_json_data = json.load(vid_json_file)
                vid_json_name = vid_json_path[-37:]
                print('|| vid_json_name || ',vid_json_name)
                start_sec, end_sec = fps2sec(vid_json_data) # 비디오 json파일 안의 프레임 시작, 끝 -> 초 변환
                vid_label = vid_json_data['annotations']['object'][0]['actionName']
                img_label = labels[vid_label]
                print('|| vid_label || ',vid_label)
                print('|| img_label || ',type(img_label),img_label)

                # 이름이 같은 이미지 폴더 들어가서 제이슨 파일 열기
                # print(vid_json_path)
                img_json_path = vid_json_path.replace('video','image')
                img_json_path = img_json_path.replace('.json','.mp4/')
                # print(img_json_path)
                img_json_paths = glob.glob(img_json_path+'*.json')
                # print(len(img_json_paths))
                for img_json_path in img_json_paths:
                    print('|| img_json_path || ',img_json_path)
                    img_json_name = img_json_path[-45:]
                    img_json_sec = int(img_json_name[-11:-8])
                    print(img_json_name,img_json_sec)
                    if img_json_sec >= start_sec and img_json_sec <= end_sec:
                        if img_json_path[-45] != '~':
                            with open(img_json_path, "r") as img_json_file: # 이미지 json 파일열기
                                img_json_data = json.load(img_json_file)
                            try:
                                bbox = img_json_data['content']['object']['annotation']['bboxes'][0]
                                print(bbox)
                                print(len(bbox))
                                xywh = x1y1x2y2_to_xywh(bbox)
                                xywh.insert(0, img_label)
                                lxywh = ' '.join(xywh)
                            except:
                                print('empty_bbox')
                                lxywh = '8 0 0 0 0'
                            print('lxywh : ', lxywh)
                    else:
                        if img_json_path[-45] != '~':
                            # img_json_name = img_json_path[:-5]
                            with open(img_json_path, "r") as img_json_file: # 이미지 json 파일열기
                                img_json_data = json.load(img_json_file)
                            try:
                                bbox = img_json_data['content']['object']['annotation']['bboxes'][0]
                                print('bbox : ',bbox)
                                # print(len(bbox))
                                xywh = x1y1x2y2_to_xywh(bbox)
                                xywh.insert(0, '8')
                                lxywh = ' '.join(xywh)
                            except:
                                print('empty_bbox')
                                lxywh = '8 0 0 0 0'
                            print('lxywh : ',lxywh)
                    print(img_json_name)
                    f = open('C:/Users/ASIAE-12/Desktop/val_txt/'+ img_json_name[:-5] + '.txt', 'w')
                    f.write(lxywh)
                    f.close()
