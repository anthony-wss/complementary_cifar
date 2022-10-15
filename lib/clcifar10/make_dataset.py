import pickle
import pandas as pd
from numpy.random import shuffle, seed
from PIL import Image
from hashlib import sha256

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# [b'batch_label', b'labels', b'data', b'filenames']

batch_data = unpickle("../cifar-10-batches-py/batches.meta")
CATEGORIES =  [s.decode("utf-8") for s in batch_data[b'label_names']]

df = pd.read_csv("clcifar_results.csv")

filenames = []
labels = []
data = []
for i in range(5):
    batch_data = unpickle(f"../cifar-10-batches-py/data_batch_{i+1}")
    filenames.extend([s.decode("utf-8") for s in batch_data[b'filenames']])
    labels.extend(batch_data[b'labels'])
    data.extend(batch_data[b'data'])

cifar10 = {}
for i in range(len(filenames)):
    cifar10[filenames[i]] = (labels[i], data[i])

cl_labels = {k:[] for k in filenames}
worker_ids = {k:[] for k in filenames}
ord_labels = []
images = []
names = []
cate_dec = dict.fromkeys(CATEGORIES)
for i in range(10):
    cate_dec[CATEGORIES[i]] = i

for idx, row in df.iterrows():
    for i in range(1, 11):
        cl_labels[row[f'Input.image_url_{i}'].split('/')[1]].append(cate_dec[row[f"Answer.image_{i}"]])
        worker_ids[row[f'Input.image_url_{i}'].split('/')[1]].append(sha256(row["WorkerId"].encode("utf-8")).hexdigest())

data = {k:[] for k in ["filenames", "data", "ord_labels", "com_labels", "worker_ids"]}

for i in range(len(filenames)):
    data['filenames'].append(filenames[i])
    data['data'].append(cifar10[filenames[i]][1])
    data['ord_labels'].append(cifar10[filenames[i]][0])
    data['com_labels'].append(cl_labels[filenames[i]])
    data['worker_ids'].append(worker_ids[filenames[i]])

pickle.dump(data, open("clcifar10.pkl", "wb"))

df = pd.DataFrame(data, columns=data.keys())
df.to_csv("clcifar10.csv")
