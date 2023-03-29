import pickle, requests
import matplotlib.pyplot as plt
import numpy as np
import os
import urllib.request
from tqdm import tqdm
from torch.utils.data import Dataset

def choose_comp_label(labels, ord_label, noise_level):
    if noise_level == "random-1":
        return labels[0]
    elif noise_level == "random-2":
        return labels[1]
    elif noise_level == "random-3":
        return labels[2]
    elif noise_level == "aggregate":
        for cl in labels:
            if labels.count(cl) > 1:
                return cl
        return sample(labels, k=1)[0]
    elif noise_level == "worst":
        if labels.count(ord_label) > 0:
            return ord_label
        return sample(labels, k=1)[0]
    elif noise_level == "zero_diagonal":
        correct_cl = []
        for cl in labels:
            if cl != ord_label:
                correct_cl.append(cl)
        if len(correct_cl) == 0:
            return None
        return sample(correct_cl, k=1)[0]
    elif noise_level == "multiple_cl":
        return labels
    else:
        raise NotImplementedError

class CustomDataset(Dataset):
    def __init__(self, root="./data", noise_level="random-1", transform=None):

        os.makedirs(os.path.join(root, "clcifar10"), exist_ok=True)
        dataset_path = os.path.join(root, "clcifar10", "clcifar10.pkl")

        if not os.path.exists(dataset_path):
            print("Downloading clcifar10(148.3MB)")
            url = "https://clcifar.s3.us-west-2.amazonaws.com/clcifar10.pkl"
            with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url.split('/')[-1]) as t:
                urllib.request.urlretrieve(url, dataset_path, reporthook=lambda b, bsize, tsize: t.update(bsize))

        data = pickle.load(open(dataset_path, "rb"))

        self.transform = transform
        self.input_dim = 3 * 32 * 32
        self.num_classes = 10

        self.targets = []
        self.data = []
        self.ord_labels = []
        for i in range(len(data["cl_labels"])):
            cl = choose_comp_label(data["cl_labels"][i], data["ord_labels"][i], noise_level)
            if cl is not None:
                self.targets.append(cl)
                self.data.append(data["images"][i])
                self.ord_labels.append(data["ord_labels"][i])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        image = self.data[index]
        if self.transform is not None:
            image = self.transform(image)
        return image, self.targets[index]
    
def get_clcifar10(root="./data", noise_level="random-1", transform=None):
    return CustomDataset(root=root, noise_level=noise_level, transform=transform)