import pickle
import pandas as pd
from numpy.random import shuffle, seed
import matplotlib.pyplot as plt

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

batch_data = unpickle("../cifar-10-batches-py/batches.meta")
CATEGORIES =  [s.decode("utf-8") for s in batch_data[b'label_names']]
print(CATEGORIES)
exit()

img_list = [s.rstrip().split('/')[1] for s in open("img_list.txt").readlines()]
# cate_img_list = [s.rstrip() for s in open("img_list.txt").readlines()]

filenames = []
labels = []
data = []
for i in range(5):
    batch_data = unpickle(f"../cifar-10-batches-py/data_batch_{i+1}")
    filenames.extend([s.decode("utf-8") for s in batch_data[b'filenames']])
    labels.extend(batch_data[b'labels'])
    data.extend(batch_data[b'data'])

seed(1126)
indices = list(range(50000))
shuffle(indices)
filenames = [filenames[i] for i in indices]
labels = [labels[i] for i in indices]
data = [data[i] for i in indices]

data_names = [[], [], [], []]
data_img = [[], [], [], []]
data_label = [[], [], [], []]
count = [[0] * 10, [0] * 10, [0] * 10, [0] * 10]
for i in range(len(filenames)):
    if filenames[i] not in img_list:
        cate = labels[i]
        for b in range(4):
            if count[b][cate] < 1000:
                count[b][cate] += 1
                data_names[b].append(filenames[i])
                data_img[b].append(data[i])
                data_label[b].append(labels[i])
                break

for i in range(4):
    data = {}
    data['names'] = data_names[i]
    data['images'] = data_img[i]
    data['ord_labels'] = data_label[i]
    pickle.dump(data, open(f"new_batch-{i+1}/data.pickle", "wb"))

# print(count)
# print(len(img_list), len(filenames))
# print([len(data_img[i]) for i in range(4)])

# print([CATEGORIES[idx] for idx in data_label[0][:10]])

# for i in range(10):
#     plt.subplot(1, 10, i+1)
#     plt.imshow(data_img[0][i].reshape(3, 32, 32).transpose(1, 2, 0))

# plt.show()

exit()

data = {}
data['names'] = data_names
data['images'] = data_img
data['ord_labels'] = data_label

print(len(data['names']), len(data['images']), len(data['ord_labels']))

# print(data['names'][:10])

pickle.dump(data, open("40000-data.pickle", "wb"))

# exit()

meta = unpickle("cifar-10-batches-py/batches.meta")
labels = [s.decode("utf-8") for s in meta[b'label_names']]
label_encode = {}
for i in range(10):
    label_encode[labels[i]] = i

# print(labels)
# print(batch_data[b'labels'][:10])
# print([labels[i] for i in batch_data[b'labels'][:10]])
# print(label_encode)

# for i in range(10):
#     plt.subplot(1, 10, i+1)
#     plt.imshow(batch_data[b'data'][i].reshape(3, 32, 32).transpose(1, 2, 0))
# plt.show()

data = pickle.load(open("10000-data.pickle", "rb"))

# print(len(data['names']), len(data['ord_labels']), len(data['images']))

data['cl_labels'] = []

data_label = {name: [] for name in data['names']}

df = pd.read_csv("10000_results-fix.csv")

for idx, row in df.iterrows():
    for i in range(10):
        data_label[row[f'Input.image_url_{i+1}'].split('/')[1]].append(label_encode[row[f"Answer.image_{i+1}"]])

for name in data['names']:
    data['cl_labels'].append(data_label[name])

pickle.dump(data, open("10000-data.pickle", "wb"))
