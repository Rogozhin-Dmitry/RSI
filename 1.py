import pickle
import os
from PIL import Image
import shutil


def main(a):
    with open(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}.pickle', 'rb') as f:
        d = pickle.load(f, encoding='latin1')
    if 'features' not in d:
        return

    if a not in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed'):
        os.mkdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}')

    with open(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}.pickle', 'rb') as f:
        d = pickle.load(f, encoding='latin1')

    c = 0
    data = d['features']
    labels = d['labels']
    for i in range(len(data)):
        im = Image.fromarray(data[i])
        label = labels[i]
        if str(label) not in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}'):
            os.mkdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}' + '\\' + str(label))
        im.save(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}' + '\\' + str(label) + f'\\{c}.png')
        c += 1

    if 'demonstration' not in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}'):
        os.mkdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\demonstration')

    for i in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}'):
        if i == 'demonstration':
            continue
        shutil.copyfile(os.path.join(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\{i}',
                                     os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\{i}')[0]),
                        os.path.join(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed\{a}\demonstration',
                                     i + '.png'))


for name in os.listdir(fr'E:\Новая папка (3)\DTSt\Traffic Signs Preprocessed'):
    if name.endswith('.pickle'):
        name = name.split('.pickle')[0]
        print(name)
        main(name)
