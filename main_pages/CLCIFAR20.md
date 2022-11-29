# CLCIFAR20

This Complementary labeled CIFAR100 dataset contains 3 human annotated complementary labels for all 50000 images in the training split of CIFAR100. We group 4-6 categories as a superclass according to [[1]](https://arxiv.org/abs/2110.12088) and collect the complementary labels of these 20 superclasses. The workers are from Amazon Mechanical Turk(https://www.mturk.com). We randomly sampled 4 different labels for 3 different annotators, so each image would have 3 (probably repeated) complementary labels.

We collect this complementary version of CIFAR100 in order to verify two important aspects of complementary label learning:

1. The distribution of complementary label is independent to the feature.
2. Collecting complementary labels can be cheaper than collecting ordinary labels when the number of classes is large.

## Dataset

Dataset download link: [clcifar20.pkl](https://drive.google.com/u/1/uc?id=1MXRC7o2dwNLyKkFEXTpanV_tnST4-g9G&export=download&confirm=t&uuid=e705fade-8041-401b-b41e-5d8134921352&at=AHV7M3etmk6Nz76Dv5oOU1gSeDiu:1669724190793) (160.2MB)

We use `pickle` package to save and load the dataset objects. Use the function `pickle.load` to load the dataset dictionary object `data` in Python.

```python
data = pickle.load(open("clcifar20.pkl", "rb"))
# keys of data: 'filenames', 'data', 'ord_labels', 'com_labels', 'worker_ids'
```

`data` would be a dictionary object with five keys: `filenames`, `data`, `ord_labels`, `com_labels`, and `worker_ids`.

* `data`: A `numpy.ndarray` of size (3072, ) representing the image data with 3 channels, 32*32 resolution.

* `filenames`: The list of filenames strings. This filenames are same as the ones in CIFAR100

* `ord_labels`: The ordinary labels of the images, and they are labeled from 0 to 19 as follows:

  0: aquatic_mammals
  1: fish
  2: flowers
  3: food_containers
  4: fruit, vegetables and mushrooms
  5: household electrical devices
  6: household furniture
  7: insects
  8: large carnivores and bear
  9: large man-made outdoor things
  10: large natural outdoor scenes
  11: large omnivores and herbivores
  12: medium-sized mammals
  13: non-insect invertebrates
  14: people
  15: reptiles
  16: small mammals
  17: trees
  18: transportation vehicles
  19: non-transportation vehicles

* `com_labels`: Three complementary labels for each image from three different workers.
* `worker_ids`: Three worker ids who submitted these complementary labels for this image. The worker ids are all hashed by sha256 and there would not be any worker id in plaintext in this dataset.
* `label_names`: The 20 super-classes label names list: 'aquatic_mammals', 'fish', 'flowers', 'food_containers', 'fruit, vegetables and mushrooms', 'household electrical devices', 'household furniture', 'insects', 'large carnivores and bear', 'large man-made outdoor things', 'large natural outdoor scenes', 'large omnivores and herbivores', 'medium-sized mammals', 'non-insect invertebrates', 'people', 'reptiles', 'small mammals', 'trees', 'transportation vehicles', 'non-transportation vehicles'

## Analysis

* There are 2.81% "wrong" complementary label submissions which are actually correct labels. These wrong labels make the diagonal of transition matrix to be nonzero.
* Transition matrix
  <img src="https://i.imgur.com/YhjXr7m.png" alt="transition matrix" width="70%"/>

* The complementary label `people` account for 6.68% of all the 150000 submitted labels, while the lable `medium-sized mammals` makes up only 3.68%.

<!-- ## Benchmark

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
| DM           | 15.03%          | 16.10%          | 13.92%    | 19.36%      | -->



## HIT Design

Human Intelligence Task (HIT) is the unit of works in Amazon mTurk. We have several designs to make the submission page friendly:

* Hyperlink to all the 10 problems that decrease the scrolling time
* Example images of the superclasses for better understanding of the categories
* Enlarge the tiny 32\*32 pixels images to 200\*200 pixels for clarity.

![](https://i.imgur.com/wg5pV2S.mp4)

### Reference

[[1]](https://arxiv.org/abs/2110.12088) Jiaheng Wei, Zhaowei Zhu, and Hao Cheng. Learning with Noisy Labels Revisited: A Study Using Real-World Human Annotations. arXiv preprint arXiv:2110.12088, 2021.

* https://www.cs.toronto.edu/~kriz/cifar.html
* https://www.mturk.com
* https://github.com/empennage98/libcll