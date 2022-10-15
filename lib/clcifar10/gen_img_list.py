import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

if __name__ == "__main__":
    metadata = unpickle("../cifar-10-batches-py/batches.meta")
    # label_map = metadata[b'label_names']
    labels = [s.decode('utf-8') for s in metadata[b'label_names']]

    # Merge images from 5 batches
    file_names = [[], [], [], [], [], [], [], [], [], []]
    images_data = [[], [], [], [], [], [], [], [], [], []]
    for i in range(1, 5+1):
        dataset = unpickle(f"../cifar-10-batches-py/data_batch_{i}")

        for j in range(len(dataset[b'labels'])):
            images_data[dataset[b'labels'][j]].append(dataset[b'data'][j])
            file_names[dataset[b'labels'][j]].append(dataset[b'filenames'][j])

    # Shuffle the 10 categories
    for c in range(10):
        order = np.random.permutation(5000)
        file_names[c] = np.array(file_names[c])[order]
        images_data[c] = np.array(images_data[c])[order]

    # Preview the first 10 images for each category
    """
    print(labels)
    for i in range(10):
        for j in range(10):
            plt.subplot(10, 10, i*10+j+1)
            plt.imshow(images_data[i][j].reshape(3, 32, 32).transpose([1,2,0]))
    plt.show()
    exit()
    """

    # Take the first 1000 images as samples
    for i in range(10):
        for j in range(5000):
            Image.fromarray(images_data[i][j].reshape(3, 32, 32).transpose([1,2,0])).resize((200, 200)).save("images/" + labels[i] + "/" + file_names[i][j].decode("utf-8"))
        print(f"category {labels[i]} done ({i+1}/10).")
