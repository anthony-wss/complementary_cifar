# CLCIFAR10

This Complementary labeled CIFAR10 dataset contains 3 human annotated complementary labels for all 50000 images in the training split of CIFAR10. The workers are from Amazon Mechanical Turk(https://www.mturk.com). We randomly sampled 4 different labels for 3 different annotators, so each image would have 3 (probably repeated) complementary labels.

We collect this complementary version of CIFAR10 in order to verify two important aspects of complementary label learning:

1. The distribution of complementary label is independent to the feature.
2. Collecting complementary labels can be cheaper than collecting ordinary labels when the number of classes is large.

## Dataset

Dataset download link: [clcifar10.pkl](https://drive.google.com/u/1/uc?id=1c-wJ1V_UDCn02S1xYXkJeArYqCvO3Ue0&export=download&confirm=t&uuid=c464f605-e25c-42e6-9d56-cde332b02256&at=AHV7M3dJ5to4SKWSP75oQmrmF8sW:1669724579221) (160.3MB)

We use `pickle` package to save and load the dataset objects. Use the function `pickle.load` to load the dataset dictionary object `data` in Python.

```python
data = pickle.load(open("clcifar10.pkl", "rb"))
# keys of data: 'filenames', 'data', 'ord_labels', 'com_labels', 'worker_ids', 'label_names'
```

`data` would be a dictionary object with five keys: `filenames`, `data`, `ord_labels`, `com_labels`, and `worker_ids`.

* `data`: A `numpy.ndarray` of size (3072, ) representing the image data with 3 channels, 32*32 resolution.

* `filenames`: The list of filenames strings. This filenames are same as the ones in CIFAR10

* `ord_labels`: The ordinary labels of the images, and they are labeled from 0 to 9 as follows:

  0: airplane
  1: automobile
  2: bird
  3: cat
  4: deer
  5: dog
  6: frog
  7: horse
  8: ship
  9: truck

* `com_labels`: Three complementary labels for each image from three different workers.
* `worker_ids`: Three worker ids who submitted these complementary labels for this image. The worker ids are all hashed by sha256 and there would not be any worker id in plaintext in this dataset.
* `label_names`: The 10 label names: 'airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'

## Analysis

* There are 3.93% "wrong" complementary label submissions which are actually correct labels. These wrong labels make the diagonal of transition matrix to be nonzero.
* Transition matrix
  <img src="https://i.imgur.com/RWYm6fm.png" alt="transition matrix" width="70%"/>

* The category airplane and automobile receives 12.96% and 12.69%, while the category cat and deer receive only 8.85% and 8.30%.

## Benchmark

These experiments are run with package `libcll` (github link: https://github.com/empennage98/libcll)

The following accuracies are obtained with 200 epochs, Adam optimizer with lr=1e-4. Only one single complementary label is used, so we consider the first complementary labels of each image.

| Method/Model | ResNet          | DenseNet        | U. ResNet | U. DenseNet |
| ------------ | --------------- | --------------- | --------- | ----------- |
| SCL-NL       | 23.94%          | 22.98% / 28.46% | 36.14%    | 34.41%      |
| SCL-EXP      | 22.55% / 28.48% | 23.31% / 26.32% | 35.78%    | 31.46%      |
| SCL-FWD      | 24.15% / 30.38% | 22.99%          | 36.15%    | 35.10%      |
| URE-GA       | 21.71%          | 23.13%          | 28.53%    | 32.32%      |
| URE-NN       | 10.95%          | 10.52%          | 11.52%    | 10.70%      |
| FWD          | 24.15%          | 22.99%          | 36.15%    | 34.94%      |
| DM           | 15.03%          | 16.10%          | 13.92%    | 19.36%      |



## HIT Design

Human Intelligence Task (HIT) is the unit of works in Amazon mTurk. We have several designs to make the submission page friendly:

* Enlarge the tiny 32\*32 pixels images to 200\*200 pixels for clarity.

![](https://i.imgur.com/SGVCVXV.mp4)

### Reference

* https://www.cs.toronto.edu/~kriz/cifar.html
* https://www.mturk.com
* https://github.com/empennage98/libcll