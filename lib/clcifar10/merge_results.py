import pandas as pd
import numpy as np

df1 = pd.read_csv("4797418-results.csv")
df2 = pd.read_csv("10000_results.csv")

print(len(df2))

for idx, row in df2.iterrows():
    for i in range(10):
        if len(row[f'Input.image_url_{i+1}'].split('/')) == 3:
            df2 = df2.drop(idx, axis=0)

print(len(df2))

df2 = pd.concat([df1, df2], axis=0)

print(len(df2))
df2.to_csv("10000_results-fix.csv")

for idx, row in df2.iterrows():
    for i in range(10):
        if len(row[f'Input.image_url_{i+1}'].split('/')) == 3:
            print("error!")

for idx, row in df2.iterrows():
    for i in range(1, 11):
        if row[f"Answer.image_{i}"] is np.nan:
            print("error: blank label")
            # print(row)
            # exit()