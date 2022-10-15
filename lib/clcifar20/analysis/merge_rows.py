import pandas as pd
import json
import numpy as np

batch_row_results = []
for idx in ['4843800', '4843806', '4843819']:
    batch_row_results.append(pd.read_csv(f"Batch_{idx}_batch_results.csv"))
processed_dfs = []

for df in batch_row_results:
    ans = [list() for _ in range(10)]
    for idx, row in df.iterrows():
        obj = json.loads(row['Answer.taskAnswers'][1:-1])
        for i in range(10):
            name = row[f'Input.image_url_{i+1}']
            found = False
            for key, item in obj[name].items():
                if item:
                    ans[i].append(key.split('/')[0])
                    found = True
            if not found:
                print("error!")
                ans[i].append(np.nan)

    for i in range(10):
        df[f'Answer.image_{i+1}'] = ans[i]

    df = df.drop("Answer.taskAnswers", axis=1)
    processed_dfs.append(df)

processed_dfs = pd.concat(processed_dfs, axis=0)
processed_dfs.to_csv("cifar100_tiny_results.csv", index=False)

# outfile = args.csvfile[6:13] + "-results.csv"
# df.to_csv(outfile, index=False)