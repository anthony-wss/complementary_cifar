import pandas as pd
from argparse import ArgumentParser
import json
import numpy as np

def main(args):
    df = pd.read_csv(args.csvfile)

    ans = [list() for _ in range(10)]

    rejected_sub = []
    for idx, row in df.iterrows():
        if row['AssignmentStatus'] == "Rejected":
            rejected_sub.append(idx)
    df = df.drop(rejected_sub, axis=0)
    df = df.reindex()

    for idx, row in df.iterrows():
        obj = json.loads(row['Answer.taskAnswers'][1:-1])
        for i in range(10):
            found = False
            for key, item in obj[f'image_{i+1}'].items():
                if item:
                    ans[i].append(key.split('-')[0])
                    found = True
            if not found:
                ans[i].append(np.nan)

    for i in range(10):
        df[f'Answer.image_{i+1}'] = ans[i]
    
    df = df.drop("Answer.taskAnswers", axis=1)

    outfile = args.csvfile[6:13] + "-results.csv"
    df.to_csv(outfile, index=False)
                    


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--csvfile", type=str, required=True)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args)