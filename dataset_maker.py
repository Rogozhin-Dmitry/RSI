import shutil
import os

# csv_file_patch = r'E:\Новая папка (3)\DTSt\China№1\Chinese Traffic Signs\annotations.csv'
# image_catalog_patch = r'E:\Новая папка (3)\DTSt\China№1\Chinese Traffic Signs\images'
# preview_image_catalog_patch = r'E:\Новая папка (3)\DTSt\China№1\Chinese Traffic Signs\preview_image'
# sorted_image_catalog_patch = r'E:\Новая папка (3)\DTSt\China№1\Chinese Traffic Signs\sorted_images'

csv_file_patch = r'E:\Новая папка (3)\DTSt\rtsd-public\classification\rtsd-r3\gt_test.csv'
image_catalog_patch = r'E:\Новая папка (3)\DTSt\rtsd-public\classification\rtsd-r3\test'
preview_image_catalog_patch = r'E:\Новая папка (3)\DTSt\rtsd-public\classification\rtsd-r3\preview_image'
sorted_image_catalog_patch = r'E:\Новая папка (3)\DTSt\rtsd-public\classification\rtsd-r3\sorted_images'
dataset_file = open(csv_file_patch)
next(dataset_file)  # пропуск первой строки
dataset_dict = {}
for i in dataset_file:
    i = i.strip().split(',')
    if i[-1] not in dataset_dict:
        dataset_dict[i[-1]] = [i[0]]
    else:
        dataset_dict[i[-1]].append(i[0])

print('classes:', len(dataset_dict.keys()))
for i in sorted(dataset_dict.keys(), key=int):
    print('class:', i, 'count:', len(dataset_dict[i]))
    shutil.copyfile(os.path.join(image_catalog_patch, dataset_dict[i][-1]),
                    os.path.join(preview_image_catalog_patch, i + '.png'))

    class_patch = os.path.join(sorted_image_catalog_patch, "class_" + str(i))
    os.mkdir(class_patch)
    for j in dataset_dict[i]:
        shutil.copyfile(os.path.join(image_catalog_patch, j), os.path.join(class_patch, j))
