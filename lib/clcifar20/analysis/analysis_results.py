import pandas as pd
import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

super_classes = [
    'aquatic_mammals', 
    'fish', 
    'flowers', 
    'food_containers', 
    'fruit_vegetables_and_mushrooms', 
    'household electrical devices', 
    'household furniture', 
    'insects', 
    'large carnivores and bear', 
    'large man-made outdoor things', 
    'large natural outdoor scenes', 
    'large omnivores and herbivores', 
    'medium-sized mammals', 
    'non-insect invertebrates', 
    'people', 
    'reptiles', 
    'small_mammals', 
    'trees', 
    'transportation_vehicles', 
    'non-transportation vehicles'
]
encode = {super_classes[i]: i for i in range(20)}
encode['fruit, vegetables and mushrooms'] = 4
encode['transportation vehicles'] = 18
encode['other_vehicles'] = 19
encode['large_man-made_outdoor_things'] = 9
encode['large_natural_outdoor_scenes'] = 10
encode['household_furniture'] = 6
encode['household_electrical_devices'] = 5
encode['non-insect_invertebrates'] = 13
encode['small mammals'] = 16
encode['medium-sized_mammals'] = 12
encode['large_omnivores_and_herbivores'] = 11
encode['large_carnivores_and_bear'] = 8

df = pd.read_csv("cifar100_tiny_results.csv")


mat = np.zeros((20,20))
count = [0 for _ in range(20)]

for _, row in df.iterrows():
    for i in range(10):
        answer = encode[row[f"Input.image_url_{i+1}"].split('/')[0]]
        count[answer] += 1
        submission = encode[row[f"Answer.image_{i+1}"]]
        
        mat[answer][submission] += 1

for i in range(20):
    mat[i] /= sum(mat[i])

plt.figure(figsize=(22, 20))
sns.heatmap(
    mat, 
    annot=True,
    fmt=".4f",
    cmap='Blues', 
    xticklabels=super_classes, 
    yticklabels=super_classes
)
plt.savefig("heatmap.png")

worker_list = []
for idx, row in df.iterrows():
    if row['WorkerId'] not in worker_list:
        worker_list.append(row['WorkerId'])

error_cnt = {}
submitted_images = {}
for worker in worker_list:
    error_cnt[worker] = 0
    submitted_images[worker] = 0


for idx, row in df.iterrows():
    for i in range(10):
        ans = row[f'Input.image_url_{i+1}'].split('/')[0]
        submission = row[f'Answer.image_{i+1}']
        choices = [row[f'Input.choice_{i+1}_{j+1}'] for j in range(4)]
        if ans in choices and submission == ans:
            error_cnt[row['WorkerId']] += 1
    submitted_images[row['WorkerId']] += 10

print(f"Total error rate: {sum(error_cnt.values()) / sum(submitted_images.values())} ({sum(error_cnt.values())}/{sum(submitted_images.values())})")

print("Error rate for each worker:")
workers_error_rate = []
for _, worker in sorted([(error_cnt[worker]/submitted_images[worker], worker) for worker in worker_list], reverse=True):
    print(f"{worker}: {round(error_cnt[worker]/submitted_images[worker], 5)} ({error_cnt[worker]}/{submitted_images[worker]})")
    workers_error_rate.append(error_cnt[worker]/submitted_images[worker])
sns.histplot(x=workers_error_rate)
plt.show()
