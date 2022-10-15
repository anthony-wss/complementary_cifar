import json
import pandas as pd
import numpy as np

df = []
df.append(pd.read_csv("10000_results-fix.csv"))
df.append(pd.read_csv("new_batch-1/20000_results.csv"))
df.append(pd.read_csv("new_batch-2/30000_results.csv"))
df.append(pd.read_csv("new_batch-3/40000_results.csv"))
df.append(pd.read_csv("new_batch-4/50000_results.csv"))
df = pd.concat(df)

df.to_csv("clcifar_results.csv", index=False)

# print(df.shape)

# df = df.sort_values(by='Input.image_url_1')

if len(df) != 15000:
    print("error: missing submission")
    exit()
for idx, row in df.iterrows():
    for i in range(1, 11):
        if row[f"Answer.image_{i}"] is np.nan:
            print("error: blank label")
            # print(row)
            # exit()

