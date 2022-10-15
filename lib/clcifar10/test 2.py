import json
import pandas as pd
import numpy as np

df = pd.read_csv("clcifar_results.csv")

print(df.shape)

if len(df) != 15000:
    print("error: missing submission")
    exit()
for idx, row in df.iterrows():
    for i in range(1, 11):
        if row[f"Answer.image_{i}"] is np.nan:
            print("error: blank label")
            exit()

