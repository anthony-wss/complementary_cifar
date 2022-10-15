import pickle
import pandas as pd
from numpy.random import shuffle, seed
from PIL import Image
from hashlib import sha256
import ast

s = """"aquatic_mammals": 4, 30, 55, 72, 95
"fish": 1, 32, 67, 73, 91
"flowers": 54, 62, 70, 82, 92
"food_containers": 9, 10, 16, 28, 61
"fruit, vegetables and mushrooms": 0, 51, 53, 57, 83
"household electrical devices": 22, 39, 40, 86, 87
"household furniture": 5, 20, 25, 84, 94
"insects": 6, 7, 14, 18, 24
"large carnivores and bear": 3, 42, 43, 88, 97
"large man-made outdoor things": 12, 17, 37, 68, 76
"large natural outdoor scenes": 23, 33, 49, 60, 71
"large omnivores and herbivores": 15, 19, 21, 31, 38
"medium-sized mammals": 34, 63, 64, 66, 75
"non-insect invertebrates": 26, 45, 77, 79, 99
"people": 2, 11, 35, 46, 98
"reptiles": 27, 29, 44, 78, 93
"small mammals": 36, 50, 65, 74, 80
"trees": 47, 52, 56, 59, 96
"transportation vehicles": 8, 13, 48, 58, 90, 81
"non-transportation vehicles": 41, 69, 85, 89"""
coarse_sub = [[int(n) for n in a.split(':')[1].split(',')] for a in s.split('\n')]
super_classes = [a.split(':')[0] for a in s.split('\n')]
super_cls_sub = {super_classes[i]:coarse_sub[i] for i in range(20)}
fine_to_super = {}

l = [s[1:-1] for s in super_classes]
print(l)
exit()
for i in range(20):
    print(f"{i}: {l[i]}")
exit()

for i in range(100):
    for gid in range(20):
        if i in list(super_cls_sub.values())[gid]:
            fine_to_super[i] = gid

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# [b'batch_label', b'labels', b'data', b'filenames']

batch_data = unpickle("../cifar-10-batches-py/batches.meta")
CATEGORIES =  super_classes

df = pd.read_csv("batch_results/final_merge/pcl_cifar20.csv")


# [b'filenames', b'batch_label', b'fine_labels', b'coarse_labels', b'data']
trainset = unpickle("cifar-100-python/train")
filenames = [s.decode("utf-8") for s in trainset[b'filenames']]
labels = [fine_to_super[l] for l in trainset[b'fine_labels']]
data = trainset[b'data']

cifar20 = {}
for i in range(len(filenames)):
    cifar20[filenames[i]] = (labels[i], data[i])

cl_labels = {k:[] for k in filenames}
worker_ids = {k:[] for k in filenames}
# cate_dec = dict.fromkeys(CATEGORIES)
# for i in range(20):
#     cate_dec[CATEGORIES[i]] = i

for idx, row in df.iterrows():
    for i in range(1, 11):
        cl_labels[row['filenames']] = [int(l) for l in ast.literal_eval(row['cl_labels'])]
        worker_ids[row['filenames']] = [sha256(w.encode("utf-8")).hexdigest() for w in ast.literal_eval(row['worker_ids'])]

data = {k:[] for k in ["filenames", "data", "ord_labels", "com_labels", "worker_ids"]}

for i in range(len(filenames)):
    data['filenames'].append(filenames[i])
    data['data'].append(cifar20[filenames[i]][1])
    data['ord_labels'].append(cifar20[filenames[i]][0])
    data['com_labels'].append(cl_labels[filenames[i]])
    data['worker_ids'].append(worker_ids[filenames[i]])

pickle.dump(data, open("clcifar20.pkl", "wb"))

df = pd.DataFrame(data, columns=data.keys())
df.to_csv("clcifar20.csv")
