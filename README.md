# clcifar

## CLCIFAR10

This Complementary labeled CIFAR10 dataset contains 3 human annotated complementary labels for all 50000 images in the training split of CIFAR10. The workers are from Amazon Mechanical Turk(https://www.mturk.com). We randomly sampled 4 different labels for 3 different annotators, so each image would have 3 (probably repeated) complementary labels.

We collect this complementary version of CIFAR10 in order to verify two important aspects of complementary label learning:

1. The distribution of complementary label is independent to the feature.
2. Collecting complementary labels can be cheaper than collecting ordinary labels when the number of classes is large.

#### Dataset

[link]

We use `pickle` package to save and load the dataset objects. Use the function `pickle.load` to load the dataset dictionary object `data` in Python.

```python
data = pickle.load(open("clcifar10.pkl", "rb"))
# keys of data: 'filenames', 'data', 'ord_labels', 'com_labels', 'worker_ids'
```

The 5 keys of `data` are `filenames`, `data`, `ord_labels`, `cl_labels`, and `worker_ids`.

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

#### Analysis

* There are 3.93% "wrong" complementary label submissions which are actually correct labels. These wrong labels make the diagonal of transition matrix to be nonzero.
* Transition matrix
  ![transition_matrix](/Users/anthony/Desktop/HTlab/mturkcll/pcl50000/transition_matrix.png)

* The category airplane and automobile receives 12.96% and 12.69%, while the category cat and deer receive only 8.85% and 8.30%.

#### Benchmark

#### HIT Design

Human Intelligence Task (HIT) is the unit of works in Amazon mTurk. We have several designs to make the submission page friendly:

* Enlarge the tiny 32\*32 pixels images to 200\*200 pixels for clarity.

### Reference

https://www.cs.toronto.edu/~kriz/cifar.html

https://www.mturk.com