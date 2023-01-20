import glob
from PIL import Image
# img = Image.open('data/src/sample.png')


img_list = glob.glob('C:/Users/ASIAE-12/Desktop/before_val_img/*.jpg')
print(img_list[0], len(img_list))
for image in img_list:
    print(image[-44:])
    img = Image.open(image)
    print(img)
    img_resize = img.resize((640,360))
    img_resize.save('C:/Users/ASIAE-12/Desktop/img/val_img/{}'.format(image[-44:]))
