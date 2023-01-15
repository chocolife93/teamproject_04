import os
import xml.etree.ElementTree as ET
import pandas as pd
import cv2
import json
import glob

def write_to_xml(image_name, image_dict, data_folder, save_folder, xml_template='pascal_voc_template.xml'):
    
    
    # get bboxes
    bboxes = image_dict[image_name]

    
    # read xml file
    tree = ET.parse(xml_template)
    root = tree.getroot()    
    
    # modify
    folder = root.find('folder')
    folder.text = 'Annotations'
    
    fname = root.find('filename')
    fname.text = image_name.split('.')[0] 
    
    src = root.find('source')
    database = src.find('database')
    database.text = 'COCO2017'
    
    
    # size
    img = cv2.imread(os.path.join(data_folder, image_name))
    h,w,d = img.shape
    
    size = root.find('size')
    width = size.find('width')
    width.text = str(w)
    height = size.find('height')
    height.text = str(h)
    depth = size.find('depth')
    depth.text = str(d)
    
    for box in bboxes:
        # append object
        obj = ET.SubElement(root, 'object')

        # print(box)
        # print(bboxes)
        name = ET.SubElement(obj, 'name')
        name.text = box[0]
        
        pose = ET.SubElement(obj, 'pose')
        pose.text = 'Unspecified'

        truncated = ET.SubElement(obj, 'truncated')
        truncated.text = str(0)

        difficult = ET.SubElement(obj, 'difficult')
        difficult.text = str(0)

        bndbox = ET.SubElement(obj, 'bndbox')

        print(box[:])
        try:
            xmin = ET.SubElement(bndbox, 'xmin')
            xmin.text = str(int(box[1]))

            ymin = ET.SubElement(bndbox, 'ymin')
            ymin.text = str(int(box[2]))

            xmax = ET.SubElement(bndbox, 'xmax')
            xmax.text = str(int(box[3]))

            ymax = ET.SubElement(bndbox, 'ymax')
            ymax.text = str(int(box[4]))

        except:
            pass
        #
        # try:
        #     seg = ET.SubElement(obj, 'polygon')
        #     for i in range(0, len(box[1])):
        #         xx = 'x{}'.format(i)
        #         xx = ET.SubElement(seg, 'x{}'.format(i))
        #         xx.text = str(int(box[1][i][0]))
        #         print(xx)
        #         print(xx.text)
        #         yy = 'y{}'.format(i)
        #         yy = ET.SubElement(seg, 'y{}'.format(i))
        #         yy.text = str(int(box[1][i][1]))
        #         print(yy)
        #         print(yy.text)
        # except:
        #     pass


    # save .xml to anno_path
    anno_path = os.path.join(save_folder, image_name.split('.')[0] + '.xml')
    tree.write(anno_path)
    

# main routine
if __name__=='__main__':
    
    # read annotations file
    for i in range(1,173):
        json_list = glob.glob('C:/Users/ASIAE-12/Desktop/label_1/{}/*.json'.format(i))
    print(json_list)

    for json_name in json_list[-4:-20:-1]:
        annotations_path = json_name
        print(annotations_path)

    # annotations_path = 'D:/Fire_Detections/Training/1/S3-N1451MF00092.json'
    # read coco category list
        df = pd.read_csv('coco_categories.csv')
        df.set_index('class', inplace=True)

        # specify image locations
        for i in range(1,173):
            image_folder = 'D:/falldown/Training/image/Abnormal_Behavior_Falldown/image/{}/*'.format(i)

        # specify savepath - where to save .xml files
        savepath = 'D:/work/xml_train'
        if not os.path.exists(savepath):
            os.makedirs(savepath)

        # read in .json format
        with open(annotations_path,'rb') as file:
            doc = json.load(file)
        # print(doc)
        # print(type(doc))

        # get annotations
        annotation = doc['content']['object']['annotation']

        #print(doc['content']['object']['annotation']['bboxes'][0])
        print(annotation)

        # iscrowd allowed? 1 for ok, else set to 0
        iscrowd_allowed = 0

        # initialize dict to store bboxes for each image
        image_dict = {}


        # loop through the annotations in the subset
        for anno in annotation:
            # get annotation for image name
            # image_id = anno['image_id']
            image_name = doc['image']['file_name']

            # get category
            print(anno['class'])
            category = df.loc[int(anno['class'])]['name']
            print(category)
            # ['name']

            # add as a key to image_dict
            if not image_name in image_dict.keys():
                image_dict[image_name] = []

            # append bounding boxes to it
            try:
                box = anno['box']
                # since bboxes = [xmin, ymin, width, height]:
                image_dict[image_name].append([category, box[0], box[1], ((box[2] + box[0] / 2)), ((box[3] + box[1] / 2))])
            except:
                pass

            # try:
            #     polygon = anno['polygon']
            #     image_dict[image_name].append([category, polygon[:]])
            # except:
            #     pass


            # generate.xml files
        for image_name in image_dict.keys():
            write_to_xml(image_name, image_dict, image_folder, savepath)
            print('generated for: ', image_name)
