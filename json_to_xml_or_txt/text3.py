import shutil
import glob

src = 'C:/Users/ASIAE-12/Desktop/txt/train_txt/'
dir = 'C:/Users/ASIAE-12/Desktop/txt/val_txt/'
compare = 'C:/Users/ASIAE-12/Desktop/before_val_img/'


src_files = glob.glob(src+'*.txt')
print(src_files[0],len(src_files))
compare_files = glob.glob(compare+'*.jpg')
print(compare_files[0],len(compare_files))
for src_file in src_files:
    filename = src_file[-44:-4]
    for compare_file in compare_files:
        compare_file_name = compare_file[-44:-4]
        if filename in compare_file_name:
            print(filename)
            shutil.move(src_file, dir + filename+'.txt')








