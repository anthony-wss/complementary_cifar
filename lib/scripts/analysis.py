import pandas as pd
import numpy as np

df = pd.read_csv("0701_results.csv")

Q = np.zeros((10, 11))

CATEGORIES = ["airplane", "automobile", "truck", "bird", "deer", "dog", "cat", "ship", "horse", "frog", "None of above"]

encode = {CATEGORIES[k]: k for k in range(11)}

tp, tn, fp, fn = 0, 0, 0, 0
s = 0

for idx, row in df.iterrows():
    for i in range(1, 11):
        choices = [row[f"Input.choice_{i}_{j}"] for j in range(1, 5)]
        submission = row[f"Answer.image_{i}"]
        answer = row[f"Input.image_url_{i}"].split('-')[0]

        Q[encode[answer]][encode[submission]] += 1

        s += 1

        if answer in choices:
            if submission == "None of above":
                fn += 1
            elif submission != answer:
                fp += 1
            elif submission == answer:
                tp += 1
        else:
            if submission == "None of above":
                tn += 1
            else:
                fp += 1

print(tp/s, tn/s, fp/s, fn/s, s, tp+tn+fp+fn)

# for i in range(10):
#     Q[i] = Q[i] / sum(Q[i])

# print(Q)
