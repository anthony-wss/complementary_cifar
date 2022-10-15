import pandas as pd
import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import pickle

data = pickle.load(open("clcifar20.pkl", "rb"))
# data = pickle.load(open("../pcl50000/clcifar10.pkl", "rb"))

# wrong = 0
# total = 0

# for i in range(len(data['ord_labels'])):
#     total += 3
#     for j in range(3):
#         if data['com_labels'][i][j] == data['ord_labels'][i]:
#             wrong += 1

# print(wrong, total, wrong/total)

# Bias among selection per worker

# Bias among each com label
c = np.zeros((20))
for i in range(len(data['ord_labels'])):
    for j in range(3):
        c[data['com_labels'][i][j]] += 1

c /= 150000
c = list(c)
print(max(c), c.index(max(c)))
print(min(c), c.index(min(c)))

# Transition Matrix
# CATEGORIES = ['aquatic_mammals', 'fish', 'flowers', 'food_containers', 'fruit, vegetables and mushrooms', 'household electrical devices', 'household furniture', 'insects', 'large carnivores and bear', 'large man-made outdoor things', 'large natural outdoor scenes', 'large omnivores and herbivores', 'medium-sized mammals', 'non-insect invertebrates', 'people', 'reptiles', 'small mammals', 'trees', 'transportation vehicles', 'non-transportation vehicles']
# # encoder = {CATEGORIES[i]: i for i in range(10)}
# T = np.zeros((20, 20))

# for i in range(len(data['ord_labels'])):
#     for j in range(3):
#         T[data['ord_labels'][i]][data['com_labels'][i][j]] += 1

# for i in range(20):
#     T[i] = T[i] / sum(T[i])

# sns.set(rc={"figure.dpi":300, 'savefig.dpi':300})
# sns.set_context('notebook')
# sns.set_style("ticks")
# sns.set(rc={'figure.figsize':(32, 33)})
# # sns.set(font_scale=0.7)
# sns.set(font_scale=1.5)
# ax = sns.heatmap(T, annot=True, fmt=".2f", cmap="Blues", xticklabels=CATEGORIES, yticklabels=CATEGORIES)
# ax.axes.set_title("Transition Matirx",fontsize=26)
# ax.set_xlabel("distribution of collected labels",fontsize=20)
# ax.set_ylabel("ordinary label",fontsize=20)
# ax.tick_params(labelsize=14)
# plt.yticks(rotation=0)
# plt.xticks(rotation=90)
# plt.savefig("transition_matrix.png")
