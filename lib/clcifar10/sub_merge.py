import json
import pandas as pd
import numpy as np

df = []
df.append(pd.read_csv("4794794-results.csv"))
df.append(pd.read_csv("4794797-results.csv"))
df.append(pd.read_csv("4794798-results.csv"))
df = pd.concat(df)

# print(df.shape)

df = df.sort_values(by='Input.image_url_1')

if len(df) != 3000:
    print("error: missing submission")
    exit()
for idx, row in df.iterrows():
    for i in range(1, 11):
        if row[f"Answer.image_{i}"] is np.nan:
            print("error: blank label")
            exit()

df.to_csv("10000_results.csv", index=False)

