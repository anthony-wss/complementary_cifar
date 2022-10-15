import pandas as pd

def unpickle(file):
    import pickle

    with open(file, "rb") as fo:
        dict = pickle.load(fo, encoding="bytes")
    return dict

trainset = unpickle("cifar-100-python/train")
img_list = set()
for i in range(50000):
    if 
for n in trainset[b'filenames']:
    img_list.add(n)
print(len(img_list))
exit()

img_list = set()

for i in range(5):
    df = pd.read_csv(f"batch_{i+1}-1.csv")
    for _, row in df.iterrows():
        for j in range(10):
            if row[f"image_url_{j+1}"] in img_list:
                print(row[f"image_url_{j+1}"])
                exit()
            img_list.add(row[f"image_url_{j+1}"])

print(len(img_list))