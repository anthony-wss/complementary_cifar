import numpy as np
import pickle
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

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
super_classes = ['"aquatic_mammals"', '"fish"', '"flowers"', '"food_containers"', '"fruit, vegetables and mushrooms"', '"household electrical devices"', '"household furniture"', '"insects"', '"large carnivores and bear"', '"large man-made outdoor things"', '"large natural outdoor scenes"', '"large omnivores and herbivores"', '"medium-sized mammals"', '"non-insect invertebrates"', '"people"', '"reptiles"', '"small mammals"', '"trees"', '"transportation vehicles"', '"non-transportation vehicles"']
super_cls_sub = {super_classes[i]:coarse_sub[i] for i in range(20)}
fine_to_super = []
for i in range(100):
    for j in range(20):
        if i in coarse_sub[j]:
            fine_to_super.append(j)
            break



# Preprocess this into pickle object
import pandas as pd
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# dict_keys([b'filenames', b'batch_label', b'fine_labels', b'coarse_labels', b'data'])
trainset = unpickle("../cifar-100-python/train")
testset = unpickle("../cifar-100-python/test")

# Make training dataset
filename_to_img = {}
for i in range(len(trainset[b'filenames'])):
    name = trainset[b'filenames'][i].decode("utf-8")
    filename_to_img[name] = trainset[b'data'][i]
df = pd.read_csv("pcl_cifar20.csv")
filenames = []
ord_labels = []
cl_labels = []
worker_ids = []
imgs = []
for _, row in df.iterrows():
    filenames.append(row['filenames'])
    ord_labels.append(int(row['ord_labels']))
    cl_labels.append([int(x) for x in row['cl_labels'][1:-1].split(', ')])
    worker_ids.append([x[1:-1] for x in row['worker_ids'][1:-1].split(', ')])
    imgs.append(filename_to_img[row['filenames']])

data = {}
data['filenames'] = filenames
data['ord_labels'] = ord_labels
data['cl_labels'] = cl_labels
data['worker_ids'] = worker_ids
data['data'] = imgs

mean, std = [0,0,0], [0,0,0]
for i in range(50000):
    imgs[i] = imgs[i].reshape(-1, 3, 32, 32)
imgs = np.vstack(imgs)
print(imgs.shape)

# pickle.dump(data, open("pcl_cifar20_train.pkl", "wb"))
exit()

# Make testing dataset
# filenames = [s.decode("utf-8") for s in testset[b'filenames']]
# imgs = testset[b'data']
# ord_labels = []
# for i in range(len(testset[b'fine_labels'])):
#     ord_labels.append(fine_to_super[testset[b'fine_labels'][i]])

# data = {}
# data['filenames'] = filenames
# data['ord_labels'] = ord_labels
# data['data'] = imgs
# pickle.dump(data, open("pcl_cifar20_test.pkl", "wb"))
# exit()


# Load
data = pickle.load(open("pcl_cifar20.pkl", "rb"))
N = 50000

# Transition Matrix
mat = np.zeros((20, 20))

# filenames                                 squirrel_s_000388.png
# ord_labels                                                   16
# cl_labels                                           [4, 17, 17]
# worker_ids    ['A36VIJRVDLM308', 'AHZ08BLAUVT5I', 'A28WXL7TY...
# Name: 0, dtype: object
for i in range(N):
    for j in range(3):
        mat[data['ord_labels'][i]][data['cl_labels'][i][j]] += 1

for i in range(20):
    mat[i] /= sum(mat[i])

plt.figure(figsize=(22, 20))
sns.heatmap(
    mat, 
    annot=True,
    fmt=".4f",
    cmap='Blues', 
    xticklabels=super_classes, 
    yticklabels=super_classes
)
plt.savefig("heatmap.png")
