import pandas as pd
import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import pickle

data = pickle.load(open("clcifar10.pkl", "rb"))

wrong = 0
total = 0

for i in range(len(data['ord_labels'])):
    total += 3
    for j in range(3):
        if data['com_labels'][i][j] == data['ord_labels'][i]:
            wrong += 1

print(wrong, total, wrong/total)

# Bias among selection per worker

# Bias among each com label
c = np.zeros((10))
for i in range(len(data['ord_labels'])):
    for j in range(3):
        c[data['com_labels'][i][j]] += 1

c /= 150000
print(c)

# Transition Matrix
# CATEGORIES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
# # encoder = {CATEGORIES[i]: i for i in range(10)}
# T = np.zeros((10, 10))

# for i in range(len(data['ord_labels'])):
#     for j in range(3):
#         T[data['ord_labels'][i]][data['com_labels'][i][j]] += 1

# for i in range(10):
#     T[i] = T[i] / 15000

# sns.set(rc={"figure.dpi":300, 'savefig.dpi':300})
# sns.set_context('notebook')
# sns.set_style("ticks")
# sns.set(rc={'figure.figsize':(10,10)})
# # sns.set(font_scale=0.7)
# ax = sns.heatmap(T, annot=True, fmt=".2f", cmap="Blues", xticklabels=CATEGORIES, yticklabels=CATEGORIES)
# ax.axes.set_title("Transition Matirx",fontsize=16)
# ax.set_xlabel("distribution of collected labels",fontsize=14)
# ax.set_ylabel("ordinary label",fontsize=14)
# ax.tick_params(labelsize=10)
# plt.yticks(rotation=0)
# plt.xticks(rotation=0)
# plt.savefig("transition_matrix.png")
