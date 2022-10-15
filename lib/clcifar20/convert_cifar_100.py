from PIL import Image
from tqdm import tqdm
import os

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

data = unpickle("cifar-100-python/meta")

fine_label_names = [s.decode("utf-8") for s in data[b'fine_label_names']]
trainset = unpickle("cifar-100-python/train")
fine_labels = trainset[b'fine_labels']

os.mkdir("./icon/")
for fine_label in fine_label_names:
    os.mkdir("./icon/"+fine_label)

for i in tqdm(range(50000)):
    img = Image.fromarray(trainset[b'data'][i].reshape(3, 32, 32).transpose(1,2,0))
    img.save("./icon/" + fine_label_names[fine_labels[i]] + "/" + trainset[b'filenames'][i].decode("utf-8"))