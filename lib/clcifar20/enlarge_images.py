import os, sys
from PIL import Image

from PIL import Image
import os, sys

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

data = unpickle("cifar-100-python/meta")

fine_label_names = data[b'fine_label_names']
coarse_label_names = [s.decode("utf-8") for s in data[b'coarse_label_names']]

new_coarse_label_names = [s.strip() for s in """aquatic_mammals,
fish,
flowers,
food_containers,
fruit_vegetables_and_mushrooms,
household_electrical_devices,
household_furniture,
insects,
large_carnivores_and_bear,
large_man-made_outdoor_things,
large_natural_outdoor_scenes,
large_omnivores_and_herbivores,
medium-sized_mammals,
non-insect_invertebrates,
people,
reptiles,
small_mammals,
trees,
transportation_vehicles,
other_vehicles""".split(',')]

s = """aquatic_mammals: 4, 30, 55, 72, 95
fish: 1, 32, 67, 73, 91
flowers: 54, 62, 70, 82, 92
food_containers: 9, 10, 16, 28, 61
fruit, vegetables and mushrooms: 0, 51, 53, 57, 83
household electrical devices: 22, 39, 40, 86, 87
household furniture: 5, 20, 25, 84, 94
insects: 6, 7, 14, 18, 24
large carnivores and bear: 3, 42, 43, 88, 97
large man-made outdoor things: 12, 17, 37, 68, 76
large natural outdoor scenes: 23, 33, 49, 60, 71
large omnivores and herbivores: 15, 19, 21, 31, 38
medium-sized mammals: 34, 63, 64, 66, 75
non-insect invertebrates: 26, 45, 77, 79, 99
people: 2, 11, 35, 46, 98
reptiles: 27, 29, 44, 78, 93
small mammals: 36, 50, 65, 74, 80
trees: 47, 52, 56, 59, 96
transportation vehicles: 8, 13, 48, 58, 90, 81
other vehicles: 41, 69, 85, 89"""
coarse_sub = [[int(n) for n in a.split(':')[1].split(',')] for a in s.split('\n')]

# print(new_coarse_label_names)
# for n in new_coarse_label_names:
#     os.mkdir(f"./cifar100-large/{n}")

trainset = unpickle("cifar-100-python/train")
testset = unpickle("cifar-100-python/test")
size = 300, 300

# print(trainset[b'data'][0].reshape(32, 32, 3))
# img = Image.fromarray(trainset[b'data'][0].reshape(3, 32, 32).transpose(1,2,0))
# img.show()
# exit()

count = [0] * 20

filenames_list = []

for i in range(len(trainset[b'data'])):
    fine = trainset[b'fine_labels'][i]
    for j in range(20):
        if fine in coarse_sub[j]:
            filenames_list.append(f"{new_coarse_label_names[j]}/{trainset[b'filenames'][i].decode('utf-8')}")
            break

filenames_list.sort()

for name in filenames_list:
    print(name)