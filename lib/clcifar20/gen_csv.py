import numpy as np
from random import shuffle, seed, sample, randint
from tqdm import tqdm

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

# print([b[1:-1] for b in super_classes])
# exit()

def unpickle(file):
    import pickle

    with open(file, "rb") as fo:
        dict = pickle.load(fo, encoding="bytes")
    return dict


if __name__ == "__main__":
    img_list = [s.rstrip() for s in open("filenames_list.txt", "r").readlines()]
    labels = super_classes

    seed(1126)
    shuffle(img_list)

    metadata = unpickle("cifar-100-python/meta")
    fine_labels = [s.decode("utf-8") for s in metadata[b'fine_label_names']]
    name_to_label = {fine_labels[i]:i for i in range(100)}
    trainset = unpickle("cifar-100-python/train")
    sample_images = [[] for _ in range(100)]
    for i in range(len(trainset[b'filenames'])):
        sample_images[trainset[b'fine_labels'][i]].append(trainset[b'filenames'][i].decode("utf-8"))

    sample_images_urls = []
    for i in range(100):
        for j in range(len(coarse_sub)):
            if i in coarse_sub[j]:
                sample_images_urls.append("https://cll-data-collect.s3.us-west-2.amazonaws.com/cifar100-large/" + super_classes[j][1:-1] + '/' + sample_images[i][randint(0,99)])

    for batch in range(0, 5):
        for s in range(3):
            outfile = open(f"batch_{batch+1}-{s+1}.csv", "w")
            header = ""
            for i in range(1, 11):
                header += f"image_url_{i},"
                for j in range(1, 5):
                    header += (
                        f"choice_{i}_{j},sample_img_{i}_{j},"
                    )
            print(header[:-1], file=outfile)
            for h in tqdm(range(1000)):
                hit_str = ""
                for i in range(10):
                    choices = sample(labels, 4)
                    hit_str += f"\"{img_list[batch*10000+h*10+i]}\","
                    for j in range(1, 5):
                        cate = choices[j-1]
                        hit_str += f'{cate},"{cate[1:-1]}.jpg",'
                print(hit_str[:-1], file=outfile)
            outfile.close()
