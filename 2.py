import os
import shutil

a = 'valid'

for i in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}'):
    if i == 'demonstration':
        continue
    for j in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\{i}'):
        shutil.copyfile(os.path.join(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\{i}', j),
                        os.path.join(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\final_dataset\{i}', j))
    print(i)
