import numpy as np
from random import shuffle, seed, sample


def unpickle(file):
    import pickle

    with open(file, "rb") as fo:
        dict = pickle.load(fo, encoding="bytes")
    return dict


if __name__ == "__main__":
    metadata = unpickle("../cifar-10-batches-py/batches.meta")
    labels = [s.decode("utf-8") for s in metadata[b"label_names"]]
    img_list = [s.rstrip() for s in open("img_list.txt", "r").readlines()]

    seed(1126)
    shuffle(img_list)

    for s in range(3):
        outfile = open(f"exp-10000-{s+1}.csv", "w")
        header = ""
        for i in range(1, 11):
            header += (
                f"image_url_{i},choice_{i}_1,choice_{i}_2,choice_{i}_3,choice_{i}_4,"
            )
        print(header[:-1], file=outfile)
        for h in range(1000):
            hit_str = ""
            for i in range(10):
                choices = sample(labels, 4)
                hit_str += f"{img_list[h*10+i]},{choices[0]},{choices[1]},{choices[2]},{choices[3]},"
            print(hit_str[:-1], file=outfile)
