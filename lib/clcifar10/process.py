import pickle
import pandas as pd
import matplotlib.pyplot as plt
import traceback

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

batch_data = unpickle("../cifar-10-batches-py/batches.meta")
print([s.decode("utf-8") for s in batch_data[b'label_names']])
exit()

data = {}
data['names'] = [s.decode("utf-8") for s in batch_data[b'filenames']]
data['images'] = batch_data[b'data']
data['ord_labels'] = batch_data[b'labels']

pickle.dump(data, open("test-data.pickle", "wb"))

exit()

img_list = [s.rstrip().split('/')[1] for s in open("img_list.txt").readlines()]

filenames = []
labels = []
data = []
for i in range(5):
    batch_data = unpickle(f"cifar-10-batches-py/data_batch_{i+1}")
    filenames.extend([s.decode("utf-8") for s in batch_data[b'filenames']])
    labels.extend(batch_data[b'labels'])
    data.extend(batch_data[b'data'])

data_names = []
data_img = []
data_label = []

for i in range(len(filenames)):
    if filenames[i] not in img_list:
        data_names.append(filenames[i])
        data_img.append(data[i])
        data_label.append(labels[i])

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
