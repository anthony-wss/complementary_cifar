# Complementary Label Datasets

## Abstract
This repo contains two datasets: CIFAR10 and CIFAR100 with human annotated complementary labels for complementary label learning tasks. We collect this complementary version of CIFAR100 in order to verify two important aspects of complementary label learning:

1. The distribution of complementary label is independent to the feature.
2. Collecting complementary labels can be cheaper than collecting ordinary labels when the number of classes is large.

## Datasets

Here are the links to the main page of each datasets, containing the analysis of collected labels and the benchmark results by [libcll](https://github.com/empennage98/libcll), a pytorch-lightning based machine learning library designed for complementary learning task:

* [CLCIFAR10](https://github.com/anthony-wss/complementary_cifar/blob/44d8f25ae366909aed3a63a2ae1dff4007aa3304/main_pages/CLCIFAR10.md)
* [CLCIFAR20](https://github.com/anthony-wss/complementary_cifar/blob/0a8ca89826264cfb595933a119cb6058b83345db/main_pages/CLCIFAR20.md)

### Reference
* https://www.cs.toronto.edu/~kriz/cifar.html
* https://www.mturk.com
* https://github.com/empennage98/libcll